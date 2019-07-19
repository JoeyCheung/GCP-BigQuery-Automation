#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:57:29 2019

@author: cheungjoey
"""

import pandas as pd

pd_data = pd.read_csv("filename.csv")

pd_data.shape # This shows the size of columns and rows of file

size = 2000 
rows = []

for i in range(size):
    rows.append("1")

# Inserts at first position with a column named Label and length of the variable called rows
pd_data.insert(0, "Label", rows, True) 

# This is for partitioning a file with 2000 rows into 1/3 for each file
pd_data1 = pd_data.iloc[:666,:]
pd_data2 = pd_data.iloc[667:1333,:]
pd_data3 = pd_data.iloc[1334:2000,:]

pd_data1.to_csv("filename1.csv", encoding='utf-8', index=False, header=None)
pd_data2.to_csv("filename2.csv", encoding='utf-8', index=False, header=None)
pd_data3.to_csv("filename3.csv", encoding='utf-8', index=False, header=None)
