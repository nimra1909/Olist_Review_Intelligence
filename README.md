# Ask-Your-Data: Olist Analytics & Review Intelligence

**Capstone Project**  
*SQL + AI/LLM Conversational Analytics Assistant*

---

## Project Overview

An e-commerce company holds two kinds of data: structured order data and unstructured customer reviews.  
Managers who don’t know SQL should still be able to ask questions like:

> “Which product categories have the worst customer sentiment, and are late deliveries the reason?”

This project builds a complete **Ask-Your-Data** assistant that answers such questions by combining:

1. **SQL Layer** – Real database with proper joins across Olist tables  
2. **NLP Layer** – Sentiment analysis + semantic search over Portuguese reviews  
3. **LLM Layer** – Natural language → SQL conversion using LangChain + prompt engineering  

All three layers are integrated into a single interactive Streamlit application.

---

## Team Members

| Name       | Role                                                                 | Contribution Focus                          |
|------------|----------------------------------------------------------------------|---------------------------------------------|
| **Kashmala** | Database design and core SQL queries                               | Schema design, joins, exploratory queries   |
| **Khaula**   | Database design and core SQL queries                               | Schema design, joins, exploratory queries   |
| **Laiba**    | Sentiment analysis, embeddings, and semantic search                | Review scoring, ChromaDB, multilingual embeddings |
| **Nimra**    | Natural-language-to-SQL pipeline (LangChain + prompt engineering) + Streamlit App | Text-to-SQL system, prompt engineering, and full application development |

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
|--------------------|-----------------------------------------|---------------------------------------------|
| **SQL Layer**      | SQLite + SQLAlchemy                     | Structured data querying with multi-table joins |
| **NLP Layer**      | Sentence-Transformers + ChromaDB        | Sentiment scoring + semantic review search  |
| **LLM Layer**      | LangChain + LLM (Hugging Face / Groq)   | Natural language → SQL conversion           |
| **Interface**      | Streamlit                               | Unified conversational demo application     |

---

## Features

- Ask business questions in plain English
- Automatic SQL generation and execution
- Sentiment-aware analysis of customer reviews
- Semantic search over Portuguese review text
- Combined answers (SQL numbers + review evidence)
- Clean and interactive Streamlit interface

---

## Tech Stack

- **Database**: SQLite  
- **Backend**: Python, SQLAlchemy  
- **Embeddings**: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`  
- **Vector Store**: ChromaDB  
- **LLM Orchestration**: LangChain  
- **Frontend**: Streamlit  
- **Deployment**: Streamlit Community Cloud  

---

## Project Structure

```bash
olist-capstone/
├── app.py                      # Main Streamlit application (built by Nimra)
├── requirements.txt
├── README.md
├── data/                       # (not committed) Raw CSVs
├── chroma_db_reviews/          # Persistent vector store
├── sql/                        # Core SQL queries and schema
├── nlp/                        # Sentiment + embedding modules
└── llm/                        # Text-to-SQL pipeline (LangChain)
