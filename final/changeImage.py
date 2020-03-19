#!/usr/bin/env python3

from PIL import Image
import os

filepath = "~/supplier-data/images"
filepath = os.path.expanduser(filepath)

if __name__ == "__main__":
 filenames = os.listdir(filepath)
 for file in filenames:
  if file[-4:] != "tiff":
   print("Skipping non-tiff file " + file)
  else:
   img = Image.open(filepath + '/' + file)
   img.resize((600,400)).save(filepath + '/' + file[:-5] + '.jpeg')

