#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import glob, os

size = 100, 100

all_images = glob.glob("samples/*.jpg")
total = len(all_images)

for infile in all_images:
    code, _ = os.path.splitext(os.path.split(infile)[-1])
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    mskfile_expert = os.path.join("Segmentation", code + "_expert.png")
    mskfile_novice = os.path.join("Segmentation", code + "_novice.png")
    mskfile = None
    if os.path.exists(mskfile_expert):
        mskfile = mskfile_expert
    elif os.path.exists(mskfile_novice):
        mskfile = mskfile_novice
    if mskfile:
        msk = Image.open(mskfile)
        msk = msk.resize(size)
        msk.save(os.path.join("sampleMasked", code + ".png"), "PNG")
        print(code)
