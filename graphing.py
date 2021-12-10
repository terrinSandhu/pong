import matplotlib.pyplot as plt
import pyautogui as pg
import cv2 as cv

r = .1
n =  4   

x0 = r
y0 = (2*n-1)*r

fig, ax = plt.subplots()        #init plots

while n > 0:
    x = x0
    for i in range(0,n):
        circle1 = plt.Circle((x, y0), r, color= 'r', fill= False)
        ax.add_patch(circle1)
        x+=(2*r)

    x0+= r
    y0-= (2*r)
    n-=1



plt.show()