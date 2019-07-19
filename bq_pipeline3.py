#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:27:45 2019

@author: cheungjoey
"""

# --- Puts data from GCS bucket into a new table (Done) ---

from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'dataset_name'

dataset_ref = client.dataset(dataset_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV #Replace with avro if you need to
uri = "gs://bucket_name/filename"

load_job = client.load_table_from_uri(
    uri, dataset_ref.table("table_name"), job_config=job_config
)  # API request
print("Starting job {}".format(load_job.job_id))

load_job.result()  # Waits for table load to complete.
print("Job finished.")

destination_table = client.get_table(dataset_ref.table("table_name"))
print("Loaded {} rows.".format(destination_table.num_rows))
