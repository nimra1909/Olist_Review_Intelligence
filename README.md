# Ask-Your-Data: Olist Analytics & Review Intelligence

**Team 2 Capstone Project**
*SQL + AI/LLM Conversational Analytics Assistant*

---

## Project Overview

An e-commerce company holds two kinds of data: structured order data and unstructured customer reviews.
Managers who don't know SQL should still be able to ask questions like:

> "Which product categories have the worst customer sentiment, and are late deliveries the reason?"

This project builds a complete **Ask-Your-Data** assistant that answers such questions by combining:

1. **SQL Layer** – Real database with proper joins across Olist tables
2. **NLP Layer** – Sentiment analysis + semantic search over Portuguese reviews
3. **LLM Layer** – Natural language → SQL conversion via a schema-aware prompt and the Hugging Face Inference API

All three layers are integrated into a single interactive Streamlit application.

**Live app:** https://olist-capstone-hbl5kjrcmoyccjkd8yszet.streamlit.app/

---

## Team Members

| Name       | Role                                                                 | Contribution Focus                          |
|------------|----------------------------------------------------------------------|---------------------------------------------|
| **Kashmala** | Database design and core SQL queries                               | Schema design, joins, exploratory queries, data-quality fixes |
| **Khaula**   | Database design and core SQL queries                               | Schema design, joins, exploratory queries, data-quality fixes |
| **Laiba**    | Sentiment analysis, embeddings, and semantic search                | Review scoring (84.63% accuracy vs. real star ratings), ChromaDB, multilingual embeddings |
| **Nimra**    | Natural-language-to-SQL pipeline (prompt engineering) + Streamlit App | Text-to-SQL system, prompt engineering, full application development and deployment |

---

## Mission

Build an assistant that lets anyone ask a plain-English question about the business and get a real, trustworthy answer — pulled from the database **and** from what customers actually wrote in their reviews.

---

## Dataset

**Olist Brazilian E-Commerce Public Dataset**
- 9 connected tables (orders, customers, products, sellers, payments, reviews, etc.)
- ~100,000 real customer reviews written in **Portuguese**
- Source: [Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## System Architecture

| Layer              | Technology                              | Responsibility                              |
|--------------------|------------------------------------------|---------------------------------------------|
| **SQL Layer**      | SQLite + SQLAlchemy                     | Structured data querying with multi-table joins |
| **NLP Layer**      | Sentence-Transformers + ChromaDB        | Sentiment scoring + semantic review search  |
| **LLM Layer**      | Hugging Face Inference API (Llama-3.3-70B-Instruct) | Natural language → SQL conversion, via a schema-aware prompt |
| **Interface**      | Streamlit                               | Unified conversational demo application     |

---

## Features

- Ask business questions in plain English
- Automatic SQL generation and execution (with a safety filter blocking destructive queries)
- Sentiment-aware analysis of customer reviews, validated against real star ratings
- Semantic search over Portuguese review text, including cross-lingual (English → Portuguese) matching
- Combined answers (SQL numbers + review evidence)
- Clean and interactive Streamlit interface

---

## Tech Stack

- **Database**: SQLite
- **Backend**: Python, SQLAlchemy
- **Embeddings**: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- **Sentiment Model**: `nlptown/bert-base-multilingual-uncased-sentiment`
- **Vector Store**: ChromaDB
- **LLM**: Hugging Face Inference API (Llama-3.3-70B-Instruct)
- **Frontend**: Streamlit
- **Deployment**: Streamlit Community Cloud

---

## Project Structure

```bash
olist-capstone/
├── app.py                      # Main Streamlit application (built by Nimra)
├── retriever.py                # Semantic search interface over ChromaDB
├── requirements.txt
├── README.md
├── Evaluation_Report.pdf       # Full evaluation report and measured results
├── chroma_db_reviews/          # Persistent vector store
└── notebooks/
    ├── sql_layer.ipynb              # Database loading, schema, core queries (Kashmala & Khaula)
    ├── sentiment_analysis.ipynb     # Sentiment scoring + accuracy evaluation (Laiba)
    ├── semantic_search_build.ipynb  # Embedding generation and ChromaDB build (Laiba)
    └── text_to_sql.ipynb            # Text-to-SQL pipeline, test set, prompt iterations (Nimra)
```

`olist.db` is not stored in this repository due to its size — `app.py` downloads it automatically from Google Drive on first run.

---

## Getting Started

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
export HF_TOKEN=your_hugging_face_token   # Windows (PowerShell): $env:HF_TOKEN="your_token"
streamlit run app.py
```

On Streamlit Community Cloud, set `HF_TOKEN` under the app's **Secrets** settings instead of an environment variable.

---

## Results Summary

- **Text-to-SQL accuracy**: 15/15 on a held-out test set, with 5 documented fixes found and corrected during testing
- **Sentiment accuracy**: 84.63% (95% negative recall, 97% positive precision), validated against real star ratings on 449 reviews
- **Semantic search**: verified relevant, cross-lingual retrieval

Full methodology and analysis in `Evaluation_Report.pdf`.

---

## License

MIT License — see `LICENSE` file / `Evaluation_Report.pdf` for full text.
