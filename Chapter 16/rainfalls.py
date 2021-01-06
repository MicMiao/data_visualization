import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename_1 = 'data/sitka_weather_2018_simple.csv'
filename_2 = 'data/death_valley_2018_simple.csv'

with open(filename_1) as f1:
    reader_1 = csv.reader(f1)
    header_row_1 = next(reader_1)

    dates_sit, rainfalls_sit = [], []
    
    for row in reader_1:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') 
        rainfall = float(row[3])
        dates_sit.append(current_date)
        rainfalls_sit.append(rainfall)


with open(filename_2) as f2:
    reader_2 = csv.reader(f2)
    header_row_2 = next(reader_2)
    
    dates_dea, rainfalls_dea = [], []
    for row in reader_2:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') 
        rainfall = float(row[3])
        dates_dea.append(current_date)
        rainfalls_dea.append(rainfall)        
    
# Plotting rainfalls
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_sit, rainfalls_sit, c='red', alpha=0.5)
ax.plot(dates_dea, rainfalls_dea, c='blue', alpha=0.5)


# Format plot.
title = 'Daily rainfalls - 2018\n Sitka and Death Valley'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfalls', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()
