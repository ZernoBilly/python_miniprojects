import pandas_datareader as pdr
from datetime import datetime, timedelta


def get_stock_prices(tickers: list):
    d = datetime.now() - timedelta(days=7)
    for ticker in tickers:
        data = pdr.get_data_yahoo(ticker, d)
        close_price = list(data["Close"])
        yield close_price


for prices in get_stock_prices(["AAPL", "TWTR"]):
    print(prices)
