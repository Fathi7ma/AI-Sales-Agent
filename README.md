AI Sales Agent

Overview

This project implements a basic AI-powered sales agent backend that can chat with leads, detect intent, maintain conversation context, and suggest next best actions for a sales representative.

Architecture & Design:
	•	Backend: FastAPI
	•	Intent Detection: Rule-based logic
	•	AI / LLM: OpenAI API used for response generation
	•	Conversation Memory: In-memory storage per lead_id (last 3–5 messages)
	•	Lead Scoring: Simple deterministic logic

AI / LLM Usage & Prompt Strategy:
	•	An LLM is used to generate polite, concise, sales-oriented responses.
	•	A system prompt defines expected sales behavior and tone.
	•	Business logic (intent, scoring, actions) is handled using structured rules.

API Endpoint:

POST /chat

Request:
{
  "lead_id": "123",
  "message": "I want to know the pricing"
}

Response:
{
  "reply": "Our pricing depends on usage. I can share details or arrange a demo if you'd like.",
  "intent": "pricing_inquiry",
  "confidence": 0.85,
  "next_action": "offer_demo",
  "lead_score": 60,
  "lead_status": "warm"
}

How to Run Locally:

pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"
uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs