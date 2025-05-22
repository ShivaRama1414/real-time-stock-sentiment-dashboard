
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from app.twitter_scraper import scrape_tweets
from app.sentiment_analysis import analyze_sentiments
from app.stock_data import get_stock_data

st.set_page_config(layout="wide")
st.title("📈 Real-Time Stock Sentiment Dashboard")

keyword = st.sidebar.text_input("Enter Stock Ticker (e.g., TSLA)", "TSLA")
max_tweets = st.sidebar.slider("Number of Tweets", 50, 500, 100)

if st.sidebar.button("Analyze"):
    tweets_df = scrape_tweets(keyword, max_tweets)
    sentiment_df = analyze_sentiments(tweets_df)
    stock_df = get_stock_data(keyword)

    st.subheader(f"Sentiment Distribution for ${keyword}")
    sentiment_counts = sentiment_df["Sentiment"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
    ax1.axis('equal')
    st.pyplot(fig1)

    st.subheader("Stock Price Over Time")
    st.line_chart(stock_df.set_index("Datetime")["Close"])

    text = " ".join(sentiment_df["Tweet"])
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    st.subheader("Tweet Word Cloud")
    st.image(wc.to_array())

    st.subheader("Sample Tweets")
    st.dataframe(sentiment_df.head(10))
