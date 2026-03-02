import statistics
# average annual temperatures (in degrees Celsius) for 40 major world regions
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
list_size = 0
mean = 0

# appending members in temperature list
for sub_dict in world_temperatures.values():
    for temp_value in sub_dict.values():
        temperature_list.append(temp_value)
        list_size+=1
        mean+=temp_value

# sorting the temperature list
temperature_list.sort()
print("Data Set:", temperature_list)

# Mean
mean/=list_size
print("Mean is:", mean, "°C")

# Median
center_value = int( (list_size / 2) - 1 )
median = (temperature_list[center_value] + temperature_list[center_value + 1]) / 2
print("Median is:", median, "°C")

# Mode 
mode = statistics.mode(temperature_list)
print("Mode is:", mode, "°C")

# Variance
variance = round(statistics.variance(temperature_list), 4)
print("Variance is:", variance, "°C^2")

# Range
temp_range = temperature_list[list_size - 1] - temperature_list[0]
print("Range is:", temp_range, "°C")

# Standard Deviation
standard_deviation = round(statistics.stdev(temperature_list), 4)
print("Standard Deviation is:", standard_deviation, "°C")

