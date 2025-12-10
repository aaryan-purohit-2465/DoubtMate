import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class DoubtSolverBaseline:
    def __init__(self, faq_path: str):
        # Load dataset
        self.faq_df = pd.read_csv(faq_path)
        # Fill missing values
        self.faq_df["question"] = self.faq_df["question"].fillna("")
        self.faq_df["answer"] = self.faq_df["answer"].fillna("No answer available.")

        # Create TF-IDF vectorizer and fit on questions
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.question_vectors = self.vectorizer.fit_transform(self.faq_df["question"])

    def get_best_answer(self, user_question: str) -> tuple[str, str, float]:
        """
        Returns (matched_question, answer, similarity_score)
        """
        if not user_question.strip():
            return "", "Please enter a valid question.", 0.0

        # Transform user question
        user_vec = self.vectorizer.transform([user_question])

        # Compute cosine similarity
        similarities = cosine_similarity(user_vec, self.question_vectors)[0]

        # Get index of best match
        best_idx = similarities.argmax()
        best_score = float(similarities[best_idx])

        matched_question = self.faq_df.iloc[best_idx]["question"]
        matched_answer = self.faq_df.iloc[best_idx]["answer"]

        return matched_question, matched_answer, best_score


def main():
    faq_path = "data/faq.csv"
    solver = DoubtSolverBaseline(faq_path)

    print("===== Classroom Doubt Solver (Baseline) =====")
    print("Type 'exit' to quit.\n")

    while True:
        user_q = input("Enter your doubt: ")

        if user_q.lower().strip() in ["exit", "quit"]:
            print("Goodbye!")
            break

        matched_q, ans, score = solver.get_best_answer(user_q)

        print("\nMost similar stored question:")
        print(f"  {matched_q}")
        print(f"Similarity score: {score:.2f}")
        print("\nSuggested answer:")
        print(f"  {ans}")
        print("-" * 50)


if __name__ == "__main__":
    main()
