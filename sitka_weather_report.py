import csv 
import matplotlib.pyplot as plt 
from datetime import datetime 

filename = 'data/death_valley_2021.csv'

def finding_temp_value(header_row):
    for value, row in enumerate(header_row):
        if row == 'TMAX':
            value_max= value

        elif row == 'TMIN':
            value_min= value

    return value_max, value_min


with open(filename) as dv_fp:
    dv_reader = csv.reader(dv_fp)
    dv_header_row = next(dv_reader)
    dv_value_max, dv_value_min = finding_temp_value(dv_header_row)
    # for value, row in enumerate(header_row):
    #     print(value, row)
    rows = list(dv_reader)
    dv_dates = []
    dv_highs = []
    dv_lows  = []
    

for row in rows:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[dv_value_max])
        low = int(row[dv_value_min])

    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dv_dates.append(current_date)
        dv_highs.append(high)
        dv_lows.append(low)


with open('data/sitka_weather_2021.csv') as sk_fp:
    sk_reader = csv.reader(sk_fp)
    sk_header_row = next(sk_reader)
    sk_value_max, sk_value_min = finding_temp_value(sk_header_row)
    rows_1 = list(sk_reader)
    sk_dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows_1]
    sk_highs = [int(row[sk_value_max]) for row in rows_1]
    sk_lows = [int(row[sk_value_min]) for row in rows_1]

plt.style.use('bmh')
fig, ax = plt.subplots()
#alpha is transparency 
ax.plot(dv_dates,dv_highs,c= 'red',alpha = 0.4)
ax.plot(dv_dates,dv_lows,c = 'blue', alpha = 0.4)
ax.fill_between(dv_dates,dv_highs,dv_lows, facecolor = 'blue', alpha = 0.2)

ax.plot(sk_dates, sk_highs, c = 'green', alpha = 0.4)
ax.plot(sk_dates, sk_lows, c = 'yellow', alpha = 0.4)
ax.fill_between(sk_dates,sk_highs, sk_lows, facecolor= 'green', alpha = 0.1)


ax.plot()
ax.set_title("Daily high temp in Sitka 2021s",fontsize = 15)
ax.set_xlabel("Days", fontsize = 13)
ax.set_ylabel("Temperature (F)", fontsize = 13)
ax.tick_params(axis='both', which='major', labelsize = 13)
fig.autofmt_xdate()
plt.show()