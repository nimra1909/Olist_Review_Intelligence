# Ask-Your-Data: Olist Analytics & Review Intelligence

**SQL + AI/LLM Conversational Analytics Assistant**

An intelligent conversational analytics assistant that combines **structured e-commerce data, customer review intelligence, sentiment analysis, semantic search, and LLM-powered SQL generation**.

The goal is simple: allow business users who don't know SQL to ask questions in natural language and receive answers backed by real database results and customer reviews.

> **Example:**
> *"Which product categories have the worst customer sentiment, and are late deliveries the reason?"*

---

## Project Overview

The **Ask-Your-Data** assistant brings together three major analytical layers:

1. **SQL Analytics**
   Query structured Olist e-commerce data using real database relationships and multi-table joins.

2. **Review Intelligence**
   Analyze Portuguese customer reviews using sentiment analysis, multilingual embeddings, and semantic search.

3. **LLM-Powered Analytics**
   Convert natural-language business questions into SQL queries using LangChain and an LLM.

These components are integrated into an interactive **Streamlit application** that allows users to explore business data conversationally.

---

## Mission

Build an assistant that allows anyone to ask business questions in plain English and receive trustworthy answers based on:

* Real transactional data
* Customer reviews
* Sentiment analysis
* Semantic similarity
* Database-generated statistics

Instead of manually writing SQL or searching through thousands of reviews, users can simply ask a question.

---

## Team Members

| Member       | Primary Role              | Contribution                                                                               |
| ------------ | ------------------------- | ------------------------------------------------------------------------------------------ |
| **Kashmala** | Database & SQL            | Database schema design, relationships, joins, and exploratory SQL queries                  |
| **Khaula**   | Database & SQL            | Database schema design, relationships, joins, and exploratory SQL queries                  |
| **Laiba**    | NLP & Review Intelligence | Sentiment analysis, multilingual embeddings, ChromaDB, and semantic review search          |
| **Nimra**    | LLM & Application         | Natural-language-to-SQL pipeline, LangChain, prompt engineering, and Streamlit application |

---

## Dataset

The project uses the **Brazilian E-Commerce Public Dataset by Olist**.

The dataset contains approximately **100,000 orders** and associated information covering customers, products, sellers, payments, deliveries, and reviews.

### Main Data Domains

* Orders
* Customers
* Products
* Sellers
* Order items
* Payments
* Reviews
* Geolocation
* Product category translations

**Dataset source:**
Kaggle - Brazilian E-Commerce Public Dataset by Olist

---

## System Architecture

The system consists of four main layers:

```text
                    ┌──────────────────────────┐
                    │       User Question      │
                    │   Natural Language Input │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │     Streamlit Interface  │
                    └────────────┬─────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
                ▼                                 ▼
      ┌──────────────────┐             ┌──────────────────┐
      │   LLM / SQL      │             │ Review Intelligence│
      │     Layer        │             │       Layer       │
      └────────┬─────────┘             └─────────┬─────────┘
               │                                 │
               ▼                                 ▼
      ┌──────────────────┐             ┌──────────────────┐
      │ SQLite Database  │             │ Embeddings +     │
      │ + SQLAlchemy     │             │ ChromaDB         │
      └────────┬─────────┘             └─────────┬─────────┘
               │                                 │
               └────────────────┬────────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │ Combined Business      │
                     │ Answer + Evidence      │
                     └────────────────────────┘
```

---

## Technology Stack

| Layer                 | Technology                              | Purpose                                      |
| --------------------- | --------------------------------------- | -------------------------------------------- |
| **Database**          | SQLite                                  | Store structured Olist data                  |
| **Database Access**   | SQLAlchemy                              | Database connection and query execution      |
| **Programming**       | Python                                  | Core application development                 |
| **Embeddings**        | Sentence-Transformers                   | Convert reviews into semantic vectors        |
| **Embedding Model**   | `paraphrase-multilingual-MiniLM-L12-v2` | Multilingual review embeddings               |
| **Vector Database**   | ChromaDB                                | Store and search review embeddings           |
| **LLM Orchestration** | LangChain                               | Build the natural-language-to-SQL pipeline   |
| **LLM**               | Hugging Face / Groq                     | Generate SQL from natural-language questions |
| **Frontend**          | Streamlit                               | Interactive conversational interface         |
| **Deployment**        | Streamlit Community Cloud               | Application deployment                       |

---

## Key Features

### Natural-Language Business Questions

Users can ask questions without knowing SQL.

Examples:

```text
Which product categories generate the most orders?

Which categories have the lowest customer ratings?

Are late deliveries associated with negative reviews?

Which sellers have the highest number of poor reviews?

What are customers complaining about most?
```

---

### Automatic SQL Generation

The LLM converts natural-language questions into SQL queries.

```text
User Question
      ↓
Prompt + Database Schema
      ↓
LLM
      ↓
Generated SQL
      ↓
SQLite Database
      ↓
Query Results
```

This allows non-technical users to interact with structured business data conversationally.

---

### Sentiment Analysis

Customer reviews are analyzed to identify sentiment and understand customer satisfaction.

The review intelligence layer can help identify:

* Positive reviews
* Negative reviews
* Customer complaints
* Product-related issues
* Delivery-related complaints
* Common themes in customer feedback

---

### Semantic Search

Portuguese customer reviews are converted into multilingual embeddings using:

```text
paraphrase-multilingual-MiniLM-L12-v2
```

