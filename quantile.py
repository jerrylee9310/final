### The thing I have to do
### 1. data is valid only it is measured(7th block != 0)
### 2. when 7th block has the value bigger than 1, how to dealing the previous days

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
city = input("Which city do you want to comput?"+'\n'
             "a) Canberra, b) Queanbeyan, c) Sydney"+'\n')
if city == 'a':
    city = Canberra
elif city == 'b':
    city == Queanbeyan
elif city == 'c':
    city == Sydney
else:
    raise NameError("It's not in options. Enter among 'a','b' and 'c'")
#   type of time series
    
time = input("Which type of data you want to know?"+'\n'
            "a) daily, b) monthly, c) specific month of the years, d) yearly"+'\n')
    
# Depends on choice, set the detail option.
if time == 'c':
    month = input('Which month you want to compute?'+'\n')
#   threshold (high or low)
threshold_type = input("high or low?"+"\n"
                  "a) high, b) low" + "\n")
#   frequency F
frequency = int(input("Enter the frequency"+"\n"))

#
# city data process
#
reader = csv.reader(city)
infolist = []
for row in reader:
    infolist.append(row)
    
# Case1. daily
if time == 'a':
    # align depends on time series
    # x&y axis val
    days = []
    rain = []
    for i in range(1,len(infolist)-1):
        a = infolist[i][6]
        if a == '':
            continue
        elif int(a) == 1:
            y = infolist[i][2:5]
            k = infolist[i][5]
            days.append(y)
            rain.append(k)
            
#   compute threshold val
#       method a.
#       method b.
    N_total = len(days)
    threshold = round(N_total/frequency)
    result = []
    # Case. high
    if threshold_type == 'a':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[len(dup_rain)-threshold]
        # Output part
        for i in range(len(rain)):
            if rain[i] >= thres_val:
                result.append(days[i])
    # Case. low
    if threshold_type == 'b':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[threshold-1]
        # Output part
        for i in range(len(rain)):
            if rain[i] <= thres_val:
                result.append(days[i])
            
# Case2. monthly
if time == 'b':
    # align depends on time series
    # x&y axis val
    months = []
    rain = []
    for i in range(1,len(infolist)-1):
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
        rain.append(rainamount)
            
#   compute threshold val
#       method a.
#       method b.
    N_total = len(months)
    threshold = round(N_total/frequency)
    result = []
    # Case. high
    if threshold_type == 'a':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[len(dup_rain)-threshold]
        # Output part
        for i in range(len(rain)):
            if rain[i] >= thres_val:
                result.append(months[i])
    # Case. low
    if threshold_type == 'b':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[threshold-1]
        # Output part
        for i in range(len(rain)):
            if rain[i] <= thres_val:
                result.append(months[i])

# Case3. specific month of the years
if time == 'c':
    # allign depends on time series
    # x_axis val
    years = []
    for i in range(1,len(infolist)-1):
        y = infolist[i][2]
        if y not in years:
            years.append(y)
    # y_axis val
    rain = []
    for year in years:
        rainamount = 0
        for j in range(1, len(infolist) - 1):
            if infolist[j][2] == year:
                if int(infolist[j][3]) == int(month):
                    k = infolist[j][5]
                    if k == '':
                        continue
                    else:
                        rainamount += float(k)
        rain.append(rainamount)
        
#   compute threshold val
#       method a.
#       method b.
    N_total = len(years)
    threshold = round(N_total/frequency)
    result = []
    # Case. high
    if threshold_type == 'a':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[len(dup_rain)-threshold]
        # Output part
        for i in range(len(rain)):
            if rain[i] >= thres_val:
                result.append(years[i])
    # Case. low
    if threshold_type == 'b':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[threshold-1]
        # Output part
        for i in range(len(rain)):
            if rain[i] <= thres_val:
                result.append(years[i])
                
# Case4. yearly
if time == 'd':
    # align depends on time series
    # x&y axis val
    years = []
    rain = []
    for i in range(1,len(infolist)-1):
        y = infolist[i][2]
        if y not in years:
            years.append(y)
        
    for year in years:
        rainamount = 0
        for j in range(1, len(infolist) - 1):
            if infolist[j][2] == year:
                    k = infolist[j][5]
                    if k == '':
                        continue
                    else:
                        rainamount += float(k)
        rain.append(rainamount)
            
    #   compute threshold val
    #       method a.
    #       method b.
    N_total = len(years)
    threshold = round(N_total/frequency)
    result = []
    # Case. high
    if threshold_type == 'a':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[len(dup_rain)-threshold]
        # Output part
        for i in range(len(rain)):
            if rain[i] >= thres_val:
                result.append(years[i])
    # Case. low
    if threshold_type == 'b':
        dup_rain = rain[:]
        dup_rain.sort()
        thres_val = dup_rain[threshold-1]
        # Output part
        for i in range(len(rain)):
            if rain[i] <= thres_val:
                result.append(years[i])
        
#
# graph part
#
if time == 'a':
    x_val = days
elif time == 'b':
    x_val = months
elif time == 'c':
    x_val = years
    
y = rain # corresponding list of total rainfall values
x = np.arange(0, len(y))
mpl.bar(x + 0.25, y, 0.5, color='blue')
mpl.plot([0, len(y) + 1], [thres_val, thres_val], '--k')  # the threshold line
mpl.xticks(x + 0.5, x_val, rotation=90)
mpl.show()

#            
# Output
#
#   threshold val
print("Threshold value is: ", thres_val)
#   corresponding time values
print("Corresponding values are : ", result)






