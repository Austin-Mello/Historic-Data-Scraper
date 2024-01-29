#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:19:42 2023

@author: austinmello
"""

from yahoo_fin.stock_info import get_data
import pandas as pd

etfList = ['SPY', 'SPYG', 'SPYV', 'SLY', 'SLYG', 'SLYV', 'XLB', 'XLV', 'XLP',
           'XLY', 'XLE', 'XLF', 'XLI', 'XLK', 'XLU']
start = "01/07/2010"
end = "01/31/2014"

etfRets = pd.DataFrame()

for i in etfList:
    etf = get_data(i,start_date=start, end_date=end)
    etfRets[i] = etf.close.pct_change()

print(etfRets)
etfRets.to_csv('E_Rets.csv')