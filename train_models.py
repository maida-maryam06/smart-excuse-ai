import pandas as pd
import pickle
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# =========================
# Load dataset
# =========================

df = pd.read_csv("dataset/excuse_realism.csv")

print("Original dataset shape:", df.shape)

# =========================
# Remove missing values
# =========================

df.dropna(inplace=True)

# =========================
# Remove duplicates
# =========================

df.drop_duplicates(inplace=True)

print("Dataset after cleaning:", df.shape)

# =========================
# Keep only needed columns
# =========================

df = df[["text", "label"]]

# =========================
# Text preprocessing
# =========================

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


df["text"] = df["text"].apply(clean_text)

# =========================
# Dataset statistics
# =========================

print("\nLabel distribution:")
print(df["label"].value_counts())

# =========================
# Features and labels
# =========================

X = df["text"]
y = df["label"]

# =========================
# Train test split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# TF-IDF Vectorization
# =========================

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    max_features=5000
)

X_train_vec = vectorizer.fit_transform(X_train)

X_test_vec = vectorizer.transform(X_test)

# =========================
# Train Logistic Regression
# =========================

model = LogisticRegression(
    class_weight="balanced",
    max_iter=3000
)

model.fit(X_train_vec, y_train)

# =========================
# Evaluate model
# =========================

pred = model.predict(X_test_vec)

print("\nModel Accuracy:", accuracy_score(y_test, pred))

print("\nClassification Report:\n")

print(classification_report(y_test, pred))

# =========================
# Save model
# =========================

model_data = {
    "model": model,
    "vectorizer": vectorizer
}

with open("models/realism_model.pkl", "wb") as f:
    pickle.dump(model_data, f)

print("\nRealism model saved successfully!")