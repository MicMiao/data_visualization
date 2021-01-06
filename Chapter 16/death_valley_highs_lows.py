import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures from this file. 
    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # strptime() method from datetime module
        try:
            low = int(row[5])
            high = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:    
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
title = 'Daily high and low temperatures - 2018\n Death Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
