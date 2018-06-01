#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:58:28 2018

@author: haswani
"""
import scipy
from scipy import ndimage
import numpy as np

a = np.array([[0,1,0,0],
             [0,1,0,0],
             [0,1,1,0],
             [1,0,0,0]])
structure = np.array([[1,1,0]])
#ndimage.binary_erosion(a).astype(a.dtype)

#Erosion removes objects smaller than the structure
print(ndimage.binary_erosion(a, structure).astype(a.dtype))
