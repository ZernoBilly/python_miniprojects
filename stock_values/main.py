import pandas as pd
from datetime import datetime, timedelta
from functions import *

DATE_TO = datetime.now()
DATE_FROM = DATE_TO - timedelta(days=7)

# def get_stock_prices(tickers: list):
#     d = datetime.now() - timedelta(days=7)
#     for ticker in tickers:
#         data = pdr.get_data_yahoo(ticker, d)
#         close_price = list(data)
#         yield close_price


# for prices in get_stock_prices(["AAPL", "TWTR"]):
#     print(prices)


stock_data = get_stock_data("FORTUM.HE")

stock_data = get_weekdays(stock_data)

print(stock_data)
