# -*- coding: utf-8 -*-
"""
Created on Tue May 03 18:29:53 2016

@author: Administrator
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Administrator\Documents\Python Scripts\pandas-cookbook-0.2\data\bikes.csv', \
sep=';',encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
print df.ix[:5,:5]
df['Berri 1'].plot()
df.plot(figsize=(15,10))
berri_bikes = df['Berri 1']
arr = berri_bikes.index.weekday
df.insert(2,'weekday',arr)
berri_weekday = df['Berri 1','weekday']

matplotlib.pyplot.style.use('ggplot')
#pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 100) 

df = pd.read_csv(r'C:\Users\Administrator\Documents\Python Scripts\pandas-cookbook-0.2\data\311-service-requests.csv')
df.fillna(value=0,inplace = True)

df['Complaint Type'][:10].value_counts().plot(kind = 'bar',figsize = (15,10))
df.ix[:5,:5]

df.insert(2,'weekday',arr)

url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

url = url_template.format(month = 3,year =2012)

weather_mar2012 = pd.read.csv(url,skiprows = 16,index_col = 'Date/Time',parse_dates = True,\
encoding = 'latin1')


pd.set_option('max_colwidth',5)
weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'],axis = 1,inplace = True)
weather_mar2012.is_copy = False

temperatures.groupby('Hour').aggregate(np.mean,axis = 0).plot()

import pandas as pd
def download_weather_month(year, month):
    if month == 1:
        year += 1
    url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data
    
weather_data = download_weather_month(2012, 1)

print weather_data.ix[:5,:5]

data_by_month = [download_weather_month(2012, i) for i in range(1,13)]

print data_by_month[0][:5]
weather_2012['Temp (C)'].resample('1M').median().plot(kind='bar')
pct.loc[:,'ind']=pd.Series(np.arange(69),index = pct.index)

data_by_month



