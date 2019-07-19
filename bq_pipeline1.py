#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:27:17 2019

@author: cheungjoey
"""

# --- Uploads avro file from DNA to a bucket in GCS (Done) ---

from google.cloud import storage

"""Uploads a file to the bucket."""
storage_client = storage.Client()
bucket = storage_client.get_bucket('bucket_name')
blob = bucket.blob('filename') # Figure out how to add 2 files
blob.upload_from_filename('filename') # Figure out how to add 2 files
print("File uploaded to bucket")
