from fastapi import FastAPI
from openai import OpenAI

from intent import detect_intent
from memory import save_message
from scoring import calculate_score
from prompts import SYSTEM_PROMPT

app = FastAPI()
client = OpenAI() 


@app.post("/chat")
def chat(data: dict):
    lead_id = data["lead_id"]
    message = data["message"]

    history = save_message(lead_id, "user", message)

    intent, confidence = detect_intent(message)

    if intent == "demo_request":
        reply = "Sure, I can help schedule a demo. Please let me know a suitable time."
    elif intent == "pricing_inquiry":
        reply = "Our pricing depends on usage. I can share details or arrange a demo if you'd like."
    elif intent == "feature_inquiry":
        reply = "We offer automation, analytics, and integrations. Would you like a demo?"
    elif intent == "follow_up":
        reply = "Sure, I can arrange a follow-up call with our team."
    elif intent == "not_interested":
        reply = "No problem at all. Feel free to reach out anytime."
    else:
        reply = "Thanks for reaching out. How can I help you further?"

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": reply}
            ]
        )
        reply = completion.choices[0].message.content.strip()
    except Exception:
        pass  

    save_message(lead_id, "assistant", reply)

    score, status = calculate_score(intent, len(history))

    if intent == "demo_request":
        next_action = "schedule_demo"
    elif intent == "pricing_inquiry":
        next_action = "offer_demo"
    elif intent == "follow_up":
        next_action = "schedule_call"
    elif intent == "not_interested":
        next_action = "stop_follow_up"
    else:
        next_action = "continue_conversation"

    return {
        "reply": reply,
        "intent": intent,
        "confidence": confidence,
        "next_action": next_action,
        "lead_score": score,
        "lead_status": status
    }