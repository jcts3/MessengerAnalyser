#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:59:14 2018

@author: jamesstratford
"""

import graphs
import pandas as pd

dfc = pd.read_csv('../csv/chatdata.csv')
a,b,c = graphs.getTimePersonValues(dfc)
print('bla')
d,e=graphs.getTimeValues(dfc)
