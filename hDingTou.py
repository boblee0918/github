# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:39:26 2016

@author: Administrator
"""

import pandas as pd
from pandas import DataFrame
import datetime
from datetime import datetime,timedelta,time
#from dateFromStr import dateFromStr
import numpy as np
import matplotlib.pyplot as plt
import pylab

#from matplotlib import pylab


listH = [u'HK2318', u'HK0700', u'HK1788', u'HK2883', u'HK0806', u'HK1211', u'HK3968']
lotH = [500,100,1000,2000,1000,500,500,0]
commissionH = 0.004
commissionA = 0.00225
taxA = 0.001
result = pd.DataFrame(columns = ['test','stock','startDate','endDate','tradeDate',\
'price','trade','hold','commission','invested','cash','portValue','span','step','initRate',\
'lotRate','increment','returns','buyHold','hsiReturn','HSI','cashFlow','targetValue','lotMoney'])


hClosePx = pd.read_csv(u'C:/Users/Administrator/Documents/PythonScripts/hClosePx.csv',parse_dates=True)
hClosePx['date']=pd.to_datetime(hClosePx['date'])

hIsTrading = pd.read_csv(u'C:/Users/Administrator/Documents/PythonScripts/hIsTrading.csv',encoding='gbk',parse_dates=True)
hIsTrading['date']=pd.to_datetime(hIsTrading['date'])
hIsTrading.fillna(value='N',inplace=True)

investment = 1000000
initRate = 0.3
hold = 0
portValue = 0
lotRate = 0.02
increment = 0.02
#increase = 0.02
k = 1


startDate = "2010-09-30"
startDate = datetime.strptime(startDate,'%Y-%m-%d')
finalDate = hClosePx.ix[hClosePx.last_valid_index()]['date']
targetValue = investment*initRate + investment*increment
span = 3000
step = 20

i = 6
test = int(1)


def trade(date,lotMoney,lastCash):
    global hold,portValue,lastDate,targetValue,k,holdValue,cash,hold
    price = hClosePx.loc[hClosePx.date == date][listH[i]].values[0]
    trade = lotMoney/price
    trade = int(round((trade/lotH[i])))*lotH[i]
    commission = commissionH*trade*price
    if commission < 0:
        commission = - commission



    invested = trade*price + commission
    cash = lastCash - invested
    hold = hold + trade
    portValue = hold*price + cash
    pxIndex = hClosePx[hClosePx.date ==date].index.values[0]
    HSI = hClosePx['HSI'].iloc[pxIndex]
    
    

    result1 = pd.Series([test, listH[i],date,date,price,trade,hold,commission,span,step,initRate,\
    lotRate,increment,invested,cash,portValue,HSI,targetValue,lotMoney], ['test','stock','startDate',\
    'tradeDate','price','trade','hold','commission','span','step','initRate',\
    'lotRate','increment', 'invested','cash','portValue','HSI','targetValue','lotMoney'])
#    if result1
    global result
    result = result.append(result1,ignore_index=True)
    targetValue = targetValue + investment*increment*(1+0.02*k)
    k= k + 1
    lastDate = date

    return


def otherTrade():
    global startDate,investment,initRate,step,span,lastDate,hold,\
    cash,finalDate,investment,result,targetValue,portValue,holdValue,k

    while True:
        lastDateIndex = hClosePx[hClosePx.date ==lastDate].index.values[0]
        startDateIndex = hClosePx[hClosePx.date ==startDate].index.values[0]


        if lastDateIndex >= startDateIndex + span or hClosePx.index.max() <=lastDateIndex + step or lastDate >= finalDate:  #or cash<20000:
            endDate = lastDate
            endDateIndexR = result[result.tradeDate ==endDate].index.values[0]
            startDateIndexR = result[result.tradeDate ==startDate].index.values[0]
            returns = result['portValue'].iloc[endDateIndexR]/investment-1
            hsiReturn = result['HSI'].iloc[endDateIndexR]/result['HSI'].iloc[startDateIndexR]-1
            buyHold = result['price'].iloc[endDateIndexR]/result['price'].iloc[startDateIndexR]-1
            print 'portReturn:',"%0.2f%%"%(returns*100),'HSI:',"%0.2f%%"%(hsiReturn*100),'buyHold:',"%0.2f%%"%(buyHold*100)
            result.set_value(endDateIndexR,'endDate',endDate)
            result.set_value(endDateIndexR,'returns',returns)
            result.set_value(endDateIndexR,'buyHold',buyHold)
            result.set_value(endDateIndexR,'hsiReturn',hsiReturn)
#            print('otherTrade finished!')
            return

        else:
            tradeDate = hClosePx['date'].iloc[lastDateIndex+step]
            holdValue = hold*hClosePx.loc[hClosePx.date == tradeDate][listH[i]].values[0]
            
            targetCash = targetValue - holdValue
#            print('cash: ',cash,'targetValue: ',targetValue,'targetCash: ',targetCash)
            if hIsTrading.loc[hIsTrading.date == tradeDate][listH[i]].any() == u'Y':
                trade(tradeDate,targetCash,cash)
#                print(tradeDate)
                lastDate = tradeDate
                tradeDateIndex = hClosePx[hClosePx.date ==tradeDate].index.values[0]
#                print('otherTraded Started!')
            else:
                 lastDate = hClosePx['date'].iloc[tradeDateIndex+1]



trade(startDate,targetValue,investment)

#print('first trade finished')
#print(lastDate)
otherTrade()
#print(result)
result.set_index('tradeDate',inplace=True)
r1 = result.portValue[:]/result.portValue[0]-1
r5 = result.invested[:]/result.portValue[0]

r2 = result.cash[:]/investment
r3 = result.HSI[:]/result.HSI[0]-1
r4 = result.price[:]/result.price[0]-1
returns = pd.concat([r1,r2,r3,r4,r5],axis=1)
s=' / '
returns.plot(figsize=(18,8),title = listH[i]+s+returns.index.min().strftime('%Y-%m-%d')+s+\
 returns.index.max().strftime('%Y-%m-%d'),legend=True,label=result.index[0],linewidth = 4)

print 'invested min:',"{0:,.0f}".format(result.invested.min())
print 'invested max:',"{0:,.0f}".format(result.invested.max())
print 'cashPct min:',"%0.2f%%"%(result.cash.min()/investment)
print 'portPct min:',"%0.2f%%"%(returns.portValue.min()*100)
print 'portPct max:',"%0.2f%%"%(returns.portValue.max()*100)
print 'portPct end:',"%0.2f%%"%(returns.portValue.values[-1]*100)
print 'pricePct end:',"%0.2f%%"%((result.price[-1]/result.price[0]-1)*100)

#targetValue
returns.dropna(inplace=True)
covmat = np.cov(returns.portValue,returns.HSI)
beta = covmat[0,1]/covmat[1,1]
prd = 12
alpha= np.mean(returns.portValue)-beta*np.mean(returns.HSI)
alpha= np.mean(returns.portValue)-beta*np.mean(returns.HSI)*prd
volatility = np.sqrt(covmat[0,0])
volatility = volatility*np.sqrt(prd)
print 'alpha:',"%0.0f%%"%(alpha*100),'beta:',"%0.0f%%"%(beta*100),'volatility',"%0.0f%%"%(volatility*100)

