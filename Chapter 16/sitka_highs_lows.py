import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)
    
    # Extracting and reading data
    # Get dates, high temperatures from this file. 
    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # strptime() method from datetime module
        low = int(row[6])
        high = int(row[5])
        dates.append(current_date)
        lows.append(low)
        highs.append(high)
        
# print(highs)


# Plotting high and low temperatures using Matplotlib
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_ylim([20,140])

# Format plot.
plt.title('Daily high and low temperatures - 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

