
import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(keyword, max_tweets=100):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} lang:en').get_items()):
        if i >= max_tweets:
            break
        tweets.append([tweet.date, tweet.user.username, tweet.content])

    df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])
    df.to_csv("data/tweets.csv", index=False)
    return df
