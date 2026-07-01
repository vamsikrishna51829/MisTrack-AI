import pandas as pd 
from sentence_transformers import SentenceTransformer

def similarity_engine():
    sentences = pd.read_csv("../../data/processed/unified_dataset.csv",usecols=['gemini_response'])
    sentences = [i[0] for i in sentences.values]
    model = SentenceTransformer('all-MiniLM-L6-v2')    
    embedding = model.encode(sentences,normalize_embeddings=True)
    print(embedding.shape)
similarity_engine()