import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def get_top_matches(vectorizer, vectors, user_question, top_n=3):
    """
    Returns top N matching question indices and their similarity scores
    """
    user_vec = vectorizer.transform([user_question])

    scores = cosine_similarity(user_vec, vectors)[0]

    top_indices = np.argsort(scores)[::-1][:top_n]
    top_scores = scores[top_indices]

    return top_indices, top_scores
