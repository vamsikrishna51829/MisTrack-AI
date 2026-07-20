import pandas as pd 
import sys

def news_combine(df1:pd.DataFrame = None,df2:pd.DataFrame = None):
    try:
        if df2 != None:
            df2 = df2.rename(columns={
                "username" : "author",
                "created_at" : "publishedAt",
                "display_name" : "title",
                "note" : "description",
            })

            
            df2 = df2.assign(platform = "Mastodonapi",source = "mastodon.social")
        
        if df1 != None:
            df1 = df1.assign(platform = "Newsapi")

        if (df1 != None) and (df2 != None):
            df = pd.concat([df1,df2])

        elif (df1 == None) and (df2 != None):
            df = df2

        elif (df1 != None) and (df2 == None):
            df = df1

        else:
            return None

        df.to_csv("../../data/processed/unified_dataset.csv",index=False)

    except Exception as e:
        print(e)
        