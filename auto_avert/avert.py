#!/usr/bin/env python
# coding: utf-8

from PIL import Image, ImageDraw, ImageColor, ImageFont 
from conf import *

# open the image & get the size
_im = Image.open(INPUTFILE);
if _im.mode <> "RGB":
	_im = _im.convert(mode="RGB");
im = _im.crop(STARTPOINT + (STARTPOINT[0]+WIDTH, STARTPOINT[1]+HEIGHT))
draw = ImageDraw.Draw(im);

# The supplyments are a scale bar, a textbox and a rectangle container
# get the position of the scale bar
class ScaleBar(object):
	def __init__(self):
		self.length = SC_LENGTH * SC_RATIO;
		self.width = HEIGHT / 50;
		self.x = WIDTH - self.length - MG_RIGHT - PD_HOR;
		self.y = HEIGHT - self.width - MG_BOTTOM- PD_VERT;
		self.x0 = self.x + self.length;
		self.y0 = self.y;

# get the position of the textbox
class TextBox(object):
	def __init__(self):
		sb = ScaleBar();
		self.text = str(SC_LENGTH) + ' ' + UNIT; # displaying text
		self.sb = sb;
		for i in range(10,100):
			font = ImageFont.truetype("arial.ttf", i);
			l = draw.textsize(self.text, font=font);
			if l[0] >= sb.length or i == 99:
				self.font = ImageFont.truetype("arial.ttf", i/5*4);
				break;
		self.width, self.height = draw.textsize(self.text, font=self.font);
		self.x = sb.x + (sb.length-self.width) / 2;
		self.gap = GAP; # the gap between textbox and scalebar
		self.y = sb.y - self.gap - self.height;

# and the container
class Container(object):
	def __init__(self):
		tb = TextBox();
		self.x = tb.sb.x - PD_HOR;
		self.y = tb.y - PD_VERT;
		self.x0 = WIDTH - MG_RIGHT;
		self.y0 = HEIGHT - MG_BOTTOM;
		
sb = ScaleBar();
tb = TextBox();
ct = Container();

draw.rectangle((ct.x, ct.y, ct.x0, ct.y0), "#ffffff");
draw.line((sb.x, sb.y, sb.x0, sb.y0), fill="#000000", width=sb.width);
draw.text((tb.x, tb.y), tb.text, "#000000", font=tb.font);
del draw;

im.show();

S = raw_input("Save or not ?(y/n):");
if S == "y":
	im.save(INPUTFILE + ".jpg", format="JPEG");