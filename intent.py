def detect_intent(message):
    msg = message.lower()

    if "price" in msg or "pricing" in msg or "cost" in msg:
        return "pricing_inquiry", 0.85
    if "demo" in msg or "trial" in msg:
        return "demo_request", 0.9
    if "feature" in msg or "support" in msg:
        return "feature_inquiry", 0.8
    if "call" in msg or "follow up" in msg:
        return "follow_up", 0.85
    if "not interested" in msg or "no thanks" in msg:
        return "not_interested", 0.95

    return "general", 0.6