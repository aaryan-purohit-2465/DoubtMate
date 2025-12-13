import streamlit as st
from src.doubt_solver import DoubtSolver

st.set_page_config(page_title="DoubtMate", page_icon="🤖")

st.title("🤖 DoubtMate")
st.write("Ask your doubt and get an instant answer")

# Load solver once
@st.cache_resource
def load_solver():
    return DoubtSolver()

solver = load_solver()

user_question = st.text_input("Enter your doubt")

if st.button("Get Answer"):
    answer, score, top_matches = solver.safe_ask(user_question)

    st.subheader("Answer")
    st.success(answer)

    st.write(f"**Similarity Score:** {score:.3f}")

    if top_matches:
        st.subheader("Similar Questions")
        for _, s, q, _ in top_matches:
            st.write(f"- {q} (score: {s:.3f})")
