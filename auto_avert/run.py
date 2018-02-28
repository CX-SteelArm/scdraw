#!/usr/bin/env python
# coding: utf-8

import PIL
from PIL import Image, ImageDraw, ImageColor, ImageFont 

import sys

def vectorMinus(v1, v2):
	return (v1[0]-v2[0], v1[1]-v2[1]);

im = Image.open(r"C:\Users\Administrator\Desktop\Al\pil\auto_alert\bg-simple.png");

draw = ImageDraw.Draw(im);
draw.rectangle((500, 30) + vectorMinus(im.size, (20,10)), "#cccccc");

font = ImageFont.truetype("arial.ttf", 15);
print(draw.textsize("world", font=font))
draw.text((500, 30), "world", "#000000", font=font);

del draw;

# write to stdout
im.show();