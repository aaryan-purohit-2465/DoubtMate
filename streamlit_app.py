import streamlit as st
import importlib
from src import doubt_solver

# Force reload to avoid cache issues
importlib.reload(doubt_solver)
from src.doubt_solver import DoubtSolver

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DoubtMate",
    page_icon="🧠",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

body {
    background: radial-gradient(circle at top, #0f2027, #020617);
    color: #e5e7eb;
}

/* Header */
.header-box {
    background: linear-gradient(135deg, #6366f1, #22d3ee);
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 35px;
}

.header-box h1 {
    color: #020617;
    font-weight: 700;
    margin-bottom: 6px;
}

.header-box p {
    color: #020617;
    font-size: 16px;
}

/* Bigger input box */
textarea, input {
    font-size: 18px !important;
    padding: 14px !important;
    border-radius: 14px !important;
}

/* Button */
.stButton button {
    width: 100%;
    border-radius: 14px;
    padding: 14px;
    font-size: 16px;
    font-weight: 600;
    background: linear-gradient(135deg, #22d3ee, #6366f1);
    color: #020617;
    border: none;
}

/* Answer container (GREENISH & SMALLER) */
.answer-card {
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.35);
    border-radius: 14px;
    padding: 16px 18px;
    margin-top: 22px;
}

/* Answer text bigger */
.answer-text {
    font-size: 18px;
    line-height: 1.6;
}

/* Score badge */
.score-badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(34,197,94,0.2);
    color: #22c55e;
    font-size: 14px;
    margin-top: 10px;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 60px;
    opacity: 0.5;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
def load_solver():
    return DoubtSolver(dataset_path="data/faq_cleaned.csv")

solver = load_solver()

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-box">
    <h1>🧠 DoubtMate</h1>
    <p>Real-Time Classroom Doubt Solver powered by ML</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT ----------------
question = st.text_input(
    "💬 Ask your doubt",
    placeholder="e.g. What is GitHub?"
)

# ---------------- ACTION ----------------
if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        answer, score, top_matches = solver.safe_ask(question)

        # ---------------- ANSWER ----------------
        st.markdown("""
        <div class="answer-card">
            <h3>📘 Answer</h3>
            <div class="answer-text">
        """, unsafe_allow_html=True)

        st.write(answer)

        st.markdown(f"""
            </div>
            <div class="score-badge">
                Similarity Score: {score:.3f}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ---------------- RELATED QUESTIONS ----------------
        if top_matches:
            st.markdown("### 🔗 Related Questions")
            for idx, sim, q, a in top_matches:
                with st.expander(f"{q} • score {sim:.2f}"):
                    st.write(a)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Built with ❤️ using Python, TF-IDF & Streamlit
</div>
""", unsafe_allow_html=True)
