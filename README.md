# Deterministic Conversation Platform

**The control layer behind production Voice AI and Conversational AI systems — built and run locally.**

---

## This Is Not a Chatbot

Most AI demos are chatbots — the LLM decides what to say next based on whatever the user typed. That works in demos. It fails in production.

Real Voice AI systems for legal intake, real estate qualification, or customer support cannot afford free-form LLM behavior. Every conversation must follow a defined path. Every branch must be predictable. Every session must be logged and auditable.

This platform is that control layer — the conversation execution engine that sits underneath the LLM, deciding where the conversation goes regardless of what the user says.

---

## What It Does

A two-mode Streamlit application:

**Build Mode** — Design conversation flows visually:
- Define steps with custom text shown to the user
- Attach up to 3 buttons per step, each routing to a next step
- Special destinations: `end` (completes conversation) or `call` (escalates to human callback)
- Flow validation before running — catches broken links and missing start nodes

**Run Mode** — Execute the flow with full session tracking:
- Unique session ID per conversation
- Full path logging — every node visited in order
- Timestamps — start time, end time, duration in seconds
- Flow versioning — track which version of the flow ran
- Traffic source tracking — where the user came from
- Two outcome states: `completed` or `callback_requested`

---

## Why This Matters in Production

This is the same architectural pattern used in production Voice AI systems.

When I deployed a Voice AI system for a New York law firm handling live legal intake calls, the core reliability layer was exactly this — a deterministic flow engine that decided:

- Which practice area is this caller trying to reach?
- Has the required intake information been collected?
- Does this need a human attorney or can it be handled automatically?
- If the caller says something unexpected — which fallback node handles it?

The LLM handles natural language understanding. This engine handles where the conversation goes next. Separating these two responsibilities is what makes production AI systems auditable and safe.

Without this layer, you have an LLM making routing decisions — which means hallucinated escalations, missed intake steps, and compliance failures.

---

## Session Log Output

Every completed conversation produces a structured log:

```json
{
  "session_id": "a3f2c1d4-...",
  "flow_version": "v1",
  "source": "website",
  "path": ["start", "buy", "residential", "2bhk", "end"],
  "started_at": "2025-03-14T10:23:11",
  "ended_at": "2025-03-14T10:24:45",
  "duration_seconds": 94,
  "outcome": "completed"
}
```

This gives you full auditability — you can reconstruct exactly what path every user took, how long it took, and what the outcome was.

---

## How to Run

**Prerequisites:** Python 3.8+

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

**Quick start:**
1. Select **Build** mode
2. Create a step named `start` — this is where every conversation begins
3. Add buttons routing to other steps or to `end` / `call`
4. Click **Run Chatbot** to execute the flow
5. Session log is printed at conversation end

---

## Tech Stack

- Python
- Streamlit
- UUID for session tracking
- Pure deterministic logic — no LLM, no external APIs

---

## Files

| File | Description |
|------|-------------|
| `app/app.py` | Full application — build mode, run mode, session logging |
| `requirements.txt` | Dependencies |
| `README.md` | This file |

---

## Author

**Kaushal Raj** — Production Voice & Agentic AI Engineer
[GitHub](https://github.com/rajhustle) · [LinkedIn](https://linkedin.com/in/kaushal-raj-a83603380)
