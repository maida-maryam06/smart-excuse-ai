import pandas as pd
import pickle
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# -----------------------------
# Load dataset
# -----------------------------

df = pd.read_csv("dataset/excuse_realism.csv")

print("Original dataset shape:", df.shape)


# -----------------------------
# Clean dataset
# -----------------------------

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# remove spaces like " family"
df["category"] = df["category"].str.strip()

# keep only required columns
df = df[["text","category"]]

print("Dataset after cleaning:", df.shape)

print("\nCategory distribution:")
print(df["category"].value_counts())


# -----------------------------
# Text preprocessing
# -----------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


df["text"] = df["text"].apply(clean_text)


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

df["category"] = df["category"].replace(category_map)

# -----------------------------
# Features and labels
# -----------------------------

X = df["text"]
y = df["category"]


# -----------------------------
# Train/Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    stratify=y,        # important for multi-class problems
    random_state=42
)


# -----------------------------
# TF-IDF Vectorization
# -----------------------------

vectorizer = TfidfVectorizer(

    stop_words="english",

    ngram_range=(1,2),      # capture phrases like "wifi stopped"

    max_features=6000,

    min_df=1,               # ignore very rare words

    max_df=0.9              # ignore overly common words
)


X_train_vec = vectorizer.fit_transform(X_train)

X_test_vec = vectorizer.transform(X_test)


# -----------------------------
# Train Model
# -----------------------------

model = LogisticRegression(

    max_iter=3000,

    class_weight="balanced"   # helps if some categories are smaller
)


model.fit(X_train_vec, y_train)


# -----------------------------
# Evaluate Model
# -----------------------------

pred = model.predict(X_test_vec)

print("\nModel Accuracy:", accuracy_score(y_test, pred))

print("\nClassification Report:\n")

print(classification_report(y_test, pred))


# -----------------------------
# Save Model
# -----------------------------

pickle.dump(

    {"model": model, "vectorizer": vectorizer},

    open("models/situation_model.pkl", "wb")

)

print("\nSituation model saved successfully!")