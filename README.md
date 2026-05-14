<div align="center">

# 🛒 Flipkart Product Recommender

### AI-Powered Conversational Shopping Assistant

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python"/></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/></a>
  <a href="https://www.langchain.com/"><img src="https://img.shields.io/badge/🦜_LangChain-1.2.18-1C3C3C?style=for-the-badge" alt="LangChain"/></a>
  <a href="https://astra.datastax.com/"><img src="https://img.shields.io/badge/DataStax_AstraDB-Vector_DB-7B42BC?style=for-the-badge&logo=datastax&logoColor=white" alt="AstraDB"/></a>
  <a href="https://groq.com/"><img src="https://img.shields.io/badge/Groq-LLM_Inference-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"/></a>
</p>
<p align="center">
  <a href="https://huggingface.co/"><img src="https://img.shields.io/badge/🤗_HuggingFace-Embeddings-FFD21E?style=for-the-badge&logoColor=black" alt="HuggingFace"/></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/></a>
  <a href="https://kubernetes.io/"><img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes"/></a>
  <a href="https://cloud.google.com/"><img src="https://img.shields.io/badge/Google_Cloud-GCP_VM-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="GCP"/></a>
  <a href="https://vercel.com/"><img src="https://img.shields.io/badge/Vercel-Deployed-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel"/></a>
</p>
<p align="center">
  <a href="https://prometheus.io/"><img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus"/></a>
  <a href="https://grafana.com/"><img src="https://img.shields.io/badge/Grafana-Dashboards-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana"/></a>
  <a href="https://github.com/P-SAIKISHAN/Flipkart-Product-Recommender/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GPL_v3-blue?style=for-the-badge&logo=gnu&logoColor=white" alt="License"/></a>
</p>

> **An intelligent, RAG-powered product recommendation chatbot for Flipkart products — giving users smart, context-aware shopping assistance through natural conversation.**

