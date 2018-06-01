#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:27:14 2018

@author: haswani
"""
import scipy
from scipy import ndimage
import numpy as np


a = np.zeros((5, 5))
a[2, 2] = 1

ndimage.morphology.binary_dilation(a)

ndimage.morphology.binary_dilation(a).astype(a.dtype)

# 3x3 structuring element with connectivity 1, used by 

struct1 = ndimage.generate_binary_structure(2, 1)

# 3x3 structuring element with connectivity 2
struct2 = ndimage.generate_binary_structure(2, 2)

test1 = ndimage.binary_dilation(a, structure=struct1).astype(a.dtype)

test2 = ndimage.binary_dilation(a, structure=struct2).astype(a.dtype)

print(test1)
print(test2)
