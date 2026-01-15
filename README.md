# Deterministic Conversation Platform

A production-grade, deterministic conversation engine for building guided chat and voice workflows with full session tracking, branching, and outcome analytics.

This project implements the **control layer behind AI agents** — the same layer used by platforms like Retell, call-center bots, and conversational automation systems — where predictable behavior, routing, and auditability are more important than free-form AI text.

---

## 🚀 What this platform does

This is **not** a chatbot.  
It is a **conversation execution engine**.

It allows you to define and run structured conversation flows such as:
start → buy → residential → 2 BHK → book callback


And it tracks everything about the session:
- Where the user went
- How long it took
- What outcome occurred
- What data was captured

---

## 🔑 Core Features

- **Deterministic flow engine**
  - Button-driven branching & sub-branching
  - No intent detection, no hallucinations

- **Session tracking**
  - Unique session IDs
  - Full conversation path
  - Start time, end time, duration

- **Outcome tracking**
  - Completed
  - Callback requested
  - Dropped off

- **Data capture**
  - Phone numbers, email, or any user input
  - Stored against the session

- **Validation**
  - Prevents broken flows
  - Detects invalid links between steps

---

## 📊 Example Session Log

```json
{
  "session_id": "b8b36909-322d-4c1a-af88-70b472c99f45",
  "path": ["start", "residential", "bhk_2", "yes"],
  "started_at": "2026-01-07T16:31:10",
  "ended_at": "2026-01-07T16:31:51",
  "duration_seconds": 41,
  "outcome": "callback",
  "captured_data": {
    "contact": "9876543210"
  }
}



🖥️ How to run locally
1. Install dependencies
pip install -r requirements.txt

2. Start the app
streamlit run app.py

3. Open in browser
http://localhost:8501


🧩 Use cases
Voice bots (Retell-style systems)

Lead qualification

Appointment booking

Sales routing

Support triage

Compliance-driven chat

AI agent control layers

🧑‍💻 Author
Built by Kaushal raj
Applied Conversational & Generative AI Engineer



