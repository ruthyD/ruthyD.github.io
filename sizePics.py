# -*- coding: utf-8 -*-
"""
@author: rick
"""
import os
import Image

size = 128, 128

for f in os.listdir('.'):

    im = Image.open(f)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(f, "JPEG")



