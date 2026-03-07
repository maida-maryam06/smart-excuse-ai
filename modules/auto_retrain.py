import pandas as pd
import pickle
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

FEEDBACK_FILE = "dataset/user_feedback.csv"
DATASET_FILE = "dataset/excuse_realism.csv"
MODEL_FILE = "models/realism_model.pkl"


def retrain_if_needed():

    if not os.path.exists(FEEDBACK_FILE):
        return

    # handle empty file safely
    try:
        feedback_df = pd.read_csv(FEEDBACK_FILE)
    except pd.errors.EmptyDataError:
        return

    # retrain only if enough feedback
    if len(feedback_df) < 500:
        return

    print("Retraining realism model using user feedback...")

    original_df = pd.read_csv(DATASET_FILE)

    original_df = original_df[["text","label"]]

    feedback_df.rename(columns={"excuse":"text"}, inplace=True)

    df = pd.concat([original_df, feedback_df], ignore_index=True)

    X = df["text"]
    y = df["label"]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,2),
        max_features=6000
    )

    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=3000)

    model.fit(X_vec, y)

    pickle.dump(
        {"model":model,"vectorizer":vectorizer},
        open(MODEL_FILE,"wb")
    )

    print("Model retrained successfully.")