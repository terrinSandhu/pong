import matplotlib.pyplot as plt
import pyautogui as pg
import cv2 as cv
from PIL import Image

img_path = "C:\\Users\\tssan\\Documents\\GitHub\\pong\\images.jpg"

im = Image.open(img_path)
width, height = im.size
if width > height:
    height = width


n =  4 
r = abs(height/(n*2))
  
x0 = r
y0 = (2*n-1)*r


fig, ax = plt.subplots()  
img = plt.imread(img_path)

while n > 0:
    x = x0
    for i in range(0,n):
        circle1 = plt.Circle((x, y0), r, color= 'r', fill= False)
        ax.add_patch(circle1)
        x+=(2*r)

    x0+= r
    y0-= (2*r)
    n-=1

ax.imshow(img)
plt.axis("off")
plt.show()
