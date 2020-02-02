import sys
import os
from PIL import Image

source_folder =  sys.argv[1]
destination_folder =  sys.argv[2]

if not os.path.exists(destination_folder):
  os.makedirs(destination_folder)

for i in os.listdir(source_folder):
  if i[-3:] == 'jpg' or i[-4:] == 'jpeg':
    img = Image.open(f'{source_folder}{i}')
    img.save(f'{destination_folder}{os.path.splitext(i)[0]}.png', 'png')
