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
        'metric':["VOLUME", "REVENUE", "GRATE"]}

# Sneak peek at first 3 lines of data from CSV
#print(data.head(3))

"""
# Not needed, just printing data to see how the computer stores it
for key, value in data.iterrows():
    print(key, value)
    print()
"""

# Create data objects for each metric from source
data_vol = data[(data['Metric'] == "VOLUME")]
data_rev = data[(data['Metric'] == "REVENUE")]
data_gra = data[(data['Metric'] == "GRATE")]
data_time =  data['Time'].unique()
data_comp = data['Company'].unique()

# Again, print statements are not needed, just seeing what it looks like
"""
print(data_vol)
print()
print(data_time)
print(data_comp)
#df = pd.DataFrame(dict)
#print(df)
"""

## MatPlotLib instructions begin here
# End goal https://i.stack.imgur.com/xaSdU.png
"""
I don't know matplotlib well.  The pseudo-code below might
not be the best method for matplotlib
YMMV

If the data being printed from below code looks good then
you can plug that into matplotlib.  If data needs formatting
we should fix that first.
"""
# FOR each time period IN total unique time values from data.csv
# (Q1'18), (Q2'18), (Q3'18), etc...
for quarter in data_time:
    # Print all data per type (VOL,REV,GRA), per quarter
    print("Time period: " + quarter)
    print(data_vol[(data_vol['Time'] == quarter)])
    print(data_rev[(data_rev['Time'] == quarter)])
    print(data_gra[(data_gra['Time'] == quarter)])
    print()


