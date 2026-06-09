# ShopNow AI Voice Agent

Version 1.0 of the ShopNow D2C AI Voice Agent for automated Tier-1 support and intelligent human escalation.

## Overview
This platform employs a Hybrid RAG architecture using Langchain, Gemini (Mocked in offline dev mode), FAISS for policy retrieval, and a simulated database for live order lookups. It includes semantic routing for 5 core intents and includes an aesthetic React dashboard for live operations monitoring.

## Services Architecture
* **Backend:** FastAPI, LangChain, FAISS Vector Store, Sarvam AI/Bhashini Mock services.
* **Frontend:** React + Vite, Recharts, Lucide-React, Glassmorphism customized aesthetic.
* **Deployment:** Containerized with Docker Compose.

## Core Features
1. **Multi-turn Multi-lingual Conversations:** Context-aware routing for English, Hindi, and Regional languages.
2. **Sentiment Analysis:** Utterance-level negative sentiment thresholds triggering instant intelligent escalation.
3. **Daily Operations Reporting:** Real-time metrics visualization (Call Volume, Intent distribution, Resolution rates).

## Getting Started

### Prerequisites
* Docker and Docker Compose installed on Windows/macOS.

### Running the Application

1. Clone or navigate to the repository on your local machine.
2. Build and run the orchestrated containers:
```bash
docker-compose up --build
```
3. **Frontend Dashboard:** Available at `http://localhost:80`
4. **Backend API Docs:** Available at `http://localhost:8000/docs`

### Architecture Docs
Please review `docs/architecture.md` for a comprehensive sequence flow of the AI routing logic.
