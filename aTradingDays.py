# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 02:54:01 2016

@author: Administrator
"""

from datetime import datetime,timedelta

start_date = '2011-01-01'
start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
print(start_date)
end_date = '2011-03-22'
end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
print(end_date)

def aTradingDays(start_date,end_date):
    f = 'aTradingDays.csv'
    with open(f,'r') as file:
        aTradingDays = []
        aTradingDays = file.readlines()
    
    for i in range(len(aTradingDays)):
        aTradingDays[i] = datetime.strptime(aTradingDays[i].strip("\n"),"%Y-%m-%d").date()
    print(aTradingDays)
    while start_date not in aTradingDays:
        start_date = start_date + timedelta(1)
    print(start_date)
    while end_date not in aTradingDays:
        end_date = end_date - timedelta(1)
    print(end_date)
    aTradingDays = aTradingDays[aTradingDays.index(start_date):aTradingDays.index(end_date)+1]
    return aTradingDays

print(aTradingDays(start_date,end_date))