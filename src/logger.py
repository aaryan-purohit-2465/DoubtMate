import logging
import os
from src.config import LOG_PATH

# Ensure logs directory exists
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_query(question, answer, score):
    logging.info(f"Q: {question} | A: {answer} | Score: {score}")
