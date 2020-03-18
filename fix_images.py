#!/usr/bin/python3

from PIL import Image
import os

path = 'images'
new_path = '/opt/icons'
filenames = os.listdir(path)

for file in filenames:
 try:
  img = Image.open(path + '/' + file)
  img.rotate(-90).resize((128,128)).convert("RGB").save(new_path + '/' + file, format="jpeg")
  print("Writing new image: " + new_path + '/' + file)
  img.close()
 except:
  print("Skipping " + path + '/' + file)
