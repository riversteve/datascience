#!/bin/python3

## Source https://www.geeksforgeeks.org/iterating-over-rows-and-columns-in-pandas-dataframe/
"""
Data example

Company,Metric,Time,Percentage
KOIPOND,VOLUME,Q4 2018,2.18%
KOIPOND,REVENUE,Q4 2018,-0.11%
KOIPOND,GRATE,Q4 2018,17.91%
CHEW,VOLUME,Q4 2018,-1.50%
CHEW,REVENUE,Q4 2018,18.35%
CHEW,GRATE,Q4 2018,20.94%
TANGO,VOLUME,Q4 2018,0.00%
TANGO,REVENUE,Q4 2018,6.44%
TANGO,GRATE,Q4 2018,6.48%
"""
## importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## importing data
data = pd.read_csv("data.csv")

## dictionary of lists
# Not currently used
dict = {'company':["KOIPOND", "CHEW", "TANGO"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

print(data.head(3))

for key, value in data.iterrows():
    print(key, value)
    print()

# Create data objects for each metric from source
data_vol = data[(data['Metric'] == "VOLUME")]
data_rev = data[(data['Metric'] == "REVENUE")]
data_gra = data[(data['Metric'] == "GRATE")]
data_time =  data['Time'].unique()

print(data_vol)
print()
print(data_time)
#df = pd.DataFrame(dict)
#print(df)
