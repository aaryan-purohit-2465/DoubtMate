# file created by abhinav
import re

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def preprocess_questions(df):
    df["cleaned_question"] = df["question"].apply(clean_text)
    return df