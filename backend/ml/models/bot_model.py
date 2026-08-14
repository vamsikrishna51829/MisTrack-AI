import pandas as pd 
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("../../../data/processed/bot_dataset.csv")

X = df.drop(columns=["label","created_at"])
Y = df["label"]

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

model = XGBClassifier(n_estimators=100, max_depth = 5,learning_rate = 0.3)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

report = classification_report(y_test,y_pred)
print(report)

feature_importance = pd.DataFrame({
    "feature" : X.columns,
    "importance" : model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

print(feature_importance)