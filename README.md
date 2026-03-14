# Deterministic Conversation Platform

**The control layer behind production Voice AI and Conversational AI systems — build, run, and deploy in minutes.**

[![Open Live Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://deterministic-conversation-platform-rd9lwwlgsp3a6tkp3lqrv9.streamlit.app/)

🟢 **[Click here to try the live demo](https://deterministic-conversation-platform-rd9lwwlgsp3a6tkp3lqrv9.streamlit.app/)** — no install, no signup, runs in your browser.

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
streamlit run app.py
```

> **Note:** Run this command from inside the `app` folder, not the root folder.

**Step 6 — Open in browser**
- Streamlit will automatically open `http://localhost:8501` in your browser
- If it doesn't open automatically, copy that URL and paste it into Chrome or Firefox


---

## Quick Start Example — Real Estate Qualification Bot

This example builds a working 5-step property inquiry bot in under 2 minutes.

### Step 1 of 5 — The Entry Point

| Field | What to type |
|-------|-------------|
| Step name | `start` |
| Text shown to user | `Welcome! Are you looking to buy or rent a property?` |
| Button 1 label | `Buy` |
| Button 1 goes to | `buy` |
| Button 2 label | `Rent` |
| Button 2 goes to | `rent` |

Click **Save Step** ✓

---

### Step 2 of 5 — Buy Branch

| Field | What to type |
|-------|-------------|
| Step name | `buy` |
| Text shown to user | `What type of property are you looking for?` |
| Button 1 label | `Apartment` |
| Button 1 goes to | `apartment` |
| Button 2 label | `Villa` |
| Button 2 goes to | `villa` |

Click **Save Step** ✓

---

### Step 3 of 5 — Rent Branch

| Field | What to type |
|-------|-------------|
| Step name | `rent` |
| Text shown to user | `What is your monthly budget for rent?` |
| Button 1 label | `Under ₹20,000` |
| Button 1 goes to | `end` |
| Button 2 label | `₹20,000 – ₹50,000` |
| Button 2 goes to | `end` |
| Button 3 label | `Above ₹50,000` |
| Button 3 goes to | `call` |

Click **Save Step** ✓

---

### Step 4 of 5 — Apartment Branch

| Field | What to type |
|-------|-------------|
| Step name | `apartment` |
| Text shown to user | `Great choice. Would you like to speak to an agent or get a callback?` |
| Button 1 label | `Speak to agent now` |
| Button 1 goes to | `call` |
| Button 2 label | `I will browse more` |
| Button 2 goes to | `end` |

Click **Save Step** ✓

---

### Step 5 of 5 — Villa Branch

| Field | What to type |
|-------|-------------|
| Step name | `villa` |
| Text shown to user | `Villas are available in premium locations. Shall we have someone call you?` |
| Button 1 label | `Yes, call me` |
| Button 1 goes to | `call` |
| Button 2 label | `Not right now` |
| Button 2 goes to | `end` |

Click **Save Step** ✓

---

### Run It

Once all 5 steps are saved, click **▶ Run Chatbot**

Your flow now looks like this:

```
start
├── Buy → buy
│         ├── Apartment → apartment
│         │               ├── Speak to agent → CALLBACK
│         │               └── Browse more   → END
│         └── Villa     → villa
│                         ├── Yes call me   → CALLBACK
│                         └── Not now       → END
└── Rent → rent
           ├── Under 20k       → END
           ├── 20k to 50k      → END
           └── Above 50k       → CALLBACK
```

---

### What the Session Log Looks Like

When a user completes the flow, you see this output:

```json
{
  "session_id": "a3f2c1d4-7b3e-4f1a-9c2d-e5f6a7b8c9d0",
  "flow_version": "v1",
  "source": "website",
  "path": ["start", "buy", "apartment"],
  "started_at": "2025-03-14T10:23:11",
  "ended_at": "2025-03-14T10:24:45",
  "duration_seconds": 94,
  "outcome": "callback_requested"
}
```

This tells you:
- Exactly which path the user took — `start → buy → apartment`
- How long it took — 94 seconds
- What the outcome was — callback requested
- Which version of the flow ran — useful when you update flows over time

---

---

## Deploy Your Own — Free, No Code Required

Any small business or website owner can deploy their own version in 5 minutes for free using Streamlit Cloud.

**Step 1 — Fork this repo**
- Click **Fork** at the top right of this GitHub page
- This creates your own copy of the project

**Step 2 — Go to Streamlit Cloud**
- Visit [share.streamlit.io](https://share.streamlit.io)
- Sign in with your GitHub account

**Step 3 — Deploy**
- Click **New app**
- Select your forked repo
- Set main file path to: `app/app.py`
- Click **Deploy**

Streamlit gives you a free public URL in under 2 minutes.
Share it with your team, embed it in your website, or use it as a standalone tool.

**No server. No monthly cost. No technical knowledge required.**

---

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
