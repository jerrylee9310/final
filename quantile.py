### The thing I have to do
### 1. data is valid only it is measured(7th block != 0)
### 2. when 7th block has the value bigger than 1, how to dealing the previous days

def Time_and_Rain(infolist, time, *specific_month):
    rain = {}

    if time == 'daily':
        for i in range(1, len(infolist) - 1):
            a = infolist[i][5]
            b = infolist[i][6]
            if a == '':
                continue
            else:
                if b == '':
                    key = tuple(infolist[i][2:5])
                    curRain = float(infolist[i][5])
                    rain[key] = rain.get(key, 0) + curRain
                elif int(b) == 1:
                    key = tuple(infolist[i][2:5])
                    curRain = float(infolist[i][5])
                    rain[key] = rain.get(key, 0) + curRain

        return rain

    if time == 'monthly':
        months = []
        rains = []
        for i in range(1, len(infolist) - 1):
            if infolist[i][6] != '':
                y = infolist[i][2:4]
                if y not in months:
                    months.append(y)

        for month in months:
            rainamount = 0
            for j in range(1, len(infolist) - 1):
                if infolist[j][2:4] == month:
                    k = infolist[j][5]
                    if k == '':
                        continue
                    else:
                        rainamount += float(k)
            rains.append(round(rainamount, 2))

        for i in range(len(months)):
            key = tuple(months[i])
            curRain = rains[i]
            rain[key] = rain.get(key, 0) + curRain

        return rain
    if time == 'yearly':
        years = []
        rains = []
        for i in range(1, len(infolist) - 1):
            if infolist[i][6] != '':
                y = infolist[i][2]
                if y not in years:
                    years.append(y)

        for year in years:
            rainamount = 0
            for j in range(1, len(infolist) - 1):
                if infolist[j][2] == year:
                    if infolist[j][6] != '':
                        k = infolist[j][5]
                        if k == '':
                            continue
                        else:
                            rainamount += float(k)
            rains.append(round(rainamount, 2))

        for i in range(len(years)):
            key = years[i]
            curRain = rains[i]
            rain[key] = rain.get(key, 0) + curRain

        return rain
    if time == 'month+year':
        specific_month = specific_month[0]
        # year-data
        years = []
        for i in range(1, len(infolist) - 1):
            a = infolist[i][5]
            b = infolist[i][6]
            if a == '' and b == '':
                continue
            else:
                y = infolist[i][2]
                if y not in years:
                    years.append(y)
        # y_axis val
        rains = []
        for year in years:
            rainamount = 0
            for j in range(1, len(infolist) - 1):
                if infolist[j][2] == year:
                    if int(infolist[j][3]) == int(specific_month):
                        k = infolist[j][5]
                        if k == '':
                            continue
                        else:
                            rainamount += float(k)
            rains.append(round(rainamount, 2))

        for i in range(len(years)):
            key = years[i]
            curRain = rains[i]
            rain[key] = rain.get(key, 0) + curRain
        return rain


def getThresholdVal_b(time_series, frequency, rain, threshold_type):
    N_total = len(time_series)
    threshold = round(N_total / frequency)
    dup_rain = rain[:]
    dup_rain.sort()
    # Case. high
    if threshold_type == 'high':
        return dup_rain[len(rain) - threshold]
    # Case. low
    else:
        return dup_rain[threshold - 1]


def getResult_b(data, rain, thres, type):
    result = []
    # Cse. high
    if type == 'high':
        # Output part
        for i in range(len(rain)):
            if rain[i] >= thres:
                result.append(data[i])

    # Case. low
    if type == 'low':
        # Output part
        for i in range(len(rain)):
            if rain[i] <= thres:
                result.append(data[i])

    return result


def getThresholdVal_a(data, rain, freq, type):
    thres_vals = []
    if type == 'high':
        for i in range(0, len(rain)):
            tmp = 0
            diff = []
            for j in range(0, len(rain)):
                if rain[i] <= rain[j]:
                    tmp = j
                    break
            for k in range(tmp+1, len(rain)):
                if rain[i] <= rain[k]:
                    if k-tmp >= freq:
                        diff.append(k - tmp)
                        tmp = k
                    else:
                        break
            if diff != []:
                thres_vals.append(rain[i])
        if thres_vals == []:
            return 'None'
        else:
            thres_val_a = min(thres_vals)
            return thres_val_a

    else:
        for i in range(0, len(rain)):
            tmp = 0
            diff = []
            for j in range(0, len(rain)):
                if rain[i] >= rain[j]:
                    tmp = j
                    break
            for k in range(tmp+1, len(rain)):
                if rain[i] >= rain[k]:
                    if k-tmp >= freq:
                        diff.append(k-tmp)
                        tmp = k
                    else:
                        break
            if diff != []:
                thres_vals.append(rain[i])
        if thres_vals == []:
            return 'None'
        else:
            thres_val_a = max(thres_vals)
            return thres_val_a


