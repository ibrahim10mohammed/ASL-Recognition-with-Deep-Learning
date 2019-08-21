# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:03:21 2019

@author: ibrah
"""


from PIL import Image

img = Image.open('A4.jpg') # image extension *.png,*.jpg
new_width  = 50
new_height = 50
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('output image name.png')