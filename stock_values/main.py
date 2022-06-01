import pandas as pd
from datetime import datetime, timedelta
from functions import *

# Ticker and days variables imported from jupyter notebook


DATE_TO = datetime.now()
DATE_FROM = DATE_TO - timedelta(days=days)


stock_data = get_stock_data(ticker, DATE_FROM)
stock_data = get_weekdays(stock_data)
stock_data = get_diff(stock_data)
weekday_avarage = group_by_weekday(stock_data)
stock_data = get_avg_weekday(stock_data, weekday_avarage)
stock_data = get_diff_from_max(stock_data)
stock_data = get_diff_from_min(stock_data)
stock_data = get_diff_percent_from_avg(stock_data)

stock_data.to_csv("data/stock_data.csv", index=False)
# print(stock_data.head(30))
