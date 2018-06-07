#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:07:59 2018
Drawing using opencv
@author: haswani
"""
import numpy as np 
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150) , (255,0,0)) #where,start pt, end pt , color ,  (optional)width
#(more color the brighter  it is  opencv BGR) for black - all zero

cv2.rectangle(img , (0,0), (50,50), (255,255,255))

cv2.circle(img , (100,45), 55, (0,0,255) , -1) # where, center, radius, color, -1:fills circle

#polygons

pts = np.array([[10, 5],[10, 2],[16,15],[50,10],[20,15]], np.int32)
pts = pts.reshape((-1,1,2)) #resize re shape
cv2.polylines(img , [pts], True, (0,255,255), 3) # true is to for a close polygon

#typing
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV ', (0,130), font, 1, (200,150,150), 2, cv2.LINE_AA) #img , text, starting pt , font , size ,color /, thickness


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



