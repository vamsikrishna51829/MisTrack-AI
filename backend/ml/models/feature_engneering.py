# title_exclamation_count,title_char_count,title_word_count,title_uppercase_ratio,title_sentiment,title_question_count
import pandas as pd
from textblob import TextBlob

df1 = pd.read_csv("../../../data/raw/merge.csv")
df2 = pd.read_csv("../../../data/processed/virality_dataset.csv")

def comb(df1,df2):
    return pd.concat([df1,df2])

def sentiment(sentence):
    sentence = TextBlob(sentence)
    return sentence.sentiment.polarity
def main():
    # title = df["title"]
    # count = 0
    # uppercase_ratio = []
    # for sentence in title:
    #     for alpha in sentence:
    #         if alpha.isupper():
    #             count += 1
    #     uppercase_ratio.append(count/len(sentence))
    #     count = 0
    # df["title_exclamation_count"] = [sentence.count('!') for sentence in title]
    # df['title_char_count'] = [len(sentence) for sentence in title]
    # df['title_word_count'] = [len(sentence.split()) for sentence in title]
    # df['title_question_count'] = [sentence.count('?') for sentence in title]
    # df['title_uppercase_ratio'] = uppercase_ratio
    # df['title_sentiment'] = [sentiment(sentence) for sentence in title]
    df = comb(df1,df2)
    df.to_csv('../../../data/processed/virality_dataset.csv',index=False)
    
main()