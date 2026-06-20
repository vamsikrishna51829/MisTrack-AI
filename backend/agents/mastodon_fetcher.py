import requests
from dotenv import load_dotenv
from os import getenv
from ratelimit import limits
import sys
import pandas as pd

def get_mastodonapi():

    load_dotenv()
    Mastodonapi = getenv("MASTODON_ACCESS_TOKEN")
    Mastodon_url = getenv("MASTODON_BASE_URL")
    call_api(Mastodonapi=Mastodonapi,Mastodon_url=Mastodon_url+"/api/v2/search")

@limits(calls=1,period=6)
def call_api(Mastodonapi,Mastodon_url):
    
    parameters = {
        "apiKey": Mastodonapi,
        'q': "COVID",
        'limit':6,

    }

    response = requests.get(url=Mastodon_url,params=parameters)
    if response.status_code == 200:
        json_into_dataframe(response.json())
        
    else:
        raise Exception('Api response:',response.json())
        

def json_into_dataframe(JSON):

    data = JSON
    df = pd.DataFrame(data=data['accounts'],columns=["username","acct","display_name","note","bot","followers_count","status_count","created_at","url"])
    df.to_csv("../../data/raw/Mastodonapi_KEYWORD_TIMESTAMP.csv",index=False,)

get_mastodonapi()