#!/usr/bin/env python
# coding: utf-8

from PIL import Image;
import numpy as np;
from conf import *;

_im = Image.open(INPUTFILE, 'r');

im = _im.crop(CROPAREA);

n = np.array(im.getcolors());

mask = THRESHOLD > n[:, 1];

areaFraction = sum(n[:, 0][mask]) / float(sum(n[:, 0]));

print(areaFraction);


