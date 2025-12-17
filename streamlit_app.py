import streamlit as st
from src.doubt_solver import DoubtSolver

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DoubtMate",
    page_icon="🎓",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0b1220;
    color: #e5e7eb;
}

/* Center container */
.block-container {
    max-width: 800px;
    padding-top: 50px;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 40px;
}

/* Input */
input {
    font-size: 18px !important;
    padding: 16px !important;
    border-radius: 12px !important;
}

/* Button */
.stButton button {
    width: 100%;
    padding: 14px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    background: linear-gradient(135deg, #2563eb, #22d3ee);
    color: black;
    border: none;
}

/* Answer box */
.answer-box {
    background-color: #ecfeff;
    color: #0f172a;
    border-radius: 14px;
    padding: 22px;
    margin-top: 30px;
    border-left: 6px solid #22c55e;
}

/* Answer text */
.answer-text {
    font-size: 19px;
    line-height: 1.7;
    margin-top: 8px;
}

/* Confidence */
.confidence {
    margin-top: 12px;
    font-size: 14px;
    font-weight: 600;
    color: #047857;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 70px;
    font-size: 13px;
    color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MODEL ----------------
solver = DoubtSolver(dataset_path="data/faq_cleaned.csv")

# ---------------- HEADER ----------------
st.markdown('<div class="title">🎓 DoubtMate</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Ask academic questions and get instant answers using Machine Learning</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT ----------------
question = st.text_input(
    "Enter your question",
    placeholder="What is deployment?"
)

# ---------------- ACTION ----------------
if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        answer, score, top_matches = solver.safe_ask(question)

        # Answer container (STREAMLIT SAFE)
        st.markdown(
            f"""
            <div class="answer-box">
                <strong>Answer</strong>
                <div class="answer-text">{answer}</div>
                <div class="confidence">Similarity confidence: {score:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if top_matches:
            st.markdown("### Related Questions")
            for _, sim, q, a in top_matches:
                with st.expander(f"{q} • {sim:.2f}"):
                    st.write(a)

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Built with Python, Machine Learning & Streamlit</div>',
    unsafe_allow_html=True
)