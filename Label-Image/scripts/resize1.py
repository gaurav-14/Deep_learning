import os
import getopt
import sys
from PIL import Image

width = 600
height = 600
directory = '../Images/003'

for image in os.listdir(directory):
    print('Resizing image ' + image)
 
    # Open the image file.
    img = Image.open(os.path.join(directory, image))
 
    # Resize it.
    img = img.resize((width, height), Image.BILINEAR)
 
    # Save it back to disk.
    img.save(os.path.join(directory,image))
 
print('Batch processing complete.')
