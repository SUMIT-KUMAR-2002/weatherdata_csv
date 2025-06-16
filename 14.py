import pandas

data = pandas.read_csv("pandas/weather_data.csv")
print(type(data))
print(data["temp"])


data_dict = data.to_dict()
print(data_dict)