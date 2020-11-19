from PIL import Image, ImageFont, ImageDraw
import numpy as np

x = 'Hello There My Name Is'

ShowText = x
font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf', 10) #load the font
size = font.getsize(ShowText)  #calc the size of text in pixels

print(size)
# size = font.getsize("Hello\nhello")
# print(size)

image = Image.new('1', size, 0)  #create a b/w image
draw = ImageDraw.Draw(image)
draw.text((0, 0), ShowText, font=font, fill='white') #render the text to the bitmap
image.save("imgs/test1.jpg")
for rownum in range(size[1]):
#scan the bitmap:
# print ' ' for black pixel and
# print '#' for white one
    line = []
    for colnum in range(size[0]):
        if image.getpixel((colnum, rownum)): line.append(' '),
        else: line.append('#'),
    print (''.join(line))

print(type(image.getdata()))


