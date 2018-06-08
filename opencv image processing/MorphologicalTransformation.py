#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:55:55 2018

@author: haswani
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(1):

    _, frame = cap.read() #Read from webacm
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Using HSV model
    
    lower_red = np.array([30,150,50]) #Since extracting red color from video
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5),np.uint8) 
    
    erosion = cv2.erode(mask,kernel,iterations = 1) #erodes pixels in specified frame
    dilation = cv2.dilate(mask,kernel,iterations = 1) #dilates pixels in specified frame

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #removes noise from backfround
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #removes noise within image

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()