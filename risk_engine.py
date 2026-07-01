def calculate_risk(detections):
    score = 0

    for detection in detections:
        category = detection[0]

        if category == "Prompt Injection":
            score += 40

        elif category == "Jailbreak":
            score += 35

        elif category == "Sensitive Data Request":
            score += 25

    score = min(score, 100)

    if score >= 80:
        level = "CRITICAL"

    elif score >= 60:
        level = "HIGH"

    elif score >= 30:
        level = "MEDIUM"

    else:
        level = "LOW"

    return score, level
