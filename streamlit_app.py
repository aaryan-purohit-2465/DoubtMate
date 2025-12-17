import streamlit as st
import importlib

# ---- FORCE RELOAD TO AVOID CACHING / STALE CODE ----
import src.doubt_solver as doubt_solver
importlib.reload(doubt_solver)
from src.doubt_solver import DoubtSolver

# ---- STREAMLIT PAGE CONFIG ----
st.set_page_config(
    page_title="DoubtMate",
    page_icon="🤖",
    layout="centered"
)

# ---- LOAD MODEL (NO CACHING TO AVOID ERRORS) ----
def load_solver():
    return DoubtSolver(dataset_path="data/faq_cleaned.csv")

solver = load_solver()

# ---- UI ----
st.title("🤖 DoubtMate")
st.write("Ask your doubt and get an instant answer")

user_question = st.text_input(
    "Enter your doubt",
    placeholder="What is a variable?"
)

# ---- BUTTON ACTION ----
if st.button("Get Answer"):
    if user_question.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        # ---- SAFE CALL (DEFENSIVE PROGRAMMING) ----
        result = solver.safe_ask(user_question)

        # ---- HANDLE ALL POSSIBLE RETURNS SAFELY ----
        if isinstance(result, tuple) and len(result) == 3:
            answer, score, top_matches = result
        else:
            answer = str(result)
            score = 0.0
            top_matches = []

        # ---- DISPLAY ANSWER ----
        st.subheader("Answer")
        st.success(answer)

        st.write(f"**Similarity Score:** {score:.3f}")

        # ---- OPTIONAL: SHOW TOP MATCHES ----
        if top_matches:
            st.subheader("Related Questions")
            for idx, sim, q, a in top_matches:
                with st.expander(f"{q} (score: {sim:.3f})"):
                    st.write(a)
