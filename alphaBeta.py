# -*- coding: utf-8 -*-
"""
Created on Sun May 08 23:18:40 2016

@author: Administrator
"""

from pandas.io.data import DataReader
from datetime import date
import numpy as np
import pandas as pd

# Grab time series data for 5-year history for the stock (here AAPL)
# and for S&P-500 Index
sdate = date(2010,12,31)
edate = date(2016,4,30)
df = DataReader('GOOG','yahoo',sdate,edate)
dfb = DataReader('^GSPC','yahoo',sdate,edate)