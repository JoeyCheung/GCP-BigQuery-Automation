#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:28:29 2019

@author: cheungjoey
"""

# --- Delete objects in buckets(blobs), buckets, and tables ---  

from google.cloud import storage

"""Deletes a blob from the bucket."""
storage_client = storage.Client()
bucket = storage_client.get_bucket('bucket_name')
blob = bucket.blob('filename')
blob.delete()
print('Blob {} deleted.'.format('filename'))

"""Deletes a bucket. The bucket must be empty."""
bucket.delete()
print('Bucket {} deleted'.format('bucket_name'))

"""Deletes a table."""
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Set table_id to the ID of the table to fetch.
table_id = 'project_name.dataset_name.table_name'

# If the table does not exist, delete_table raises
# google.api_core.exceptions.NotFound unless not_found_ok is True
client.delete_table(table_id, not_found_ok=True)
print("Deleted table '{}'.".format(table_id))
