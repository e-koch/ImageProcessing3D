#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:40:37 2018

@author: haswani
"""

import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) # below 12 is black,maxval - 255

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

#adaptive threshold

gaus = cv2.adaptiveThreshold(grayscaled, 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155 ,1)

cv2.imshow('Original',img)
cv2.imshow('Threshold Color', threshold)
cv2.imshow('Threshold Greyscale', grayscaled)
cv2.imshow('threshold gausian',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()