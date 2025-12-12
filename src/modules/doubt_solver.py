import pandas as pd
from modules.preprocessing import preprocess_questions
from modules.vectorizer import create_vectorizer
from modules.similarity import get_best_match

class DoubtSolver:
    def __init__(self, dataset_path):
        df = pd.read_csv(dataset_path)
        df = preprocess_questions(df)

        self.questions = df["cleaned_question"]
        self.answers = df["answer"]

        self.vectorizer, self.vectors = create_vectorizer(self.questions)

    def ask(self, question):
        idx, score = get_best_match(self.vectorizer, self.vectors, question)
        return self.answers[idx], 
    def safe_ask(self, question):
    try:
        if not question or question.strip() == "":
            return "Please enter a valid question.", 0.0

        answer, score = self.ask(question)

        if score < 0.20:
            return "I couldn't find a close enough match. Please rephrase your question.", score

        return answer, score

    except Exception as e:
        return f"An error occurred: {str(e)}", 0.0