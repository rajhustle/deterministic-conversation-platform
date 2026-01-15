
import requests
def respond(script, user_input):
    prompt = f"""You are a professional chat support agent.
Follow this script strictly and do not invent prices or locations.

SCRIPT:
{script}

USER:
{user_input}
"""
    r = requests.post("http://localhost:11434/api/generate",
        json={"model":"llama3","prompt":prompt,"stream":False}, timeout=60)
    return r.json().get("response","")
