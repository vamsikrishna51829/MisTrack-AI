import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from scipy.sparse import csr_matrix

def virality_model():

    X,Y,title = returning_XY()

    x_train,x_test,title_train,title_test,y_train,y_test = train_test_split(X,title,Y,test_size=0.2,random_state=42,stratify=Y)

    x_train_sparse = csr_matrix(x_train)
    x_test_sparse = csr_matrix(x_test)

    vectorizer = TfidfVectorizer(max_features=1000)
    title_train_tfidf = vectorizer.fit_transform(title_train)
    title_test_tfidf = vectorizer.transform(title_test)
    vectorizer.get_feature_names_out()

    train_sparse_matrix = hstack([x_train_sparse,title_train_tfidf])
    test_sparse_matrix = hstack([x_test_sparse,title_test_tfidf])

    model = RandomForestClassifier(n_estimators=100,random_state=50,class_weight="balanced")

    model.fit(train_sparse_matrix,y_train)

    y_pred = model.predict(test_sparse_matrix)

    print(classification_report(y_test,y_pred))

def returning_XY():
    df = pd.read_csv("../../../data/processed/virality_dataset.csv")
    title = df["title"]
    X = df.drop(columns=["title","label"])
    Y = df["label"]
    return [X,Y,title]

virality_model()