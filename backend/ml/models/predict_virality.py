import joblib

def load_models():
    model = joblib.load("../trained_models/virality_random_forest.joblib")
    vectorizer = joblib.load("../trained_models/virality_tfidf_vectorizer.joblib")

    return model,vectorizer

def get_title():

    title = input("Enter the title:")

    return title

model,vectorizer = load_models()
