import numpy as np

def get_top_matches(vectorizer, vectors, user_question, top_n=3):
    user_vec = vectorizer.transform([user_question])
    scores = cosine_similarity(user_vec, vectors)[0]
    idxs = np.argsort(scores)[::-1][:top_n]
    return idxs, scores[idxs]