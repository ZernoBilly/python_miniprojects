import pandas as pd
from datetime import datetime, timedelta
from functions import *

DATE_TO = datetime.now()
DATE_FROM = DATE_TO - timedelta(days=100)


stock_data = get_stock_data("FORTUM.HE", DATE_FROM)
stock_data = get_weekdays(stock_data)
stock_data = get_diff(stock_data)
weekday_avarage = group_by_weekday(stock_data)
stock_data = get_avg_weekday(stock_data, weekday_avarage)

print(stock_data)
