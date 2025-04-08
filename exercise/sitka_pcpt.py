from datetime import datetime 
import csv
import matplotlib.pyplot as plt

with open('data/sitka_weather_07-2018.csv') as fp:
    reader = csv.reader(fp)
    header = next(reader)
    rows = list(reader)

    pcpt = [float(row[3]) for row in rows]
    dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]



fig,ax = plt.subplots()
ax.plot(dates,pcpt)
fig.autofmt_xdate()
plt.show()