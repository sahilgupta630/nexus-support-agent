l# ShopNow AI Voice Agent Architecture

## Overview
This document outlines the architecture for the ShopNow AI Voice Agent, a highly resilient, multi-turn conversational agent capable of serving Tier-1 customer support needs in English, Hindi, and regional languages. 

## Hybrid RAG Approach & Data Flow

The system employs a **Hybrid RAG** (Retrieval-Augmented Generation) design. The hybrid element refers to combining structured database queries (mock Orders/Returns database) with unstructured vector retrieval (FAISS documentation/policy index) via LangChain's intelligent routing.

### 1. Intent Detection & Routing
When a transcribed user utterance is received, the primary LLM agent (Gemini) determines the intent among:
*   `ORDER_STATUS` -> Routes to structured mock DB lookup.
*   `RETURN_INITIATION` -> Looks up return policy in FAISS and validates against the order DB.
*   `PAYMENT_ISSUE` -> Handled via standard QA or immediate escalation.
*   `DELIVERY_COMPLAINT` -> Registers the complaint structurally, assesses sentiment.
*   `PRODUCT_QUERY` -> Routes strictly to the FAISS RAG index.

### 2. Conversational Memory
The agent maintains an ephemeral `ConversationBufferMemory` context over the session lifecycle. The STT (Speech-to-Text) module retains the user's language preference and enables seamless code-switching.

### 3. Sentiment & Escalation
At each utterance, the LLM provides a hidden sentiment score. If the sentiment crosses a negative threshold, an "Escalation Brief" is constructed containing:
* Customer Name
* Issue Summary
* Sentiment Timeline
* Suggested Human Tone
This brief is subsequently pushed via WebSockets or Server-Sent Events to the React.js operation dashboard.

## System Sequence Flow

```mermaid
sequenceDiagram
    participant User
    participant React Dashboard
    participant FastAPI as FastAPI (Backend)
    participant Speech Services
    participant Engine as Engine (LangChain + Gemini)
    participant FAISS as FAISS (Vector Store)
    
    User->>React Dashboard: Voice Input (Multi-lingual)
    React Dashboard->>FastAPI: Audio Blob Stream
    FastAPI->>Speech Services: STT (Language Detection included)
    Speech Services-->>FastAPI: Transcribed text in source language
    FastAPI->>Engine: Analyze Text (Sentiment + Intent)
    
    alt Knowledge Retrieval Needed
        Engine->>FAISS: Semantic Search
        FAISS-->>Engine: Relevant Chunks
    else SQL/Order Data Needed
        Engine->>FastAPI: Query Mock Database
        FastAPI-->>Engine: JSON Response
    end
    
    Engine-->>FastAPI: Generated Text Response & Metrics
    FastAPI->>Speech Services: TTS Request (in spoken language)
    Speech Services-->>FastAPI: Audio Output
    FastAPI-->>React Dashboard: Audio Stream + Live KPI Metrics
    React Dashboard-->>User: Plays Audio
```
