# import requests
# import numpy as np

# url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m" 

# response = requests.get(url)
# data = response.json()

# print(data)

import matplotlib.pyplot as plt

world_temperatures = {
    "Continents": {
        "Africa": 24.8,
        "Asia": 13.0,
        "Europe": 10.4,
        "North America": 2.5,
        "South America": 21.0,
        "Oceania": 21.5,
        "Antarctica": -56.7
    },
    "Oceans (Surface)": {
        "Pacific Ocean": 16.9,
        "Atlantic Ocean": 16.1,
        "Indian Ocean": 17.0,
        "Arctic Ocean": -11.4,
        "Southern Ocean": 3.5,
        "Mediterranean Sea": 19.5,
        "Red Sea": 32.2
    },
    "Hottest Regions": {
        "Burkina Faso": 30.4,
        "Mali": 29.2,
        "Aruba": 29.1,
        "Senegal": 28.9,
        "Djibouti": 28.5,
        "Bahrain": 28.2,
        "Qatar": 28.2,
        "United Arab Emirates": 28.0
    },
    "Coldest Regions": {
        "Russia": -5.1,
        "Canada": -5.3,
        "Mongolia": -0.7,
        "Norway": 1.5,
        "Kyrgyzstan": 1.6,
        "Finland": 1.7,
        "Iceland": 1.8,
        "Sweden": 2.1
    },
    "Temperate/Major Regions": {
        "Brazil": 25.0,
        "India": 24.5,
        "Australia": 21.6,
        "Mexico": 21.0,
        "United States": 11.5,
        "Japan": 12.0,
        "United Kingdom": 9.5,
        "Central Asia": 10.2,
        "Sahel Region": 28.5,
        "Southeast Asia": 27.0
    }
}

# declaring variables and temperature list
temperature_list = []
categories_list = []
list_size = 0

# Creating a 2-D list for the above 2-D dictionary
for keys, values in world_temperatures.items():
    categories_list.append(keys) # creating categories list
    sub_values_row = [] # temperature data related to each category
    for sub_keys, sub_values in values.items():
        sub_values_row.append(sub_values)
    temperature_list.append(sub_values_row) # appending rows in temperature list


print("\n\n")
print(categories_list)
print("\n\n")
print(temperature_list)
print("\n\n")



# Data for the pie slices
sizes = [30, 25, 20, 15, 10]
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']

plt.pie(temperature_list, labels=categories_list)
plt.title('Programming Language Popularity')
# plt.show()