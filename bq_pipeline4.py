#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:28:05 2019

@author: cheungjoey
"""

# --- Queries the table that was just created and store into csv (Done) ---
from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT body FROM `project_name.dataset_name.table_name` '
    'LIMIT 10')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

data = []

# this takes all of the queried columns and appends to a list
for row in rows:
    data.append("insert column name")
    
print(data)

# Stores list into a csv file
import pandas as pd
import numpy as np

pd_data = pd.read_csv("data.csv")
old_data = pd_data.values # numpy array

new_data = np.asarray(data) # New rows that I want to add

combinedData = np.row_stack((old_data, new_data[:,None]))
combinedData = pd.DataFrame(combinedData)
combinedData.to_csv('combinedData.csv', encoding='utf-8', index=False, header=None)
print("New data downloaded into a csv format")
