#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:21:06 2018

@author: haswani
"""

import cv2
import numpy as np

img_bgr = cv2.imread('bggg.jpg')
#img_bgr = cv2.resize(bigger, (0,0), fx=0.3, fy=0.3) 
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)


template = cv2.imread('templ.jpg',0)
w, h = template.shape[::-1] #template width and height

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

threashold = 0.9

location = np.where(res>=threashold)

#marking on actual picture
for pt in zip(*location[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    
    
small = cv2.resize(img_bgr, (0,0), fx=0.3, fy=0.3) 
cv2.imwrite('resultRectangled.jpg',img_bgr)    

cv2.imshow('detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()    
