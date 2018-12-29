#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:33:08 2018

@author: jamesstratford
"""

import pandas as pd
#import datetime
import numpy as np
import matplotlib.pyplot as plt
#import csv


def getTimeValues(dfrg):
    dfData = dfrg
    
    dfData['Date'] = pd.to_datetime(dfData.Date)
    datesData = dfData.groupby(dfData.Date).size()
    #datesData.sort_values('Date')
    dates = datesData.index
    counts = datesData.values
    return dates, counts

def getTimePersonValues(dfr):
    dfPData = dfr
    
    dfPData['Date'] = pd.to_datetime(dfPData.Date)
    datesPivot = dfPData.pivot_table(index='Date',columns='Person', aggfunc=len)
    dates = datesPivot.index
    person1 = datesPivot.ix[:,0]
    person2 = datesPivot.ix[:,1]
    return dates, person1, person2
    #datesPData.plot.area()

def stackPlot(x,y1,y2):
    plt.stackplot(x, y1, y2)
    plt.show()
    
    