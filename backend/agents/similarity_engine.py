import pandas as pd 
from sentence_transformers import SentenceTransformer
import numpy as np
from itertools import combinations

def similarity_engine(threshold:float):
    # similarity_score = {}
    sentence1 = []
    sentence2 = []
    scores = []
    sentences = pd.read_csv("../../data/processed/unified_dataset.csv",usecols=['extracted_claim'])
    sentences = [i[0] for i in sentences.values]
    model = SentenceTransformer('all-MiniLM-L6-v2')    
    embedding = model.encode(sentences,normalize_embeddings=True)
    comb = combinations(embedding,2)
    comb_sentences = combinations(sentences,2)
    for sentence, pair in zip(comb_sentences, comb):
        score = distance_of_vectors(pair[0],pair[1])
        if score >= threshold:
            sentence1.append(sentence[0])
            sentence2.append(sentence[1])
            scores.append(score)
    # return similarity_score
    df = pd.DataFrame({
        "sentence1": sentence1,
        "sentence2": sentence2,
        "score" : scores
    })
    df.to_csv("../../data/processed/similarity_dataset.csv",index=False)

def distance_of_vectors(vector1,vector2):
    return np.dot(vector1,vector2)

similarity_engine(0.3)