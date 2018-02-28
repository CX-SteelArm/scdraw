#coding:utf-8

from PIL import Image,ImageDraw,ImageFont,ImageColor
from conf import *
from math import ceil

# tag color, white or black
if TAG_COLOR == 'w':
	color = '#ffffff'
elif TAG_COLOR == 'b':
	color = '#000000'
else:
	color = TAG_COLOR

font = ImageFont.truetype('arial.ttf',TAG_SIZE)

imageNumber = len(SRC)

if not ONEROW:
	rows = ceil(imageNumber/2.)
else:
	rows = 1

# calc the positions of images
def calcPos(n,x,y,gap):
	if rows == 1:
		return (n*x+int(n*gap*x), 0)
	else:
		a = (n%2)*(1+gap)*x
		if n < 2: b = 0
		else: b = y+x*gap*(n/2)
		return (int(a),int(b))

# open an image to get the size
im = Image.open(SRC[0])
print(rows, im.size)
x,y = im.size
del im

if rows == 1:
	newim = Image.new(mode='RGB',size=(imageNumber*x+int((imageNumber-1)*GAP*x),y),color='#ffffff')
else:
	newim = Image.new(mode='RGB',size=(int((2+GAP)*x),int(y*rows+(rows-1)*GAP*x)),color="#ffffff")

for e,i in enumerate(SRC):
	img = Image.open(i)
	draw = ImageDraw.Draw(img)
	if BOX:
		w, h = font.getsize('(..)');
		draw.rectangle([0, 0, w, h], '#ffffff');
	draw.text((0,0),"("+chr(97+OFFSET+e)+")",font=font,fill=color)
	newim.paste(img,box=calcPos(e,x,y,GAP))
	del draw,img

newim.show()

S = raw_input("Save or not ?(y/n):")
if S == "y":
	newim.save(OUTPUT, format='JPEG')