# src/doubt_solver.py
# src/doubt_solver.py (imports - top of file)
from pathlib import Path
import pandas as pd

# Use package-relative imports
from src.config import DATASET_PATH, MIN_SIMILARITY_THRESHOLD
from src.logger import log_query

from src.modules.preprocessing import preprocess_questions, clean_text
from src.modules.vectorizer import create_vectorizer
from src.modules.similarity import get_top_matches

from pathlib import Path
import pandas as pd

# Import project config and logger
try:
    # If your config and logger are in src/ (recommended), use:
    from config import DATASET_PATH, MIN_SIMILARITY_THRESHOLD
    from logger import log_query
except ImportError:
    # Fallback if executed from project root or different import paths
    from src.config import DATASET_PATH, MIN_SIMILARITY_THRESHOLD
    from src.logger import log_query

# Import modules you created on Day 2
try:
    from modules.preprocessing import preprocess_questions, clean_text
    from modules.vectorizer import create_vectorizer
    from modules.similarity import get_top_matches
except ImportError:
    # Fallback if running as script from src/
    from src.modules.preprocessing import preprocess_questions, clean_text
    from src.modules.vectorizer import create_vectorizer
    from src.modules.similarity import get_top_matches


class DoubtSolver:
    def __init__(self, dataset_path: str | None = None):
        # Use config path if no dataset_path provided
        if dataset_path is None:
            dataset_path = DATASET_PATH

        # Resolve relative paths robustly
        dataset_path = str(Path(dataset_path))

        # Load dataset
        df = pd.read_csv(dataset_path)
        # Ensure expected columns exist
        if "question" not in df.columns or "answer" not in df.columns:
            raise ValueError("Dataset must contain 'question' and 'answer' columns.")

        # Preprocess and vectorize
        df = preprocess_questions(df)  # adds cleaned_question column
        self.df = df.reset_index(drop=True)

        self.questions = self.df["cleaned_question"].astype(str).tolist()
        self.answers = self.df["answer"].astype(str).tolist()

        self.vectorizer, self.vectors = create_vectorizer(self.questions)

    def ask(self, user_question: str, top_n: int = 3):
        """
        Returns:
          best_answer (str),
          best_score (float),
          top_matches (list of tuples (idx, score, original_question, answer))
        """
        if not user_question or not user_question.strip():
            return "Please enter a valid question.", 0.0, []

        # Clean user question similarly to training data
        cleaned = clean_text(user_question)

        # Get top matches (indexes and scores)
        idxs, scores = get_top_matches(self.vectorizer, self.vectors, cleaned, top_n=top_n)

        # Prepare top_matches list
        top_matches = []
        for i, s in zip(idxs, scores):
            orig_q = self.df.iloc[i]["question"]
            ans = self.df.iloc[i]["answer"]
            top_matches.append((int(i), float(s), str(orig_q), str(ans)))

        # Best match is first in the returned list
        best_idx, best_score, best_orig_q, best_ans = top_matches[0]

        # Log the query (question, returned answer, score)
        try:
            log_query(user_question, best_ans, best_score)
        except Exception:
            # Logging must not break functionality
            pass

        return best_ans, float(best_score), top_matches

    def safe_ask(self, user_question: str, top_n: int = 3):
        """
        Wrapper that returns a friendly message if similarity is too low
        or if input is invalid. Uses MIN_SIMILARITY_THRESHOLD from config.
        """
        try:
            if not user_question or user_question.strip() == "":
                return "Please enter a valid question.", 0.0, []

            answer, score, top_matches = self.ask(user_question, top_n=top_n)

            if score < MIN_SIMILARITY_THRESHOLD:
                # Low confidence
                return (
                    "I couldn't find a close enough match. Please rephrase your question.",
                    float(score),
                    top_matches,
                )

            return answer, float(score), top_matches
        except Exception as e:
            return f"An error occurred: {str(e)}", 0.0, []


# Quick CLI tester (helpful for local testing)
if __name__ == "__main__":
    import sys

    ds_path = None
    if len(sys.argv) > 1:
        ds_path = sys.argv[1]

    solver = DoubtSolver(dataset_path=ds_path)

    print("DoubtMate - test shell (type 'exit' to quit)")
    while True:
        q = input("\nEnter your doubt> ").strip()
        if q.lower() in ("exit", "quit"):
            break

        ans, score, top = solver.safe_ask(q, top_n=3)
        print(f"\nAnswer: {ans}")
        print(f"Score: {score:.3f}")
        print("\nTop matches:")
        for idx, s, oq, a in top:
            print(f" - idx={idx}, score={s:.3f}, Q={oq}")
