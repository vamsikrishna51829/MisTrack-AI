import requests
from dotenv import load_dotenv
from os import getenv
from ratelimit import limits
import sys
import pandas as pd

def get_news_from_newsapi(keyword:str):

    load_dotenv()
    Newsapi = getenv("NEWS_API_KEY")
    call_api(Newsapi=Newsapi,keyword= keyword)

@limits(calls=1,period=6)
def call_api(Newsapi,keyword):
    
    parameters = {
        "apiKey": Newsapi,
        'q': keyword,
        'pageSize':6
    }

    response = requests.get(url="https://newsapi.org/v2/everything",params=parameters)
    if response.status_code == 200:
        json_into_dataframe(response.json())
    else:
        raise Exception('Api response:',response.json().get('message'))

def json_into_dataframe(JSON):
    
    data = JSON
    data = data["articles"]
    df = pd.DataFrame(data=data)
    df['source'] = df['source'].apply(convert_to_name)
    df = df.drop(labels=['content','urlToImage'],axis=1)
    df.to_csv("../../data/raw/newsapi_KEYWORD_TIMESTAMP.csv",index=False)

def convert_to_name(source):

    source = dict(source)
    source = source['name']
    return source
