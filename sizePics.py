# -*- coding: utf-8 -*-
"""
@author: rick
"""
import os
from PIL import Image
#
# size = 400, 400
#
# for f in os.listdir('./img/work/full/'):
#     print(f)
#
#     im = Image.open(f"./img/work/full/{f}")
#     im.thumbnail(size, Image.ANTIALIAS)
#     im.save(f"./img/work/thumbs/{f}", "JPEG")


size = 400, 400

for f in os.listdir('./img/work/full/'):
    print(f)

    im = Image.open(f"./img/work/full/{f}")
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(f"./img/work/google/{f}", "JPEG")

