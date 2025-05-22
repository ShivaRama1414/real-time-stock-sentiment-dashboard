
from textblob import TextBlob
import pandas as pd

def analyze_sentiments(df):
    sentiments = []
    for tweet in df["Tweet"]:
        polarity = TextBlob(tweet).sentiment.polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        sentiments.append((tweet, sentiment, polarity))

    df["Sentiment"] = [s[1] for s in sentiments]
    df["Polarity"] = [s[2] for s in sentiments]
    return df
