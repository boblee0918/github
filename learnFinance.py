# -*- coding: utf-8 -*-
"""
Created on Thu May 05 23:05:56 2016

@author: Administrator
"""

import datetime

import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl

aapl = pd.io.data.get_data_yahoo('AAPL', 
                                 start=datetime.datetime(2006, 10, 1), 
                                 end=datetime.datetime(2012, 1, 1))

import pylab
pylab.show()

from IPython.core.display import Image 
Image("http://cdn.meme.li/instances/300x300/39833146.jpg")


import pandas as pd
import pandas.io.data
import numpy as np

import pytz
from datetime import datetime

import zipline as zp

from zipline.finance.slippage import FixedSlippage