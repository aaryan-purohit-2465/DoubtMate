# src/logger.py
import logging
from src.config import LOG_PATH

# ensure logs folder exists
import os
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_query(question, answer, score):
    try:
        logging.info(f"Q: {question} | A: {answer} | Score: {score}")
    except Exception:
        # never crash the app due to logging
        pass
