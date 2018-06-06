#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:41:29 2018

@author: haswani
"""

#import cv2
#import numpy as np
#import matplotlib.pyplot as plt
#
#img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE) #converted to grayscale - 0  to remove alpha
##other options to read in color ->1 , unchanged->  -1 , or in number
#
#cv2.imshow('image', img)
#cv2.waitKey(0) # wait for a key
#cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#cv2.startWindowThread()
#cv2.namedWindow("preview")
h
#using opencv

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Using metplotlib

#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.show()

#to save image use 

cv2.imwrite('greywatch', img)