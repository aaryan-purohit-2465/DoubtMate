from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer(corpus):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(corpus)
    return vectorizer, vectors