"""
Olist Ask-Your-Data Assistant
Team 2 Capstone — Streamlit App

Combines:
- Text-to-SQL layer (Hugging Face LLM + SQLite database)
- Semantic search layer (ChromaDB + multilingual embeddings, built by Laiba)

Run locally:
    streamlit run app.py

Required in the same folder:
    olist.db                  (the SQL database, from Kashmala/Khaula)
    chroma_db_reviews/         (the Chroma vector store folder, from Laiba)
    retriever.py                (Laiba's retriever module)

Required secret:
    HF_TOKEN                    (Hugging Face API token, set as an environment
                                  variable or in .streamlit/secrets.toml)
"""

import os
import streamlit as st
from sqlalchemy import create_engine
from huggingface_hub import InferenceClient

# retriever.py must sit next to this file (Laiba's module)
from retriever import retrieve_reviews

# --------------------------------------------------------------------------
# CONFIG
# --------------------------------------------------------------------------

DB_PATH = "olist.db"
MODEL = "meta-llama/Llama-3.3-70B-Instruct"

# Google Drive file ID for olist.db (used only if the file isn't already
# present locally - e.g. on first run on Streamlit Cloud, where the DB
# is too large to keep in the GitHub repo).
GDRIVE_FILE_ID = "1JHdBKvbbT0VAkmYlo9S__W21R9DtJ0br"


def ensure_database_downloaded():
    """Download olist.db from Google Drive if it isn't already present."""
    if os.path.exists(DB_PATH):
        return
    import gdown
    url = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"
    with st.spinner("Downloading database (first run only, ~65MB)..."):
        gdown.download(url, DB_PATH, quiet=False)

# Questions where showing review evidence doesn't make sense (pure counts/stats)
NO_REVIEW_KEYWORDS = [
    "how many", "total number", "count of", "unique", "average delivery time",
    "which payment", "average review score", "average freight",
]

SYSTEM_PROMPT = """You are a SQL expert working with the Olist e-commerce database.

Schema:
{schema}

Important notes:
- product_category_name is in Portuguese. To get English category names, join products.product_category_name to product_category_name_translation.product_category_name, and use product_category_name_english.
- order_delivered_customer_date vs order_estimated_delivery_date determines if a delivery was late. Only compare these when order_delivered_customer_date IS NOT NULL, since undelivered/cancelled orders have NULL dates and should be excluded from "late/on-time" comparisons, not counted as on-time.
- "Revenue" means product price only (oi.price), not including freight_value, unless the question explicitly asks about shipping/freight costs.
- When counting "number of orders", use COUNT(DISTINCT order_id), not COUNT(order_id) — an order can contain multiple items, which would otherwise inflate the count.
- Be careful when joining order_items to order-level data (like order_reviews or orders) for averages/counts: an order can have multiple items, which duplicates rows and skews AVG() or COUNT() results. When aggregating order-level values, first get distinct order_ids before joining, or aggregate at the order level before joining to item-level category data. See Example 2 below for the correct pattern.
- To count unique/distinct customers (people), use customer_unique_id, not customer_id. customer_id is generated per-order, so the same person gets a different customer_id on each order — COUNT(DISTINCT customer_id) does not give the real number of unique customers.
- Only output a single valid SQLite query. No explanation, no markdown, no backticks.

Example 1:
Question: What is total revenue by English product category?
SQL: SELECT t.product_category_name_english, SUM(oi.price) as revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
GROUP BY t.product_category_name_english
ORDER BY revenue DESC;

Example 2 (correct handling of order_items joined to order-level data, avoiding row duplication):
Question: Which product categories have the worst average review score?
SQL: SELECT t.product_category_name_english, AVG(orv.review_score) as avg_score
FROM (SELECT DISTINCT order_id, product_id FROM order_items) oi
JOIN products p ON oi.product_id = p.product_id
JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
JOIN order_reviews orv ON oi.order_id = orv.order_id
GROUP BY t.product_category_name_english
ORDER BY avg_score ASC;

Now write SQL for this question:
{question}
"""


# --------------------------------------------------------------------------
# CACHED SETUP (runs once, reused across every question)
# --------------------------------------------------------------------------

@st.cache_resource
def get_engine():
    ensure_database_downloaded()
    return create_engine(f"sqlite:///{DB_PATH}")


@st.cache_resource
def get_hf_client():
    token = os.environ.get("HF_TOKEN") or st.secrets.get("HF_TOKEN", None)
    if not token:
        st.error(
            "No Hugging Face token found. Set HF_TOKEN as an environment "
            "variable or in .streamlit/secrets.toml before running the app."
        )
        st.stop()
    return InferenceClient(token=token)


