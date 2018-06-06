#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:28:52 2018
2nd tutorial
@author: haswani
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0) #: to use webcam 0,1,2 number of webcam

#to save 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', forcc, 20.0, (640,480))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray) # modified video
    
    #TERMINATING CONDTION
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release() #stop recording
out.release() #saving video
cv2.destroyAllWindows()    
    