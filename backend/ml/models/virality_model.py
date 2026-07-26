import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def virality_model():

    X,Y = returning_XY()
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    model = RandomForestClassifier(random_state=50,class_weight="balanced")

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    print(classification_report(y_test,y_pred))

def returning_XY():
    df = pd.read_csv("../../../data/processed/virality_dataset.csv")
    X = df.drop(columns=["title","label"])
    Y = df["label"]
    return [X,Y]

virality_model()
