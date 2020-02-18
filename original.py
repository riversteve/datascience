# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:51:34 2020

@author: kevin.g
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#IMPORT THE CSV
comp_data = pd.read_csv('C:/Users/kevin.g/Desktop/Competitive Analysis Python.csv')


#CHANGE THE PERCENTAGE COLUMN TO PERCENTAGE TYPES

comp_data['Revenue Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in comp_data['Revenue Percentage']], index = comp_data.index)

comp_data['Volume Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in comp_data['Volume Percentage']], index = comp_data.index)

comp_data['GRATE Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in comp_data['GRATE Percentage']], index = comp_data.index)

barWidth = 0.25


bars1 = comp_data['Volume Percentage']
bars2 = comp_data['Revenue Percentage']
bars3 = comp_data['GRATE Percentage']

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Volume')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Revenue')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='GRATE')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['Q4 2018', 'Q1 2019', 'Q2 2019', 'Q3 2019', 'Q4 2019'])

# Create legend & Show graphic
plt.legend()
plt.show()
