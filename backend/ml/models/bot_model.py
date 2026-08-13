import pandas as pd 

df = pd.read_csv("../../../data/processed/bot_dataset.csv")

for i in df.columns:
    if i not in ["label","statuses_count","followers_count","friends_count","created_at"]:
        df = df.drop(columns=i)

df.to_csv("../../../data/processed/bot_dataset.csv",index=False)