def calculate_score(intent, msg_count):
    score = 20 + msg_count * 10

    if intent in ["pricing_inquiry", "demo_request"]:
        score += 30
    if intent == "not_interested":
        score -= 40

    score = max(0, min(score, 100))
    status = "hot" if score > 70 else "warm" if score > 40 else "cold"
    return score, status