import random


def rewrite_excuse(excuse, mode="Balanced"):

    excuse = excuse.lower()

    if excuse.endswith("."):
        excuse = excuse[:-1]

    # ---------------- SERIOUS MODE ---------------- #

    serious_templates = [

        "While attempting to complete the assignment submission, {excuse}.",

        "During the submission process, {excuse} which prevented me from finishing the task.",

        "Unfortunately, {excuse} which interrupted the submission process.",

        "At the time of uploading the assignment, {excuse} and the process could not continue.",

        "While preparing my assignment for submission, {excuse}."
    ]


    # ---------------- BALANCED MODE ---------------- #

    balanced_templates = [

        "While I was working on the assignment, {excuse}.",

        "Right when I was submitting the assignment, {excuse}.",

        "While trying to finish my assignment, {excuse}.",

        "Unfortunately, {excuse} during submission.",

        "{excuse} which stopped me from submitting the assignment."
    ]


    # ---------------- CHAOTIC MODE ---------------- #

    chaotic_templates = [

        "Apparently {excuse} because my laptop also hates deadlines.",

        "{excuse} as if the universe decided today was not my day.",

        "For some reason, {excuse} right when the deadline was approaching.",

        "{excuse} which honestly felt like a personal attack from technology.",

        "At the exact moment of submission, {excuse} like it had something against me."
    ]


    if mode == "Serious":
        template = random.choice(serious_templates)

    elif mode == "Chaotic":
        template = random.choice(chaotic_templates)

    else:
        template = random.choice(balanced_templates)

    rewritten = template.format(excuse=excuse)

    return rewritten.capitalize()