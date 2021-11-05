#!/usr/bin/python
import numpy as np
import cv2 as cv
import sys

def minmax_rgb(i, w, h, m):
    x = 0
    minmax = 0
    while x < h:
        y = 0
        while y < w:
            if m == 'min':
                minmax = min(i[x][y][0],i[x][y][1],i[x][y][2])
            else:
                minmax = max(i[x][y][0],i[x][y][1],i[x][y][2])
            if minmax == i[x][y][0]: # blue is least
                i[x][y][1] = 0
                i[x][y][2] = 0 
            if minmax == i[x][y][1]: # green is least
                i[x][y][0] = 0
                i[x][y][2] = 0
            if minmax == i[x][y][2]: # red is least       
                i[x][y][0] = 0
                i[x][y][1] = 0
            y+=1
        x+=1 
    return i
    
def sobel(i, k):
    # the general convention is to use a gaussian blur on the image, 
    # but the pixelization should take care of that here.
    sobx = cv.Sobel(i,cv.CV_16S,1,0,ksize=k,scale=1,delta=0)
    soby = cv.Sobel(i,cv.CV_16S,0,1,ksize=k,scale=1,delta=0)
    abSobx = cv.convertScaleAbs(sobx) # makes the sobels absolute
    abSoby = cv.convertScaleAbs(soby)
    # approximates the sobel algo
    sobtot = cv.addWeighted(abSobx, 0.5, abSoby, 0.5, 0)  
    cv.imshow('sobel\'d', sobtot)
    cv.waitKey(0)
    cv.destroyAllWindows()

k = 3
mode = 'min'
if len(sys.argv) > 3:
    k = int(sys.argv[2])
    if k%2 == 0:
        print("Error: k must be odd.")
        sys.exit(1)
    if k > 31:
        print("Error: k must be less than 32")
        sys.exit(1)
    mode = sys.argv[3]
    if mode != 'min' or mode != 'max':
        print("Error: third flag must be \"min\" or \"max\"")
        sys.exit(1)
try:
   i = cv.imread(sys.argv[1])
   hig, wid, _ = i.shape
except:
    print("Error: image does not exist")
    sys.exit(1)
j = minmax_rgb(i, wid, hig, mode)
sobel(i, k)
