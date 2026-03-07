import random


# -----------------------
# Unrealistic excuses
# -----------------------

def generate_unrealistic_excuse():

    events = [
        "aliens abducted my laptop",
        "my dog ate my assignment",
        "a ghost deleted my project file",
        "my computer developed emotions and refused to work",
        "my brain decided to go on vacation",
        "my heart said no to studying",
        "my stomach started protesting the exam"
    ]

    return "Unfortunately, " + random.choice(events) + "."


# -----------------------
# Technical excuses
# -----------------------

def generate_technical_excuse(user_input):

    devices = ["laptop","computer","system","pc","desktop","lab computer"]

    actions = [
        "uploading my assignment",
        "submitting the project",
        "saving my files",
        "uploading the final report"
    ]

    problems = [
        "crashed",
        "froze",
        "restarted",
        "stopped responding",
        "shut down unexpectedly",
        "displayed a system error",
        "became unresponsive",
        "encountered a fatal error",
        "failed during processing"
    ]

    templates = [

        "My {device} suddenly {problem} while I was {action}.",

        "While I was {action}, my {device} unexpectedly {problem}.",

        "During {action}, my {device} unfortunately {problem}.",

        "While dealing with {context}, my {device} suddenly {problem}.",

        "Right at the moment of {action}, my {device} suddenly {problem}."
    ]

    template = random.choice(templates)

    return template.format(
        device=random.choice(devices),
        problem=random.choice(problems),
        action=random.choice(actions),
        context=user_input
    )


# -----------------------
# Environment excuse
# -----------------------

def generate_environment_excuse(user_input):

    templates = [

        f"Due to {user_input}, the electricity supply was disrupted and I couldn't complete the assignment.",

        f"Because of {user_input}, my internet connection stopped working during submission.",

        f"The disturbance caused by {user_input} prevented me from finishing the assignment on time.",

        f"{user_input.capitalize()} created an unexpected disruption that affected my ability to submit the assignment."
    ]

    return random.choice(templates)


# -----------------------
# Family excuse
# -----------------------

def generate_family_excuse():

    events = [
        "A close family member had a medical emergency",
        "My grandmother passed away suddenly",
        "A relative was hospitalized",
        "There was an urgent family situation"
    ]

    return random.choice(events) + " so I couldn't complete the submission on time."


# -----------------------
# Health excuse
# -----------------------

def generate_health_excuse():

    events = [
        "I had severe food poisoning",
        "I developed a high fever",
        "I had a terrible migraine",
        "I had severe stomach pain"
    ]

    return random.choice(events) + " which prevented me from finishing the assignment."


# -----------------------
# Transport excuse
# -----------------------

def generate_transport_excuse():

    events = [
        "My bus broke down on the way to university",
        "There was heavy traffic due to an accident",
        "My ride got cancelled unexpectedly",
        "My car broke down"
    ]

    return random.choice(events) + " so I reached the university late."


# -----------------------
# Submission excuse
# -----------------------

def generate_submission_excuse():

    events = [
        "I accidentally uploaded the wrong version of the assignment",
        "I submitted the assignment to the wrong course portal",
        "I uploaded a draft instead of the final version",
        "I forgot to press the final submit button",
        "I attached the wrong document file"
    ]

    return random.choice(events) + "."


# -----------------------
# Group project excuse
# -----------------------

def generate_group_project_excuse():

    events = [
        "My teammate uploaded the wrong project file",
        "Our group member forgot to submit the final report",
        "Our shared project document was accidentally deleted",
        "Our group misunderstood the submission deadline"
    ]

    return random.choice(events) + "."


# -----------------------
# Lab excuse
# -----------------------

def generate_lab_excuse():

    events = [
        "The lab computer crashed during my experiment",
        "The laboratory software stopped responding",
        "The experiment equipment malfunctioned",
        "The lab network stopped working"
    ]

    return random.choice(events) + "."


# -----------------------
# Library excuse
# -----------------------

def generate_library_excuse():

    events = [
        "The library computers were not working",
        "The library closed earlier than expected",
        "The library wifi stopped working",
        "All library computers were occupied"
    ]

    return random.choice(events) + "."


# -----------------------
# Academic excuse
# -----------------------

def generate_academic_excuse():

    events = [
        "I misunderstood the assignment instructions",
        "I misread the assignment deadline",
        "I confused the exam schedule",
        "I misunderstood the project requirements"
    ]

    return random.choice(events) + "."


# -----------------------
# Personal excuse
# -----------------------

def generate_personal_excuse():

    events = [
        "My glasses broke and I couldn't see the screen properly",
        "My alarm did not ring in the morning",
        "My phone battery died overnight",
        "I lost my phone and missed the submission notification"
    ]

    return random.choice(events) + "."


# -----------------------
# Main Excuse Generator
# -----------------------

def generate_excuses(category, user_input, n=5, mode="Balanced"):

    # normalize categories
    category_map = {

        "internet_issue":"technical",
        "file_issue":"technical",
        "printer_issue":"technical",
        "account_issue":"technical",

        "power_outage":"environment",
        "weather_issue":"environment",
        "environment_issue":"environment",

        "exam_issue":"academic",
        "deadline_confusion":"academic",
        "schedule_conflict":"academic",

        "hostel_issue":"personal",
        "mental_health":"personal",
        "personal_issue":"personal"
    }

    category = category_map.get(category, category)

    excuses = []

    if mode == "Serious":
        unrealistic_prob = 0.05
    elif mode == "Balanced":
        unrealistic_prob = 0.20
    else:
        unrealistic_prob = 0.40

    while len(excuses) < n:

        if random.random() < unrealistic_prob:
            excuses.append(generate_unrealistic_excuse())
            continue

        if category == "technical":
            excuses.append(generate_technical_excuse(user_input))

        elif category == "environment":
            excuses.append(generate_environment_excuse(user_input))

        elif category == "family":
            excuses.append(generate_family_excuse())

        elif category == "health":
            excuses.append(generate_health_excuse())

        elif category == "transport":
            excuses.append(generate_transport_excuse())

        elif category == "submission":
            excuses.append(generate_submission_excuse())

        elif category == "group_project":
            excuses.append(generate_group_project_excuse())

        elif category == "lab_issue":
            excuses.append(generate_lab_excuse())

        elif category == "library_issue":
            excuses.append(generate_library_excuse())

        elif category == "academic":
            excuses.append(generate_academic_excuse())

        elif category == "personal":
            excuses.append(generate_personal_excuse())

        else:
            excuses.append(generate_technical_excuse(user_input))

    return excuses