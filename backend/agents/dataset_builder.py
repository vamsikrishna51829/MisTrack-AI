import pandas as pd 

def news_combine():

    df1,df2 = map(pd.read_csv,["../../data/raw/newsapi_KEYWORD_TIMESTAMP.csv","../../data/raw/Mastodonapi_KEYWORD_TIMESTAMP.csv"])

    df2 = df2.rename(columns={
        "username" : "author",
        "created_at" : "publishedAt",
        "display_name" : "tittle",
        "note" : "description",
    })

    df1 = df1.assign(platform = "Newsapi")
    df2 = df2.assign(platform = "Mastodonapi",source = "mastodon.social")

    df = pd.concat([df1,df2])
    
    df.to_csv("../../data/processed/unified_dataset.csv",index=False)
news_combine()