# src/doubt_solver.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DoubtSolver:
    def __init__(self, dataset_path="data/faq_cleaned.csv"):
        self.df = pd.read_csv(dataset_path)
        # Ensure column name used: "question" and "answer"
        if "question" not in self.df.columns or "answer" not in self.df.columns:
            raise ValueError("Dataset must contain columns: 'question' and 'answer'")
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.vectors = self.vectorizer.fit_transform(self.df["question"].astype(str))

    def ask(self, question):
        question = str(question)
        qvec = self.vectorizer.transform([question])
        sims = cosine_similarity(qvec, self.vectors)[0]
        best_idx = int(sims.argmax())
        best_score = float(sims[best_idx])
        answer = str(self.df.iloc[best_idx]["answer"])
        return answer, best_score

    def safe_ask(self, question, top_n=3):
        # Always return exactly (answer, score, top_matches)
        if not question or str(question).strip() == "":
            return "Please enter a valid question.", 0.0, []

        try:
            answer, score = self.ask(question)

            sims = cosine_similarity(self.vectorizer.transform([question]), self.vectors)[0]
            top_idxs = sims.argsort()[-top_n:][::-1]

            top_matches = []
            seen = set()
            for idx in top_idxs:
                q = str(self.df.iloc[int(idx)]["question"])
                a = str(self.df.iloc[int(idx)]["answer"])
                s = float(sims[int(idx)])
                if q in seen:
                    continue
                seen.add(q)
                # keep only meaningful matches
                if s < 0.10:
                    continue
                top_matches.append((int(idx), s, q, a))

            if not top_matches:
                return "No relevant answer found. Try rephrasing.", 0.0, []

            return answer, score, top_matches

        except Exception as e:
            return f"Error: {str(e)}", 0.0, []
