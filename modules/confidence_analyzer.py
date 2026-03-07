def analyze_confidence(score):

    # Professor suspicion risk
    if score >= 85:
        risk = "LOW"
    elif score >= 65:
        risk = "MEDIUM"
    else:
        risk = "HIGH"


    # Excuse strength
    if score >= 90:
        strength = "VERY STRONG"
    elif score >= 75:
        strength = "STRONG"
    elif score >= 60:
        strength = "AVERAGE"
    else:
        strength = "WEAK"


    return risk, strength