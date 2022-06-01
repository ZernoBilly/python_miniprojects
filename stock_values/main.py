import pandas as pd
from datetime import datetime, timedelta
from functions import *

DATE_TO = datetime.now()
DATE_FROM = DATE_TO - timedelta(days=200)


def get_diff_percent_from_avg(stock_data):
    avg = (stock_data["High"].mean() + stock_data["Low"].mean()) / 2
    values = []

    for i, row in stock_data.iterrows():
        day_avg = (row["High"] + row["Low"]) / 2
        dif_from_avg = day_avg - avg
        values.append(dif_from_avg)

    stock_data["Diff_percent_from_avg"] = values
    return stock_data


stock_data = get_stock_data("FORTUM.HE", DATE_FROM)
stock_data = get_weekdays(stock_data)
stock_data = get_diff(stock_data)
weekday_avarage = group_by_weekday(stock_data)
stock_data = get_avg_weekday(stock_data, weekday_avarage)
stock_data = get_diff_from_max(stock_data)
stock_data = get_diff_from_min(stock_data)
stock_data = get_diff_percent_from_avg(stock_data)


print(stock_data.tail(30))

# max_value = stock_data["High"].max()
# print((17.355000 / max_value) * 100)
