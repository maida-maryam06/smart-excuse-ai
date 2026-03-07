import random


def explain_excuse(excuse, score):

    reasons = []

    excuse_lower = excuse.lower()

    # detect excuse type
    if any(word in excuse_lower for word in ["laptop","computer","system","wifi","network","internet"]):
        reasons.append("A specific technical issue was detected.")

    if any(word in excuse_lower for word in ["upload","submit","assignment","project","portal"]):
        reasons.append("The excuse references a realistic academic submission scenario.")

    if any(word in excuse_lower for word in ["crashed","failed","stopped","disconnected","error"]):
        reasons.append("The excuse describes a believable system failure.")

    if any(word in excuse_lower for word in ["hospital","sick","fever","family","emergency"]):
        reasons.append("The excuse involves a personal or family emergency.")

    if score >= 85:
        reasons.append("The wording appears natural and believable.")

    if score < 60:
        reasons.append("The excuse may sound unusual or exaggerated.")

    # fallback
    if len(reasons) == 0:
        reasons.append("The excuse contains a clear explanation for the delay.")

    # limit to 3 reasons
    reasons = reasons[:3]

    return reasons