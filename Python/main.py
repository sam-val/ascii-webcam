import cv2.cv2 as cv2
import time
import numpy as np
from PIL import Image, ImageFont, ImageDraw

def string_to_image_data(str, width, height):
    global font
    line_str = str[:width]
    line_w, line_h = font.getsize(line_str)
    # make a plain black image...
        # calculate the height - in advance:
    new_line_distance = line_h/1.5
    img = Image.new(mode='L',size=(line_w, int(new_line_distance*height)),color=0)
    draw = ImageDraw.Draw(img)

    for i in range(height):
        draw.text((0,i*new_line_distance),str[i*width:i*width + width], font=font, fill="white")

    return np.asarray(img)

def make_ascii_string(gray_img_data):
    # gray_ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    gray_ramp = "@%#*+=-:. "
    ramp_length = len(gray_ramp)
    rs = ''

    ### convert gray-scale data into one single string:
    for j in gray_img_data:
        rs += ''.join([gray_ramp[int(j / (256 / ramp_length))]])

    return rs


font = ImageFont.truetype('CourierScreenplay.ttf', 15) #load the font

capture = cv2.VideoCapture(0)

width, height = 1200, 900
RESIZE_AMOUNT = 15
width, height = width // RESIZE_AMOUNT, height // RESIZE_AMOUNT
capture.set(3, width)  ## set '3': the width
capture.set(4, height)  ## set '4': the height
while (True):
    # Capture fram by frame
    ret, frame = capture.read()


    # Process the image/frame
    mirror_framed = cv2.flip(frame, 1)
    gray = cv2.cvtColor(mirror_framed, cv2.COLOR_BGR2GRAY) # this an numpy array

    ### resize to a smaller resolution to work with ASCII
    resized_gray = cv2.resize(gray, (width,height)).flatten()

    # Display the resulting frame

    key = cv2.waitKey(1)
    ### convert the RESIZED_GRAY IMAGE DATA => An ascii string
    ascii_string = make_ascii_string(resized_gray)
    ascii_img = string_to_image_data(ascii_string, width, height)
    ascii_img = ascii_img.astype(np.uint8) ### this is to make it compatible with the imshow() 'mat' param
    cv2.imshow(winname='frame', mat=ascii_img)
    cv2.imshow(winname='gray', mat=gray)

    if key == ord("q"):
        break

    time.sleep(1/24)

capture.release()
cv2.destroyAllWindows()

