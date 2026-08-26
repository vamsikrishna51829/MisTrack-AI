import random
import pandas as pd
from agents.claim_extractor import calling_gemini

def generate_scenarios(count=10):
        
    scenarios = []

    for _ in range(count):

        scenario = {
            "virality_prob": random.uniform(0, 1),
            "bot_percentage": random.uniform(0, 1),
            "mutation_severity": random.randint(0, 3),
            "sentiment_extremity": random.uniform(0, 1),
            "reach_score": random.uniform(0, 1)
        }

        scenarios.append(scenario)

    return pd.DataFrame(scenarios)


def main():

    df = generate_scenarios()

    df.to_csv("../../data/processed/danger_score.csv",index=False)


if __name__ == "__main__":
    main()