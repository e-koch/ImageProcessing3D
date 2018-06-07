#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 18:35:38 2018

@author: haswani
"""

import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

add = img1+img2

add2 = cv2.add(img1, img2) #add all the pixels

weighted = cv2.addWeighted(img1 , 0.6 ,img2 , 0.4 , 0) #image, weight, image , weight,  gamma value

#using logical operations

img3 = cv2.imread('mainlogo.png')

#putting logo in right top corner

rows,cols,channels = img3.shape
roi = img1[0:rows,0:cols]

#creating mask

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 220, 255 , cv2.THRESH_BINARY_INV) #THRESHHOLDING ABOVE 220 -> 255 AND BELOW IT TO BLACK , THRESH_BINARY_INV : ENDING UP INVERSING  IT


#removing white from img3 

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('mask', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
 