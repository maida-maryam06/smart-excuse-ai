import random


def improve_excuse(user_input):

    templates = [

        "While attempting to complete my assignment submission, {context} which prevented the process from finishing successfully.",

        "During the process of submitting my assignment through the university portal, {context} which interrupted the submission.",

        "Unfortunately, {context} while I was trying to submit my assignment which caused the delay.",

        "While working on my assignment submission, {context} and I was unable to complete the process.",

        "At the moment I was submitting the assignment, {context} which disrupted the upload."
    ]

    template = random.choice(templates)

    context = user_input.lower()

    if context.endswith("."):
        context = context[:-1]

    improved = template.format(context=context)

    return improved.capitalize() + "."