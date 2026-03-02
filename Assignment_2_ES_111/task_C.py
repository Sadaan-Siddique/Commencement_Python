import matplotlib.pyplot as plt

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


main_category_totals = {}
for category, sub_dict in world_temperatures.items(): # Summing absolute values of all items in the sub-dictionary
    main_category_totals[category] = sum(abs(v) for v in sub_dict.values())

# Flattening for Histogram/Scatter (Global analysis)
all_temps = [temp for sub_dict in world_temperatures.values() for temp in sub_dict.values()]

# Setup Figure (2x2 grid)
fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.suptitle('Global Temperature Analysis: Main Categories', fontsize=20, fontweight='bold', y=1)
ax = axes.flatten()


# --- Plot 1: Pie Chart for main Categories ---
ax[0].pie(main_category_totals.values(), 
          labels=main_category_totals.keys(), 
          autopct='%1.1f%%', 
          startangle=140, 
          pctdistance=0.70, 
          explode=[0.03]*len(main_category_totals)) # Slight gap between slices
ax[0].set_title("Distribution by Main Category (Pie)", fontweight='bold', pad=20)


# --- Plot 2: Histogram of All Temperatures ---
ax[1].hist(all_temps, bins=15, color='skyblue', edgecolor='black')
ax[1].set_title("Global Temperature Frequency (Histogram)", fontweight='bold')
ax[1].set_xlabel("Temperature (°C)")


# --- Plot 3: Bar Chart of Category Totals ---
ax[2].bar(main_category_totals.keys(), main_category_totals.values(), color='salmon')
ax[2].set_title("Total Magnitude per Category (Bar)", fontweight='bold')
ax[2].tick_params(axis='x', rotation=15) # Slight tilt for long category names


# --- Plot 4: Scatter Plot of All Individual Data Points ---
ax[3].scatter(range(len(all_temps)), all_temps, color='purple', alpha=0.6)
ax[3].axhline(0, color='black', linestyle='--', linewidth=1)
ax[3].set_title("Individual Location Data (Scatter)", fontweight='bold')
ax[3].set_ylabel("Temperature (°C)")


# layout for clear gaps between rows and columns
plt.subplots_adjust(hspace=0.4, wspace=0.5)
plt.show()