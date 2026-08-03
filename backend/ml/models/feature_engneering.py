from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv("../../../data/processed/virality_dataset.csv")
title = df["title"]

vectorizer = TfidfVectorizer(max_features=1000)
