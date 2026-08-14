import pandas as pd 

df = pd.read_csv("../../../data/processed/bot_dataset.csv")

# df = df.drop(columns=["Unnamed: 0"])

statuses_count = df["statuses_count"]
account_age_days = df["account_age_days"]
avg_daily_posts = []

for i in range(len(df["statuses_count"])):
    if account_age_days[i] != 0:
        avg_daily_posts.append(statuses_count[i]/account_age_days[i])
    else:
        avg_daily_posts.append(0)

df["avg_daily_posts"] = avg_daily_posts

df.to_csv("../../../data/processed/bot_dataset.csv",index=False)