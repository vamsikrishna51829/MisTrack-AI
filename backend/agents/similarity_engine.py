import pandas as pd 
from sentence_transformers import SentenceTransformer

def similarity_engine():
    sentence = [
                "i love ai",
                "i love machine learning",
                "i love sun",
                "redbull gives you wings",
                "i can fly using redbull"
                ]
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(sentence,normalize_embeddings=True)
    print(embedding.shape)
similarity_engine()