#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

filepath = "~/supplier-data/images"
filepath = os.path.expanduser(filepath)

for file in os.listdir(filepath):
 if file[-4:] == "jpeg":
  print("Uploading " + file)
  with open(filepath + '/' + file, 'rb') as opened:
   r = requests.post(url, files={'file': opened})
 else:
  print("Skipping non-jpeg file: " + file)
