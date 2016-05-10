# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:55:59 2016

@author: Administrator
"""

from datetime import datetime
def dateFromStr(string):
    temp = datetime(int(string[:4]),int(string[5:7]),int(string[8:10]))
    return temp.date()

#date = dateFromStr("2010-08-31 15:00:00.0000")
#j = date == datetime(2010,8,31).date()



#print(date,j)

