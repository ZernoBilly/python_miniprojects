
import constants as c
import pandas_datareader as pdr


def get_weekdays(data):
    day_mapper = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
                  3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    data["Weekday"] = data["Date"].map(lambda x: day_mapper[x.dayofweek])
    return data


def get_stock_data(tickers: str, date_from=c.DATE_FROM, date_to=c.DATE_TO):
    stock_data = pdr.DataReader(tickers, "yahoo", start=date_from, end=date_to)
    stock_data = stock_data.reset_index()
    stock_data.drop("Adj Close", inplace=True, axis=1)
    return stock_data
