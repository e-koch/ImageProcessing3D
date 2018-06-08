#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:04:32 2018

@author: haswani
"""

import cv2
import numpy as np 

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

laplacian = cv2.Laplacian(img, cv2.CV_64F) # CV_64F is just data type
#adding x and y gradient

sobelx = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=5) #ksize = kernel size
sobely = cv2.Sobel(img , cv2.CV_64F, 0, 1, ksize=5)

#using edge detectors

edges = cv2.Canny(img, 160 , 160)

cv2.imshow('original',img)
cv2.imshow('laplacian',laplacian)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('Canny',edges)






cv2.waitKey(0)
cv2.destroyAllWindows()
