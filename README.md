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

**Step 1 — Download the project**
- Click the green **Code** button on this GitHub page
- Click **Download ZIP**
- Unzip the folder on your computer

**Step 2 — Install Python**
- Go to [python.org](https://www.python.org/downloads/) and download Python 3.8 or higher
- During installation check the box that says **"Add Python to PATH"**

**Step 3 — Open terminal in the project folder**
- **Windows:** open the unzipped folder → click the address bar at the top → type `cmd` → press Enter
- **Mac:** right click the unzipped folder → New Terminal at Folder

**Step 4 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 5 — Run the app**
```bash
streamlit run app/app.py
```

**Step 6 — Open in browser**
- Streamlit will automatically open `http://localhost:8501` in your browser
- If it doesn't open automatically, copy that URL and paste it into Chrome or Firefox

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