🔗 **Live Demo:** [flipkart-product-recommender-7tgo.vercel.app](https://flipkart-product-recommender-7tgo.vercel.app/)

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Workflow](#-project-workflow)
- [Tech Stack & Tools](#-tech-stack--tools)
- [System Architecture](#-system-architecture)
- [RAG Pipeline](#-rag-pipeline)
- [Data Ingestion Pipeline](#-data-ingestion-pipeline)
- [Project Structure](#-project-structure)
- [Environment Variables](#-environment-variables)
- [Getting Started](#-getting-started)
- [Docker Deployment](#-docker-deployment)
- [Kubernetes on GCP](#-kubernetes-on-gcp-minikube)
- [Monitoring — Prometheus & Grafana](#-monitoring--prometheus--grafana)
- [API Endpoints](#-api-endpoints)
- [License](#-license)

---

## 🧠 Overview

The **Flipkart Product Recommender** is a full-stack AI application that enables users to have natural language conversations about Flipkart products. Instead of keyword-based search, users can ask questions like *"Show me budget laptops under ₹40,000 with good battery life"* and receive intelligent, contextual responses.

Under the hood, the system uses **Retrieval-Augmented Generation (RAG)** — a cutting-edge AI architecture that combines a vector database (AstraDB) for semantic product search with a Large Language Model (via Groq) to generate human-like, informative answers grounded in real product data.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **Conversational AI** | Chat-style interface for natural product discovery |
| 🔍 **Semantic Search** | Find products by meaning, not just keywords |
| 🧩 **RAG Architecture** | Grounded responses from real product data |
| 💾 **Vector Store** | AstraDB stores product embeddings for fast similarity search |
| 🧠 **HuggingFace Embeddings** | High-quality sentence embeddings for product understanding |
| ⚡ **Groq LLM** | Ultra-fast LLM inference for real-time responses |
| 📊 **Prometheus Metrics** | Built-in observability and HTTP request tracking |
| 📈 **Grafana Dashboards** | Visual monitoring of system health |
| 🐳 **Dockerized** | Easy, reproducible containerized deployment |
| ☸️ **Kubernetes on GCP** | Production-grade deployment on Minikube in a GCP VM |
| 🌐 **Vercel Deployment** | Serverless-compatible Flask application |

---

## 🗺️ Project Workflow

The diagram below shows the complete end-to-end development and deployment workflow — from local setup all the way to cloud monitoring.

![Project Workflow](./Flipkart_product_recommender_Workflow.png)

### Workflow Phases Explained

| Phase | Steps | What Happens |
|---|---|---|
| 🖥️ **Local Project Setup** | Project & API Setup → Config Code → Data Converter → Data Ingestion → RAG Chain → Flask App | All AI and backend code is written and tested locally |
| 🐳 **Containerization & Orchestration** | Dockerfile → Kubernetes Deployment YAML | App is packaged into a Docker image and K8s manifests are defined |
| 📊 **Monitoring Setup** | Prometheus Deployment File → Grafana Deployment File | Observability stack is configured as K8s deployments |
| 🔁 **Version Control** | Code Versioning using GitHub | All code is committed and pushed to GitHub |
| ☁️ **Cloud Deployment** | GCP VM Instance Setup → Build & Deploy on Minikube K8s Cluster | App is deployed on a Kubernetes cluster running inside a GCP VM |
| 📡 **Monitoring** | Prometheus + Grafana live dashboards | Deployed app is monitored in real-time |

---

## 🛠️ Tech Stack & Tools

### 🎨 Frontend

<table>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/></td>
    <td>Chat UI structure and Jinja2 templating</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/></td>
    <td>Responsive styling and layout</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/></td>
    <td>AJAX-based chat interactions (no page reload)</td>
  </tr>
</table>

### ⚙️ Backend

<table>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python"/></td>
    <td><b>Python 3.10</b> — Core programming language</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/></td>
    <td><b>Flask 3.1.3</b> — Lightweight web framework & REST API server</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Gunicorn"/></td>
    <td><b>Gunicorn 26.0.0</b> — Production WSGI server</td>
  </tr>
</table>

### 🤖 AI / ML

<table>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/🦜_LangChain-1C3C3C?style=for-the-badge" alt="LangChain"/></td>
    <td><b>LangChain 1.2.18</b> — RAG orchestration, prompt chaining, conversation memory</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/🤗_HuggingFace-FFD21E?style=for-the-badge&logoColor=black" alt="HuggingFace"/></td>
    <td><b>HuggingFace Hub 1.14.0</b> — Sentence-transformer embedding models for vectorizing products</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"/></td>
    <td><b>langchain-groq 1.1.2</b> — Ultra-fast Groq LLM inference (LLaMA / Mixtral)</td>
  </tr>
</table>

### 💾 Database

<table>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/DataStax_AstraDB-7B42BC?style=for-the-badge&logo=datastax&logoColor=white" alt="AstraDB"/></td>
    <td><b>AstraDB + astrapy 2.2.1</b> — Serverless cloud-native vector database (Cassandra-based). Stores product embeddings and serves similarity search queries.</td>
  </tr>
</table>

### 📊 Monitoring & Observability

<table>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus"/></td>
    <td><b>Prometheus</b> — Scrapes the <code>/metrics</code> endpoint and collects HTTP request counters</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana"/></td>
    <td><b>Grafana</b> — Connects to Prometheus and visualizes app metrics on live dashboards</td>
  </tr>
</table>

### 🚀 DevOps & Infrastructure

<table>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/></td>
    <td><b>Docker</b> — Containerizes the Flask app using <code>python:3.10-slim</code> base image</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes"/></td>
    <td><b>Kubernetes (Minikube)</b> — Orchestrates Flask, Prometheus, and Grafana pods on a cluster</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="GCP"/></td>
    <td><b>Google Cloud Platform</b> — VM instance hosts the Minikube Kubernetes cluster for cloud deployment</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel"/></td>
    <td><b>Vercel</b> — Serverless hosting for the public-facing Flask app</td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></td>
    <td><b>GitHub</b> — Source code versioning and integration hub</td>
  </tr>
</table>

---

## 🏗️ System Architecture

```
┌───────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                                 │
│             HTML / CSS / JavaScript Chat  (Flask Template)             │
└─────────────────────────────┬─────────────────────────────────────────┘
                               │  HTTP POST /get  { msg: "user query" }
                               ▼
┌───────────────────────────────────────────────────────────────────────┐
│                       FLASK APPLICATION  (app.py)                      │
│                                                                        │
│  ┌─────────────┐   ┌───────────────────┐   ┌────────────────────────┐ │
│  │  GET  /     │   │  POST  /get       │   │  GET  /metrics         │ │
│  │  index.html │   │  → RAG Query      │   │  GET  /health          │ │
│  └─────────────┘   └────────┬──────────┘   └────────────────────────┘ │
│                             │ Lazy-loads on first request              │
└─────────────────────────────┼──────────────────────────────────────────┘
                              │
              ┌───────────────┴──────────────────┐
              ▼                                  ▼
┌──────────────────────────┐      ┌──────────────────────────────────────┐
│  DATA INGESTOR           │      │  RAG CHAIN BUILDER                   │
│  data_ingestion.py       │      │  rag_chain.py                        │
│                          │      │                                      │
│  ① Load CSV Products     │      │  ① HuggingFace Embeddings            │
│  ② LangChain Text Split  │      │     (encode user query → vector)     │
│  ③ HuggingFace Embed     │      │                                      │
│  ④ Upsert → AstraDB      │      │  ② AstraDB Similarity Search         │
│                          │      │     (top-K relevant product chunks)  │
└──────────────────────────┘      │                                      │
                                  │  ③ LangChain Prompt Template         │
                                  │     (context + history + query)      │
                                  │                                      │
                                  │  ④ Groq LLM (LLaMA / Mixtral)        │
                                  │     (generate natural answer)        │
                                  │                                      │
                                  │  ⑤ Return answer → Flask → UI        │
                                  └──────────────────┬───────────────────┘
                                                     │
                                ┌────────────────────┴──────────────────┐
                                │          DATASTAX ASTRADB              │
                                │   Serverless Cloud Vector Database     │
                                │   Stores all product embeddings        │
                                │   Serves cosine similarity queries     │
                                └───────────────────────────────────────┘
```

---

## 🔄 RAG Pipeline

```
  USER: "Find me a gaming laptop under ₹60,000"
        │
        ▼
┌───────────────────────────────────────────┐
│  STEP 1 — QUERY EMBEDDING                 │
│  User text → HuggingFace Sentence         │
│  Transformer → 768-dim float vector       │
└──────────────────────┬────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────┐
│  STEP 2 — VECTOR SIMILARITY SEARCH        │
│  Query vector → AstraDB                   │
│  Cosine similarity → Top-K product chunks │
└──────────────────────┬────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────┐
│  STEP 3 — CONTEXT CONSTRUCTION            │
│  Retrieved chunks + Conversation history  │
│  → LangChain Prompt Template              │
│  "Given these products: {context}         │
│   Answer the question: {question}"        │
└──────────────────────┬────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────┐
│  STEP 4 — LLM GENERATION  (Groq API)      │
│  Prompt → Groq LLaMA / Mixtral model      │
│  → Grounded, natural product response     │
└──────────────────────┬────────────────────┘
                       │
                       ▼
        RESPONSE DISPLAYED IN CHAT UI
```

---

## 📥 Data Ingestion Pipeline

```
┌─────────────────┐   ┌──────────────────┐   ┌───────────────────┐
│  Flipkart CSV   │   │  LangChain       │   │  HuggingFace      │
│  Product        │──►│  Text Splitter   │──►│  Embedding Model  │
│  Dataset        │   │  (Chunking)      │   │  (Vectorize text) │
└─────────────────┘   └──────────────────┘   └────────┬──────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────────┐
                                              │   DataStax AstraDB  │
                                              │   Vector Store      │
                                              │   (Upsert / Index)  │
                                              └─────────────────────┘

   load_existing=True  → Skip ingestion, reuse existing vectors
   load_existing=False → Re-embed all products and re-index
```

---

## 📁 Project Structure

```
Flipkart-Product-Recommender/
│
├── app.py                    # Flask app: routes, lazy RAG init, Prometheus metrics
├── setup.py                  # Package setup (pip install -e .)
├── requirements.txt          # All Python dependencies with pinned versions
├── runtime.txt               # Python 3.10 version pin for deployment
├── Dockerfile                # Docker build: python:3.10-slim, exposes port 5000
├── flask-deployment.yaml     # Kubernetes Deployment + Service manifest
├── vercel.json               # Vercel serverless routing configuration
├── .gitignore
│
├── flipkart/                 # ★ Core AI module
│   ├── data_ingestion.py     #   DataIngestor: CSV → chunk → embed → AstraDB
│   └── rag_chain.py          #   RAGChainBuilder: retriever + Groq LLM + prompt
│
├── data/                     # Raw Flipkart product datasets (CSV/JSON)
│
├── utils/                    # Helper utilities
│
├── templates/
│   └── index.html            # Jinja2 chat UI template
│
├── static/                   # CSS, JS, images
│
├── prometheus/
│   └── prometheus.yml        # Scrape config → targets Flask /metrics
│
└── grafana/
    └── dashboard.json        # Pre-built Grafana dashboard for import
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
# ── DataStax AstraDB ──────────────────────────────────────
ASTRA_DB_APPLICATION_TOKEN=AstraCS:your_token_here
ASTRA_DB_API_ENDPOINT=https://your-db-id-region.apps.astra.datastax.com

# ── Groq LLM ──────────────────────────────────────────────
GROQ_API_KEY=gsk_your_groq_key_here

# ── HuggingFace Embeddings ────────────────────────────────
HUGGINGFACEHUB_API_TOKEN=hf_your_token_here

# ── LangSmith Tracing (optional) ─────────────────────────
LANGCHAIN_API_KEY=ls_your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=flipkart-recommender
```

| Variable | Where to get it |
|---|---|
| `ASTRA_DB_APPLICATION_TOKEN` | [astra.datastax.com](https://astra.datastax.com) → Create DB → Generate Token |
| `ASTRA_DB_API_ENDPOINT` | AstraDB dashboard → Connect → API Endpoint |
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) → API Keys |
| `HUGGINGFACEHUB_API_TOKEN` | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+, Git
- AstraDB account (free tier works)
- Groq API key (free)
- HuggingFace token (free)

### 1. Clone the Repository

```bash
git clone https://github.com/P-SAIKISHAN/Flipkart-Product-Recommender.git
cd Flipkart-Product-Recommender
```

### 2. Install Dependencies

```bash
pip install -e .
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env and fill in your API keys
```

### 4. Run Locally

```bash
python app.py
# Visit http://localhost:5000
```

> **First run:** Set `load_existing=False` in `data_ingestion.py` to ingest products into AstraDB. After initial ingestion, switch to `load_existing=True` for faster startups.

---

## 🐳 Docker Deployment

```bash
# Build
docker build -t flipkart-recommender .

# Run
docker run -p 5000:5000 --env-file .env flipkart-recommender
```

---

## ☸️ Kubernetes on GCP (Minikube)

```
┌──────────────────────────────────────────────────────┐
│                  GCP VM Instance                     │
│                                                      │
│  ┌────────────────────────────────────────────────┐  │
│  │             Minikube Cluster                   │  │
│  │                                                │  │
│  │  ┌────────────┐  ┌─────────────┐  ┌────────┐  │  │
│  │  │ Flask Pod  │  │ Prometheus  │  │Grafana │  │  │
│  │  │ port 5000  │  │    Pod      │  │  Pod   │  │  │
│  │  └────────────┘  └─────────────┘  └────────┘  │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

```bash
# Create secrets
kubectl create secret generic flipkart-secrets --from-env-file=.env

# Deploy Flask app
kubectl apply -f flask-deployment.yaml

# Deploy monitoring stack
kubectl apply -f prometheus/
kubectl apply -f grafana/

# Check status
kubectl get pods && kubectl get services
```

---

## 📊 Monitoring — Prometheus & Grafana

| Metric | Type | Description |
|---|---|---|
| `http_requests_total` | Counter | Total HTTP requests across all endpoints |

```bash
# Prometheus (Docker standalone)
docker run -p 9090:9090 \
  -v ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus

# Grafana (Docker standalone)
docker run -p 3000:3000 grafana/grafana
```

Grafana setup: Add Prometheus data source → `http://localhost:9090` → Import `grafana/dashboard.json`

---

## 🌐 API Endpoints

| Method | Endpoint | Description | Response |
|---|---|---|---|
| `GET` | `/` | Renders the chat UI | HTML page |
| `POST` | `/get` | Send user message, receive AI response | Plain text |
| `GET` | `/health` | Health check | `{"status": "healthy"}` |
| `GET` | `/metrics` | Prometheus metrics | Prometheus text format |

```bash
# Example
curl -X POST http://localhost:5000/get \
  -d "msg=Suggest a good gaming laptop under 60000 rupees"
```

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by [P-SAIKISHAN](https://github.com/P-SAIKISHAN)

⭐ **Star this repo if you found it useful!**

[![GitHub stars](https://img.shields.io/github/stars/P-SAIKISHAN/Flipkart-Product-Recommender?style=social)](https://github.com/P-SAIKISHAN/Flipkart-Product-Recommender)

</div>