def getResult_a(data, rain, thres, type):
    result = []
    if thres == 'None':
        return ['None']
    if type == 'high':
        for index in range(len(rain)):
            if rain[index] >= thres:
                result.append(data[index])
        return result
    else:
        for index in range(len(rain)):
            if rain[index] <= thres:
                result.append(data[index])
        return result

import csv
import numpy as np
import matplotlib.pyplot as mpl

#
# file input
#
Canberra = open('Rainfall_Canberra_070247.csv')
Queanbeyan = open('Rainfall_Queanbeyan_070072.csv')
Sydney = open('Rainfall_Sydney_066062.csv')

#
# User input
#
#   city
while True:
    tmpCity = input("Which city do you want to comput?"+'\n'
             "a) Canberra, b) Queanbeyan, c) Sydney"+'\n')
    if tmpCity == 'a':
        city = Canberra
        break
    elif tmpCity == 'b':
        city = Queanbeyan
        break
    elif tmpCity == 'c':
        city = Sydney
        break
    else:
        print("Try again")

#   type of time series
while True:
    time = input("Which type of data you want to know?"+'\n'
                "a) daily, b) monthly, c) yearly, d)  specific month of the years"+'\n')
    if time == 'a':
        time = 'daily'
        break
    if time == 'b':
        time = 'monthly'
        break
    if time == 'c':
        time = 'yearly'
        break
    elif time == 'd':
        time = 'month+year'
        month = input('Which month you want to compute?' + '\n')
        break
    else:
        print("Try again")

#   threshold (high or low)
while True:
    threshold_type = input("high or low?"+"\n"
                      "a) high, b) low" + "\n")
    if threshold_type == 'a':
        threshold_type = 'high'
        break
    if threshold_type == 'b':
        threshold_type = 'low'
        break
    else:
        print("Type again plz")

#   frequency F
while True:
    frequency = input("Enter the frequency"+"\n")
    if frequency.isnumeric() == True:
        frequency = int(frequency)
        break
    else:
        print("plz enter the numeric value")


#
# city data process
#
reader = csv.reader(city)
infolist = []
for row in reader:
    infolist.append(row)


# data processing
if time == 'month+year':
    data = Time_and_Rain(infolist, time, month)
else:
    data = Time_and_Rain(infolist, time)
time_series = list(data.keys())
rain_amount = list(data.values())


# compute threshold val

# method a.
thres_val_a = getThresholdVal_a(time_series, rain_amount, frequency, threshold_type)
result_a = getResult_a(time_series, rain_amount, thres_val_a, threshold_type)
# method b.
thres_val_b = getThresholdVal_b(time_series, frequency, rain_amount, threshold_type)
result_b = getResult_b(time_series, rain_amount, thres_val_b, threshold_type)

#
# graph part
#
graphYorN = input("Do you want to see the graph? (Y/N)\n")

#
# Output
#
# Method A.
print("[Method A]:\nThreshold value =", thres_val_a, "\nCorresponding values are")
for i in result_a:
    print(i)
# Method B. threshold val # corresponding time values
print("[Method B]\nThreshold value =", thres_val_b, "\nCorresponding values are ")
for i in result_b:
    print(i)


if graphYorN == 'Y':
    x_val = time_series
    y = rain_amount # corresponding list of total rainfall values
    x = np.arange(0, len(y))
    mpl.bar(x + 0.25, y, 0.5, color='blue')
    mpl.plot([0, len(y) + 1], [thres_val_a, thres_val_a], '--k')  # the threshold line
    mpl.plot([0, len(y) + 1], [thres_val_b, thres_val_b], '--k')  # the threshold line
    mpl.xticks(x + 0.5, x_val, rotation=90)
    mpl.show()





