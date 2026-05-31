# Compliance-RAG-Copilot

GenAI PDF RAG System with OCR, Hybrid Search, FAISS, Mistral 7B, and FastAPI

## Overview

This project is a production-oriented Retrieval-Augmented Generation (RAG) application that enables users to query information from PDF documents using natural language.

The system supports both digitally generated and scanned PDFs through OCR, performs intelligent document chunking, generates semantic embeddings, stores vectors in FAISS, and retrieves relevant context using a Hybrid Search architecture combining Dense Retrieval (FAISS) and Sparse Retrieval (BM25). Retrieved documents are reranked using a Cross-Encoder before being passed to a locally hosted Mistral 7B model running on Ollama.

The application is built using FastAPI and provides REST APIs for document ingestion and question answering.

---

## Key Features

* PDF document ingestion
* OCR support for scanned PDFs
* Automatic text extraction and cleaning
* Intelligent document chunking
* Semantic embeddings using BGE embeddings
* FAISS vector database
* BM25 keyword retrieval
* Hybrid Search (Dense + Sparse Retrieval)
* Cross-Encoder reranking
* Local LLM inference using Mistral 7B via Ollama
* FastAPI REST APIs
* Source-aware responses
* Fully local deployment
* No external LLM API dependency

---

## Architecture

```text
User Query
    │
    ▼

Query Embedding
    │
    ▼

┌─────────────────────┐
│ Dense Retrieval     │
│ FAISS               │
└─────────────────────┘

┌─────────────────────┐
│ Sparse Retrieval    │
│ BM25                │
└─────────────────────┘

          │
          ▼

Merged Candidate Chunks

          │
          ▼

Cross Encoder Reranker

          │
          ▼

Top Relevant Chunks

          │
          ▼

Prompt Construction

          │
          ▼

Mistral 7B (Ollama)

          │
          ▼

Final Answer
```

---

## Document Ingestion Pipeline

```text
PDF Upload
     │
     ▼

Text Extraction (PyMuPDF)

     │
     ▼

OCR Fallback (Tesseract)

     │
     ▼

Text Cleaning

     │
     ▼

Chunking

     │
     ▼

Embeddings

     │
     ▼

FAISS Index Storage
```

---

## Tech Stack

### Backend

* FastAPI
* Python 3.10+

### LLM

* Mistral 7B
* Ollama

### Retrieval

* FAISS
* BM25
* Cross Encoder Reranker

### Embeddings

* BAAI/bge-small-en-v1.5

### OCR

* Tesseract OCR
* pdf2image
* Pillow

### PDF Processing

* PyMuPDF

### ML/NLP

* Sentence Transformers
* LangChain Text Splitters

---

## Project Structure

```text
rag-pdf-chatbot/

├── app
│   ├── api
│   │   ├── upload.py
│   │   └── query.py
│   │
│   ├── services
│   │   ├── pdf_processor.py
│   │   ├── ocr_service.py
│   │   ├── text_cleaner.py
│   │   ├── chunker.py
│   │   ├── embedding_service.py
│   │   ├── vector_store.py
│   │   ├── bm25_store.py
│   │   ├── retriever.py
│   │   ├── hybrid_retriever.py
│   │   ├── reranker.py
│   │   ├── prompt_builder.py
│   │   └── llm_service.py
│   │
│   ├── models
│   │   ├── request_models.py
│   │   └── response_models.py
│   │
│   ├── config.py
│   └── main.py
│
├── data
│   ├── pdfs
│   └── faiss_index
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git

cd rag-pdf-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull Mistral:

```bash
ollama pull mistral
```

Verify:

```bash
ollama run mistral
```

---

## Install Tesseract OCR

### Ubuntu

```bash
sudo apt update

sudo apt install tesseract-ocr
```

### Windows

Install Tesseract OCR and add it to PATH.

---

## Environment Variables

Create a `.env` file:

```env
MODEL_NAME=mistral

OLLAMA_BASE_URL=http://localhost:11434

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

FAISS_INDEX_PATH=data/faiss_index

PDF_STORAGE=data/pdfs

TOP_K=5
```

---

## Running the Application

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Upload PDF

```http
POST /upload
```

Upload a PDF document and create vector embeddings.

Response:

```json
{
  "filename": "compliance.pdf",
  "chunks": 6,
  "status": "indexed"
}
```

---

### Query Documents

```http
POST /query
```

Request:

```json
{
  "question": "What are the top 5 best practices for compliance?"
}
```

Response:

```json
{
  "answer": "The top 5 best practices from the provided context are...",
  "sources": [
    "Relevant chunk text..."
  ]
}
```

---

## Hybrid Search Workflow

### Dense Retrieval

Uses semantic embeddings and FAISS to retrieve contextually similar chunks.

### Sparse Retrieval

Uses BM25 to retrieve keyword-matching chunks.

### Hybrid Search

Combines results from:

* FAISS
* BM25

Improves retrieval recall and relevance.

---

## Cross Encoder Reranking

After retrieval, a Cross Encoder evaluates:

```text
Query + Chunk
```

pairs and assigns relevance scores.

Only the highest-ranked chunks are passed to the LLM.

Benefits:

* Improved answer accuracy
* Reduced hallucinations
* Better context utilization

---

## Hallucination Reduction Techniques

* Retrieval-Augmented Generation
* Source-grounded prompting
* Hybrid Search
* Cross Encoder reranking
* Limited top-k context
* Context-only answering instructions

---

## Performance Optimizations

* Local LLM inference
* FAISS vector indexing
* Chunk overlap strategy
* Hybrid retrieval
* Reranking
* Context filtering

---

## Future Improvements

* Multi-document support
* Metadata filtering
* Conversational memory
* Streaming responses
* Async FastAPI endpoints
* Docker deployment
* Kubernetes deployment
* Evaluation framework
* Monitoring and observability
* Role-based access control

---

## Sample Use Cases

* Enterprise document search
* Policy and compliance assistants
* Legal document analysis
* Financial report querying
* HR knowledge assistants
* Internal knowledge management systems
* Customer support knowledge bases

---

## License

MIT License

---

## Author

Built using FastAPI, FAISS, Hybrid Search, Cross-Encoder Reranking, and Mistral 7B running locally through Ollama.
