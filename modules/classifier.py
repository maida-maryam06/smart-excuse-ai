import pickle
import re


# Load trained model
data = pickle.load(open("models/situation_model.pkl","rb"))

model = data["model"]
vectorizer = data["vectorizer"]


# Improved keyword dictionary
keyword_rules = {

"technical":[
"laptop","computer","pc","system","crash","freeze","bug","error",
"software","update","restart","keyboard","screen","battery"
],

"internet_issue":[
"internet","wifi","network","router","connection","online",
"signal","bandwidth","disconnect","lag","latency"
],

"file_issue":[
"file","document","usb","drive","deleted","corrupted",
"lost file","missing file","wrong file","overwrite"
],

"health":[
"sick","fever","migraine","pain","hospital","ill","vomit",
"food poisoning","infection","allergy","injury"
],

"family":[
"family","funeral","grandmother","grandfather","relative",
"emergency","hospitalized","death","passed away"
],

"transport":[
"bus","traffic","car","ride","road","transport","bike",
"puncture","accident","vehicle","train"
],

"environment_issue":[
"construction","noise","electricity","power","flood",
"rain","storm","blackout","generator","transformer"
],

"lab_issue":[
"lab","experiment","equipment","practical","laboratory",
"microscope","circuit","apparatus"
],

"group_project":[
"group","teammate","team","partner","project",
"collaboration","shared file","team member"
],

"submission":[
"submit","submission","upload","portal","deadline",
"assignment portal","lms","course portal"
]

}


def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text


def keyword_classifier(text):

    for category,words in keyword_rules.items():

        for word in words:

            if word in text:

                return category

    return None


def classify_situation(user_input):

    text = clean_text(user_input)

    # Step 1: keyword detection
    keyword_result = keyword_classifier(text)

    if keyword_result is not None:

        return keyword_result, 1.0   # keyword rules = high confidence


    # Step 2: fallback to ML model
    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)[0]

    proba = model.predict_proba(text_vec)[0]

    confidence = max(proba)


    # Step 3: fallback protection
    if confidence < 0.45:
        prediction = "technical"

    return prediction, confidence