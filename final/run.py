#! /usr/bin/env python3

import os
import requests

filepath = "~/supplier-data/descriptions"
filepath = os.path.expanduser(filepath)

filenames = os.listdir(filepath)

if __name__ == "__main__":
 for file in filenames:
  item_info = {}
  with open(filepath + '/' + file) as item:
   item_info["name"] = item.readline().rstrip()
   item_info["weight"] = int(item.readline().split(' ')[0])
   item_info["description"] = item.readline().rstrip()
   item_info["image_name"] = file[:-4] + ".jpeg"

  response = requests.post("http://34.71.18.218/fruits/", json=item_info)
  if response.status_code == 201:
   print("Post for file " + file + " was successful.")
  else:
   print("Post for file " + file + " occurred with error " + str(response.status_code) + ".")
