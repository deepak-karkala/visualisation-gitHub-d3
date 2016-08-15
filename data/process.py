# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:26:14 2016
Compute total number of forks in top 100 repositories for each year.
@author: nesara
"""
import pandas as pd

totalForks = {}
filename = ['gitHubTop100Fork2011.csv','gitHubTop100Fork2012.csv',\
    'gitHubTop100Fork2013.csv','gitHubTop100Fork2014.csv','gitHubTop100Fork2015.csv']

for i in range(5):
    data=pd.read_csv(filename[i])
    totalForks[i] = sum(data['num'])