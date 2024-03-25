# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

print(data['Primary Fur Color'].value_counts()[0])

data_dict = {
    "Fur color" : ["Gray", "Red", "Black"] , 
    "Count" : [data['Primary Fur Color'].value_counts()[0], data['Primary Fur Color'].value_counts()[1], data['Primary Fur Color'].value_counts()[2]]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")