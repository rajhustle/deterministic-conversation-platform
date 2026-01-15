import streamlit as st
import uuid
from datetime import datetime

st.set_page_config(page_title="Deterministic Conversation Platform", layout="centered")

# =========================
# SESSION INITIALIZATION
# =========================
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "flow" not in st.session_state:
    st.session_state.flow = {}

if "current" not in st.session_state:
    st.session_state.current = None

if "path" not in st.session_state:
    st.session_state.path = []

if "started_at" not in st.session_state:
    st.session_state.started_at = datetime.now()

if "flow_version" not in st.session_state:
    st.session_state.flow_version = "v1"

if "source" not in st.session_state:
    st.session_state.source = "website"


# =========================
# FLOW VALIDATION
# =========================
def validate_flow(flow):
    errors = []

    if "start" not in flow:
        errors.append("Missing 'start' step")

    for step, data in flow.items():
        for btn in data["buttons"]:
            nxt = btn["next"].strip()
            if nxt not in flow and nxt not in ["end", "call"]:
                errors.append(
                    f"Button '{btn['label']}' in step '{step}' points to invalid step '{nxt}'"
                )
    return errors


# =========================
# MODE SELECT
# =========================
mode = st.radio("Mode", ["Build", "Run"], horizontal=True)


# =========================
# BUILD MODE
# =========================
if mode == "Build":
    st.header("Build Conversation Flow")

    step_name = st.text_input("Step name (use 'start' for first step)").strip()
    step_text = st.text_area("Text shown to user")

    st.subheader("Buttons")
    buttons = []

    for i in range(1, 4):
        col1, col2 = st.columns(2)
        with col1:
            label = st.text_input(f"Button {i} label", key=f"lbl_{i}")
        with col2:
            nxt = st.text_input(
                f"Button {i} goes to (step name / end / call)", key=f"nxt_{i}"
            )

        if label.strip() and nxt.strip():
            buttons.append({
                "label": label.strip(),
                "next": nxt.strip()
            })

    if st.button("Save Step"):
        if not step_name or not step_text or not buttons:
            st.error("Step name, text, and at least 1 complete button required")
        else:
            st.session_state.flow[step_name] = {
                "text": step_text,
                "buttons": buttons
            }
            st.success(f"Saved step '{step_name}'")

    st.subheader("Current Flow")
    for k, v in st.session_state.flow.items():
        st.markdown(f"**{k}**: {v['text']}")
        for b in v["buttons"]:
            st.markdown(f"- {b['label']} → {b['next']}")

    if st.button("▶ Run Chatbot"):
        errors = validate_flow(st.session_state.flow)
        if errors:
            for e in errors:
                st.error(e)
        else:
            st.session_state.current = "start"
            st.session_state.path = []
            st.session_state.started_at = datetime.now()
            st.rerun()


# =========================
# RUN MODE
# =========================
if mode == "Run":

    if not st.session_state.current:
        st.info("Go to BUILD mode and create a flow first.")
        st.stop()

    # ---------- END ----------
    if st.session_state.current == "end":
        ended_at = datetime.now()
        duration = (ended_at - st.session_state.started_at).total_seconds()

        log = {
            "session_id": st.session_state.session_id,
            "flow_version": st.session_state.flow_version,
            "source": st.session_state.source,
            "path": st.session_state.path,
            "started_at": st.session_state.started_at.isoformat(),
            "ended_at": ended_at.isoformat(),
            "duration_seconds": duration,
            "outcome": "completed"
        }

        st.write("SESSION LOG:", log)
        st.success("Thank you.")
        st.stop()

    # ---------- CALLBACK ----------
    if st.session_state.current == "call":
        ended_at = datetime.now()
        duration = (ended_at - st.session_state.started_at).total_seconds()

        log = {
            "session_id": st.session_state.session_id,
            "flow_version": st.session_state.flow_version,
            "source": st.session_state.source,
            "path": st.session_state.path,
            "started_at": st.session_state.started_at.isoformat(),
            "ended_at": ended_at.isoformat(),
            "duration_seconds": duration,
            "outcome": "callback_requested"
        }

        st.write("SESSION LOG:", log)
        st.success("A human will contact you shortly.")
        st.stop()

    # ---------- NORMAL STEP ----------
    node = st.session_state.current

    if node not in st.session_state.path:
        st.session_state.path.append(node)

    data = st.session_state.flow[node]

    st.markdown(
        f"<div style='background:#f4f4f6;padding:16px;border-radius:8px;'>"
        f"{data['text']}</div>",
        unsafe_allow_html=True
    )

    st.write("")

    for b in data["buttons"]:
        if st.button(
            b["label"],
            key=f"{node}_{b['label']}",
            use_container_width=True
        ):
            st.session_state.current = b["next"]
            st.rerun()

    st.text_input("Type here (fallback only)")
