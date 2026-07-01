import pandas as pd 
from sentence_transformers import SentenceTransformer
import numpy as np
from itertools import combinations

def similarity_engine():
    similarity_score = []
    sentences = pd.read_csv("../../data/processed/unified_dataset.csv",usecols=['extracted_claim'])
    sentences = [i[0] for i in sentences.values]
    model = SentenceTransformer('all-MiniLM-L6-v2')    
    embedding = model.encode(sentences,normalize_embeddings=True)
    comb = combinations(embedding,2)
    for i in comb:
        similarity_score.append(distance_of_vectors(i[0],i[1]))
    print(similarity_score)

def distance_of_vectors(vector1,vector2):
    return np.dot(vector1,vector2)

similarity_engine()