import streamlit as st
import pandas as pd
import time
import random

from modules.excuse_improver import improve_excuse
from modules.explanation_engine import explain_excuse
from modules.confidence_analyzer import analyze_confidence
from modules.rewrite_engine import rewrite_excuse
from modules.auto_retrain import retrain_if_needed
from modules.feedback import save_feedback
from modules.classifier import classify_situation
from modules.excuse_generator import generate_excuses
from modules.realism_detector import realism_score

if "history" not in st.session_state:
    st.session_state.history = []

retrain_if_needed()

# Page configuration
st.set_page_config(
    page_title="Smart Excuse AI",
    page_icon="💀",
    layout="wide"
)


# Styling
st.markdown("""
<style>
.stButton>button {
background-color:#ff4b4b;
color:white;
border-radius:8px;
height:40px;
font-weight:bold;
}

.stProgress > div > div {
background-color:#ff4b4b;
}
</style>
""", unsafe_allow_html=True)


# Category icons
icons = {
"technical":"💻",
"family":"👪",
"health":"🤒",
"transport":"🚌",
"submission":"📄",
"internet_issue":"🌐",
"file_issue":"📂",
"lab_issue":"🧪",
"group_project":"👥",
"power_outage":"⚡",
"weather_issue":"🌧",
"environment_issue":"🏠",
"library_issue":"📚",
"printer_issue":"🖨",
"hostel_issue":"🏫",
"personal_issue":"🙂",
"schedule_conflict":"📅"
}


# Title
st.title("💀 Smart Excuse AI")

st.markdown("""
Generate believable academic excuses using AI.
Type your situation and let the AI generate a convincing excuse.
""")


# Sidebar controls
mode = st.sidebar.selectbox(
    "Excuse Mode",
    ["Serious","Balanced","Chaotic"]
)

strictness = st.sidebar.slider(
    "Professor Strictness",
    0,10,5
)

st.sidebar.title("📊 AI Stats")
st.sidebar.write("Dataset Size: ~900+ excuses")
st.sidebar.write("Realism Model: Logistic Regression")
st.sidebar.write("Accuracy: ~92%")
st.sidebar.write("Vectorizer: TF-IDF")


# User input
user_input = st.text_input("Enter your situation")


# Buttons
col1, col2 = st.columns(2)

with col1:
    generate_btn = st.button("Generate Excuse")

with col2:
    random_btn = st.button("🎲 Random Excuse")


# ---------------- RANDOM EXCUSE ---------------- #

if random_btn:

    with st.spinner("🤖 Generating random excuse..."):
        time.sleep(1.2)

        category = "technical"

        excuses = generate_excuses(category, "random situation", n=10, mode=mode)

    results = []

    for excuse in excuses:
        score = realism_score(excuse)
        results.append((excuse,score))

    results = list({x[0]:x for x in results}.values())

    results.sort(key=lambda x: x[1], reverse=True)

    best_excuse, best_score = results[0]

    st.success(best_excuse)

    st.metric("Realism Score",f"{best_score}%")

    st.progress(best_score/100)


# ---------------- USER INPUT EXCUSE ---------------- #

if generate_btn and user_input != "":

    with st.spinner("🤖 Analyzing your situation..."):
        time.sleep(1.2)

        category, confidence = classify_situation(user_input)
        improved_input = improve_excuse(user_input)
        excuses = generate_excuses(category, user_input, n=10, mode=mode)

    results = []

    for excuse in excuses:
        if random.random() < 0.7:
            rewritten = rewrite_excuse(excuse, mode)
        else:
            rewritten = excuse

        score = realism_score(rewritten)
        results.append((rewritten,score))

    results = list({x[0]:x for x in results}.values())

    results.sort(key=lambda x: x[1], reverse=True)


    # ---------- STRICTNESS + MODE LOGIC ---------- #

    if strictness <= 4:

        if mode == "Chaotic":

            low_scores = sorted(results,key=lambda x:x[1])
            best_excuse, best_score = random.choice(low_scores[:3])

        elif mode == "Balanced":

            mid = results[2:6]
            best_excuse, best_score = random.choice(mid)

        else:  # Serious
            best_excuse, best_score = results[0]
            st.session_state.history.append((best_excuse, best_score))

    else:

        threshold = 70 + (strictness * 3)

        best_excuse = None
        best_score = 0

        for excuse,score in results:
            if score >= threshold:
                best_excuse = excuse
                best_score = score
                break

        if best_excuse is None:
            best_excuse, best_score = results[0]


    # Display results
    st.write(f"Situation Category: {icons.get(category,'❓')} {category}")

    st.success("Best Excuse")

    st.code(best_excuse)

    st.download_button(
        label="📋 Copy Excuse",
        data=best_excuse,
        file_name="excuse.txt",
        mime="text/plain"
    )

    st.write("Professor Strictness Level:", strictness)

    st.metric("AI Believability Score",f"{best_score}%")
    if best_score >= 85:
        difficulty = "🟢 EASY"
    elif best_score >= 65:
        difficulty = "🟡 MEDIUM"
    else:
        difficulty = "🔴 RISKY"

    st.write("Excuse Difficulty:", difficulty)

    reasons = explain_excuse(best_excuse, best_score)

    st.subheader("🤖 AI Explanation")

    for r in reasons:
        st.write("•", r)
    
    risk, strength = analyze_confidence(best_score)

    col1, col2 = st.columns(2)
    col1.metric("Suspicion Risk", risk)
    col2.metric("Excuse Strength", strength)

    st.progress(best_score/100)


    # ---------------- FEEDBACK SYSTEM ---------------- #

    st.subheader("Was this excuse believable?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Believable"):
            save_feedback(best_excuse, 1)
            st.success("Thanks! Feedback saved.")

    with col2:
        if st.button("👎 Unrealistic"):
            save_feedback(best_excuse, 0)
            st.warning("Feedback recorded.")


    # Leaderboard
    st.subheader("🏆 Excuse Ranking")

    df = pd.DataFrame(results,columns=["Excuse","Score"])

    df["Score"] = df["Score"].apply(lambda x: f"{x}%")

    st.table(df)