@st.cache_data
def get_schema(_engine):
    with _engine.connect() as conn:
        tables = conn.exec_driver_sql(
            "SELECT name FROM sqlite_master WHERE type='table';"
        ).fetchall()
        schema_str = ""
        for (table,) in tables:
            cols = conn.exec_driver_sql(f"PRAGMA table_info({table});").fetchall()
            col_list = ", ".join(f"{c[1]} ({c[2]})" for c in cols)
            schema_str += f"Table {table}: {col_list}\n"
        return schema_str


# --------------------------------------------------------------------------
# CORE PIPELINE FUNCTIONS
# --------------------------------------------------------------------------

def generate_sql(question, schema, client):
    prompt = SYSTEM_PROMPT.format(schema=schema, question=question)
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        model=MODEL,
        max_tokens=300,
        temperature=0,
    )
    return response.choices[0].message.content.strip()


def run_query(sql, engine):
    forbidden = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]
    if any(word in sql.upper() for word in forbidden):
        raise ValueError("Blocked: only SELECT queries are allowed.")
    with engine.connect() as conn:
        result = conn.exec_driver_sql(sql)
        return result.fetchall(), list(result.keys())


def should_fetch_reviews(question):
    q = question.lower()
    return not any(kw in q for kw in NO_REVIEW_KEYWORDS)


def ask_question(question, engine, schema, client, include_reviews=True):
    sql = generate_sql(question, schema, client)
    rows, cols = run_query(sql, engine)

    reviews = []
    if include_reviews:
        reviews = retrieve_reviews(question, top_k=5)
        # Prefer lower-scoring reviews when the question implies a problem
        problem_words = ["late", "delay", "worst", "bad", "complaint", "defect", "damage"]
        if any(w in question.lower() for w in problem_words):
            negative = [r for r in reviews if r.get("review_score") and int(r["review_score"]) <= 3]
            if negative:
                reviews = negative
        reviews = reviews[:3]

    return {"question": question, "sql": sql, "rows": rows, "cols": cols, "reviews": reviews}


# --------------------------------------------------------------------------
# STREAMLIT UI
# --------------------------------------------------------------------------

st.set_page_config(page_title="Olist Ask-Your-Data Assistant", page_icon="🛍️", layout="wide")

st.title("Ask-Your-Data: Olist Analytics Assistant")
st.caption(
    "Ask a plain-English question about orders, deliveries, revenue, or customer "
    "reviews, the assistant turns it into SQL, runs it, and pulls supporting "
    "review evidence when relevant."
)

engine = get_engine()
client = get_hf_client()
schema = get_schema(engine)

with st.expander("Example questions"):
    st.markdown(
        """
- Which product categories have the most late deliveries?
- Is there a relationship between delivery delay and review score?
- What is total revenue by product category?
- Which sellers have the highest number of orders?
- What percentage of orders are delivered late overall?
        """
    )

question = st.text_input("Ask a question about the business:", placeholder="e.g. Which product categories have the most late deliveries?")

include_reviews = st.checkbox(
    "Include supporting customer review evidence (when relevant)", value=True
)

if st.button("Ask", type="primary") and question:
    with st.spinner("Generating SQL and fetching results..."):
        try:
            fetch_reviews = include_reviews and should_fetch_reviews(question)
            result = ask_question(question, engine, schema, client, include_reviews=fetch_reviews)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.stop()

    st.subheader("Answer")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("**Generated SQL**")
        st.code(result["sql"], language="sql")

        st.markdown("**Result**")
        if result["rows"]:
            st.dataframe(
                [dict(zip(result["cols"], row)) for row in result["rows"][:20]],
                use_container_width=True,
            )
        else:
            st.info("Query ran successfully but returned no rows.")

    with col2:
        if result["reviews"]:
            st.markdown("**Supporting customer reviews**")
            for r in result["reviews"]:
                score = r.get("review_score", "?")
                st.markdown(f"⭐ **{score} stars**")
                st.write(r.get("review", ""))
                st.divider()
        elif fetch_reviews:
            st.markdown("**Supporting customer reviews**")
            st.info("No closely matching reviews found for this question.")

st.markdown("---")
st.caption(
    "Built for the Olist E-Commerce Analytics Capstone · SQL layer: Kashmala & Khaula · "
    "Sentiment & semantic search: Laiba · Text-to-SQL pipeline: Nimra"
)
