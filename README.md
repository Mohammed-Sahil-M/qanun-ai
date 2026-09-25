# Qanun AI (قانون) - Dubai Real Estate Document Intelligence

Qanun AI is an enterprise-grade RAG (Retrieval-Augmented Generation) application built to analyze Dubai real estate contracts, lease agreements, and legal documents.

## Problem Statement
Real estate brokers and tenants in Dubai spend 2-3 hours manually reviewing complex property contracts to identify penalty clauses, transfer conditions, and hidden terms. Qanun AI provides instant, grounded document intelligence to extract clauses and answer questions with citations.

## Tech Stack
- **Frontend:** Streamlit (Interactive Chat & Drag-and-Drop PDF Upload)
- **Backend:** FastAPI (Async REST API Server)
- **Vector Database:** ChromaDB (Local Persistent Embeddings Store)
- **Database:** PostgreSQL / SQLite (Session Audit Logs & User Records)
- **LLM Engine:** Groq / Llama-3 via LangChain LCEL
