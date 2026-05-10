# Production-Ready RAG System

A production-style Retrieval-Augmented Generation platform for building internal knowledge assistants, support copilots, and document-question-answering systems.

This project demonstrates how a RAG application can be structured beyond a simple notebook: backend API, Streamlit UI, document ingestion, retrieval pipeline, guardrails, observability hooks, evaluation, tests, Docker, and CI.

---

## Why this project matters

Many RAG demos only show a basic chatbot. This repository is designed to show the engineering around a real system:

- clean application structure
- API-first backend
- user-facing demo app
- retrieval pipeline separation
- safety checks before generation
- evaluation-ready design
- Docker-based deployment
- CI-ready testing

---

## Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
FastAPI Backend
 │
 ├── Guardrails
 │   ├── prompt-injection checks
 │   └── sensitive-data checks
 │
 ├── RAG Pipeline
 │   ├── document loading
 │   ├── chunking
 │   ├── embedding
 │   ├── vector search
 │   └── answer generation
 │
 ├── Evaluation
 │   ├── retrieval checks
 │   └── answer quality metrics
 │
 └── Observability
     ├── structured logging
     └── latency/error tracking
```

---

## Repository structure

```text
api/                    FastAPI backend
app/                    Streamlit frontend
rag/                    Ingestion, retrieval, and generation logic
guardrails/             Input and output safety checks
evaluation/             RAG evaluation helpers
observability/          Logging and monitoring utilities
docs/                   Architecture and roadmap documents
tests/                  Unit tests
.github/workflows/      CI pipeline
```

---

## Features

| Area | What is included |
|---|---|
| API | FastAPI `/health` and `/ask` endpoints |
| UI | Streamlit chat interface |
| Retrieval | Simple local knowledge-base search starter |
| Guardrails | Prompt-injection and sensitive-pattern checks |
| Evaluation | Basic answer/retrieval scoring helper |
| Observability | Structured application logging |
| Deployment | Dockerfile and Docker Compose |
| Quality | Pytest and GitHub Actions CI |

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/ieeexplorer/production-ready-rag-system.git
cd production-ready-rag-system
git checkout production-hardening-strategy
```

### 2. Create environment file

```bash
cp .env.example .env
```

### 3. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 4. Run API

```bash
uvicorn api.main:app --reload --port 8000
```

Open:

```text
http://localhost:8000/docs
```

### 5. Run Streamlit UI

```bash
streamlit run app/streamlit_app.py
```

---

## Docker usage

```bash
docker compose up --build
```

Services:

| Service | URL |
|---|---|
| FastAPI | http://localhost:8000 |
| API docs | http://localhost:8000/docs |
| Streamlit | http://localhost:8501 |

---

## Example API request

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this system designed for?"}'
```

---

## Example response

```json
{
  "answer": "This system is designed to demonstrate a production-style RAG platform...",
  "sources": ["data/sample_knowledge_base.txt"],
  "blocked": false
}
```

---

## Production roadmap

See:

```text
docs/PRODUCTION_HARDENING_STRATEGY.md
```

Recommended next production upgrades:

1. Replace starter search with ChromaDB-backed vector retrieval.
2. Add OpenAI or Azure OpenAI answer generation.
3. Add RAGAS evaluation pipeline.
4. Add authentication and rate limiting.
5. Add Azure Container Apps or AWS ECS deployment.
6. Add monitoring dashboard and tracing.

---

## Skills demonstrated

- Python backend engineering
- FastAPI API design
- Streamlit application development
- RAG system architecture
- LLM safety and guardrails
- Docker deployment
- CI/testing workflow
- Production documentation
- AI platform engineering mindset

---

## CV-ready project description

Built a production-style Retrieval-Augmented Generation system using FastAPI, Streamlit, Docker, guardrails, evaluation utilities, and structured logging. Designed the repository to demonstrate enterprise AI engineering practices including API-first architecture, safety checks, test automation, deployment readiness, and a clear roadmap for cloud productionisation.
