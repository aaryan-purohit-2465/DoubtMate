import pandas as pd
from src.config import DATASET_PATH, MIN_SIMILARITY_THRESHOLD
from src.logger import log_query

from src.modules.preprocessing import preprocess_questions, clean_text
from src.modules.vectorizer import create_vectorizer
from src.modules.similarity import get_top_matches


class DoubtSolver:
    def __init__(self, dataset_path=None):
        if dataset_path is None:
            dataset_path = DATASET_PATH

        # Load dataset
        df = pd.read_csv(dataset_path)

        # Basic validation
        if "question" not in df.columns or "answer" not in df.columns:
            raise ValueError("Dataset must contain 'question' and 'answer' columns")

        # Preprocess questions
        df = preprocess_questions(df)
        self.df = df.reset_index(drop=True)

        self.questions = self.df["cleaned_question"].astype(str).tolist()
        self.answers = self.df["answer"].astype(str).tolist()

        # Vectorize
        self.vectorizer, self.vectors = create_vectorizer(self.questions)

    def ask(self, question, top_n=3):
        cleaned_question = clean_text(question)

        idxs, scores = get_top_matches(
            self.vectorizer, self.vectors, cleaned_question, top_n
        )

        top_matches = []
        for i, s in zip(idxs, scores):
            top_matches.append(
                (
                    int(i),
                    float(s),
                    self.df.iloc[i]["question"],
                    self.df.iloc[i]["answer"],
                )
            )
