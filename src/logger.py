import logging
from config import LOG_PATH

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_query(question, answer, score):
    logging.info(f"Q: {question} | A: {answer} | Score: {score}")