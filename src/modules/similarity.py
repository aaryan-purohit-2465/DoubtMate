from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_best_match(vectorizer, vectors, user_question):
    user_vec = vectorizer.transform([user_question])
    similarity_scores = cosine_similarity(user_vec, vectors)[0]
    best_idx = np.argmax(similarity_scores)
    best_score = similarity_scores[best_idx]
    return best_idx, float(best_score)