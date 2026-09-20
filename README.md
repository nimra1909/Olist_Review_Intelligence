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

---

Markdown---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>
2. Set Up Virtual EnvironmentBashpython -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Run the Streamlit ApplicationBashstreamlit run app.py
👥 Team Members & ContributionsMemberPrimary Focus & DeliverablesKashmalaDatabase design and core SQL queries.   KhaulaDatabase design and core SQL queries.   LaibaSentiment analysis, embeddings, and semantic search.   NimraNatural-language-to-SQL pipeline (LangChain + prompt engineering).   📄 LicenseThis project is licensed under the MIT License — see below for details:PlaintextMIT License

Copyright (c) 2026 Team 2 Capstone Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



