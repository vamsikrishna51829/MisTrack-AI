import random
import pandas as pd

def main():

    df = pd.read_csv("../../../data/processed/danger_score.csv")
    print(df.shape)
    danger_score = df['danger_score']
    danger_score = [i*100 for i in danger_score]
    df['danger_score'] = danger_score
    df.to_csv("../../../data/processed/danger_score.csv",index=False)


if __name__ == "__main__":
    main()