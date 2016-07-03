# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 21:56:59 2016

@author: rick
"""
import os
import Image

size = 128, 128

for f in os.listdir('.'):

    im = Image.open(f)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(f, "JPEG")



