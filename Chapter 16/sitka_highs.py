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
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # strptime() method from datetime module
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
        
# print(highs)


# Plotting high temperatures using Matplotlib
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title('Daily high temperatures - 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


















