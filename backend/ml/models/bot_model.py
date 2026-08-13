import pandas as pd 

import pandas as pd 

df1, df2 = map(pd.read_csv,["../../../data/raw/cresci-2017/genuine_accounts/users.csv","../../../data/raw/cresci-2017/social_spambots_1/users.csv"])

df1 = df1.drop(columns=["test_set_1","test_set_2"])
df2 = df2.drop(columns=["test_set_1"])
df1["label"] = 0
df2["label"] = 1
df = pd.concat([df1,df2],ignore_index=True)

df.to_csv("../../../data/processed/bot_dataset.csv",index=False)