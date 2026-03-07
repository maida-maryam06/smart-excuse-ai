import pickle

data = pickle.load(open("models/realism_model.pkl", "rb"))

model = data["model"]
vectorizer = data["vectorizer"]

def realism_score(excuse):

    vec = vectorizer.transform([excuse])

    prob = model.predict_proba(vec)[0][1]

    return round(prob * 100,2)