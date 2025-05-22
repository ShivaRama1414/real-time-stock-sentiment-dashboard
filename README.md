
# 📊 Real-Time Stock Sentiment Dashboard

A real-time interactive dashboard that combines Twitter sentiment analysis and live stock price tracking.

## 🚀 Features
- Scrapes tweets about selected stock tickers
- Runs sentiment analysis (Positive, Negative, Neutral)
- Retrieves real-time stock price data from Yahoo Finance
- Visualizes sentiment distribution, tweet word clouds, and stock trends

## 🧰 Tech Stack
- Python
- Streamlit
- snscrape
- TextBlob
- yfinance
- Matplotlib / WordCloud

## 📂 Project Structure
```
real-time-stock-sentiment-dashboard/
├── app/
│   ├── twitter_scraper.py
│   ├── sentiment_analysis.py
│   ├── stock_data.py
│   └── dashboard.py
├── data/
│   └── tweets.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## 🖥️ Run Locally
```bash
git clone https://github.com/yourusername/real-time-stock-sentiment-dashboard.git
cd real-time-stock-sentiment-dashboard
pip install -r requirements.txt
streamlit run app/dashboard.py
```

## 📈 Example Use Cases
- Financial sentiment monitoring
- Market behavior research
- Real-time news & stock correlation
