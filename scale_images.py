#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import glob, os

size = 100, 100

all_images = glob.glob("Images/*.jpeg")
total = len(all_images)

for infile in all_images:
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im = im.resize(size)
    im.save("sm100x100" + file + ".jpg", "JPEG")
    print(file)
