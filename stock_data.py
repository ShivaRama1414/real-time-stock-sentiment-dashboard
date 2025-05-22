
import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="7d", interval="1h")
    hist.reset_index(inplace=True)
    return hist[["Datetime", "Close"]]
