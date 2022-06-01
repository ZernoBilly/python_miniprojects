
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


def get_diff(data):
    data["Diff_percent"] = (data["Open"].diff() / data["Open"]) * 100
    data["Diff_percent"] = data["Diff_percent"].fillna(0)
    return data


def group_by_weekday(data):
    return data.groupby("Weekday")["Diff_percent"].mean(5)


def get_avg_weekday(stock_data, weekday_avarage):
    avg_weekday = []

    for index, row in stock_data.iterrows():
        avg_day = weekday_avarage[row["Weekday"]]
        if row["Diff_percent"] == 0.0:
            avg_day = 0.000000
        avg_weekday.append(avg_day)

    stock_data["Avg_weekday"] = avg_weekday
    return stock_data


def get_diff_from_max(stock_data):
    stock_data["Diff_from_max"] = [
        x for x in stock_data["High"] - stock_data["High"].max()]
    return stock_data


def get_diff_from_min(stock_data):
    stock_data["Diff_from_min"] = [
        x for x in stock_data["Low"] - stock_data["Low"].min()]
    return stock_data
