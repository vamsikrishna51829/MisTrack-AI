import joblib
import pandas as pd 

def load_model():
    model = joblib.load("../trained_models/bot_XGBClassifier.joblib")
    return model

def run_model():
    model = load_model()

    feature = pd.DataFrame([{
        # "statuses_count": 2000,
        # "followers_count": 5000,
        # "friends_count": 5000,
        'followers_to_friends_ratio': 1.2,
        # "account_age_days":30,
        "avg_daily_posts":0.5,
        # "is_zero_followers":0
    }])

    prediction = model.predict(feature)
    probability = model.predict_proba(feature)

    print(prediction)
    print(probability)
run_model()