The embeddings are stored in **ChromaDB**, allowing the application to retrieve semantically relevant reviews even when the user's wording does not exactly match the review text.

For example:

```text
User:
"Why are customers unhappy with delivery?"

        ↓

Semantic Search

        ↓

Relevant Portuguese reviews

        ↓

Review evidence for analysis
```

---

### Multilingual Review Intelligence

Because the original reviews are written in Portuguese, the project uses a multilingual embedding model to support semantic retrieval across languages.

This allows English-language questions to be connected with relevant Portuguese customer reviews.

---

### Combined Analytics

The assistant combines structured SQL results with unstructured review evidence.

For example:

```text
Business Question
        ↓
 ┌───────────────┬────────────────┐
 │               │                │
 ▼               ▼                │
SQL Analysis   Review Search      │
 │               │                │
 ▼               ▼                │
Business Data  Customer Evidence  │
 └───────────────┴────────────────┘
                │
                ▼
       Combined Answer
```

This makes the system useful for questions where **numbers alone are not enough**.

---

## Example Use Case

A manager asks:

> **"Which product categories have the worst customer sentiment, and are late deliveries the reason?"**

The system can:

1. Convert the business question into an SQL query.
2. Identify product categories with low review scores.
3. Analyze delivery performance.
4. Search customer reviews semantically.
5. Retrieve relevant customer complaints.
6. Combine quantitative results with review evidence.
7. Present the findings through the Streamlit interface.

This connects **what happened in the data** with **what customers actually said**.

---

## Project Structure

```text
olist-capstone/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── # Raw Olist CSV files
│
├── chroma_db_reviews/
│   └── # Persistent ChromaDB vector store
│
├── sql/
│   ├── schema.sql
│   └── queries/
│
├── nlp/
│   ├── sentiment.py
│   ├── embeddings.py
│   └── semantic_search.py
│
└── llm/
    ├── text_to_sql.py
    └── prompts.py
```

> **Note:** Raw dataset files and other large/generated files should not be committed to GitHub unless necessary. Use `.gitignore` for datasets, virtual environments, secrets, and local vector-store files where appropriate.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git

cd <your-repository>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Environment Variables

Create a `.env` file if your selected LLM provider requires an API key.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Never commit API keys or other secrets to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The Streamlit application should then open in your browser.

---

## Security & GitHub Practices

The following files should generally be excluded from version control:

```text
.env
venv/
__pycache__/
*.pyc
data/
chroma_db_reviews/
```

Example `.gitignore`:

```gitignore
# Environment
.env
.venv/
venv/

# Python
__pycache__/
*.pyc

# Dataset
data/

# Vector database
chroma_db_reviews/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## Project Workflow

```text
Olist Dataset
     │
     ├───────────────┐
     │               │
     ▼               ▼
Structured Data   Customer Reviews
     │               │
     ▼               ▼
SQLite          Sentiment Analysis
     │               │
     │          Embeddings
     │               │
     │          ChromaDB
     │               │
     └───────┬───────┘
             │
             ▼
       User Question
             │
             ▼
      LangChain + LLM
             │
             ▼
       SQL Generation
             │
             ▼
     Database Execution
             │
             ├──────────────┐
             │              │
             ▼              ▼
       SQL Results     Review Evidence
             │              │
             └──────┬───────┘
                    ▼
             Final Response
                    │
                    ▼
              Streamlit UI
```

---

## Team Contributions

### Kashmala

* Database schema design
* Table relationships
* SQL joins
* Exploratory SQL queries

### Khaula

* Database schema design
* Table relationships
* SQL joins
* Exploratory SQL queries

### Laiba

* Customer review sentiment analysis
* Multilingual review embeddings
* Sentence-Transformers integration
* ChromaDB vector storage
* Semantic search over customer reviews
* Review intelligence pipeline

### Nimra

* Natural-language-to-SQL pipeline
* LangChain integration
* Prompt engineering
* Streamlit application
* End-to-end application integration

---

## Example Questions

The assistant can be used to explore questions such as:

```text
Which product categories have the lowest review scores?

What are the most common complaints from customers?

Are late deliveries associated with negative reviews?

Which sellers receive the most negative feedback?

Which categories have both high order volume and poor customer sentiment?

What do customers complain about when delivery is late?

Which product categories have improved customer satisfaction?
```

---

## Why This Project?

Traditional business dashboards usually answer predefined questions.

An **Ask-Your-Data** system allows users to ask new questions dynamically.

This project demonstrates the combination of:

* SQL
* Relational databases
* Data analysis
* NLP
* Sentiment analysis
* Vector databases
* Embeddings
* Semantic search
* LLMs
* Prompt engineering
* LangChain
* Streamlit

Together, these technologies create a practical example of **AI-powered business intelligence**.

---

## Future Improvements

Potential future enhancements include:

* Support for additional languages
* More advanced sentiment classification
* Automatic chart generation
* Query validation before SQL execution
* SQL query explanation
* Conversation memory
* More sophisticated review clustering
* Product-level issue detection
* Delivery-delay root-cause analysis
* Dashboard and KPI generation
* LLM-based summarization of retrieved reviews
* Deployment with a production database

---

## License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Team 2 Capstone Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

---

## Capstone Project

**Ask-Your-Data: Olist Analytics & Review Intelligence**

Built with Python, SQL, NLP, embeddings, vector search, LLMs, LangChain, and Streamlit.
