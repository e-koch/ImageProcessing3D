#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:41:47 2018

@author: haswani
"""

import numpy as np
from skimage.morphology import skeletonize,skeletonize_3d
from astropy.io import fits
from skimage.morphology import binary_opening,binary_dilation,binary_erosion,closing,dilation,opening,ball,remove_small_holes

cube = fits.getdata('ngc3627_co21_12m+7m+tp_mask.fits')

selem = ball(3)

dskel = skeletonize_3d(cube)
ddilate = dilation(dskel, selem)
dclose = closing(ddilate)
dskel2 = skeletonize_3d(dclose)

import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.show()

xoff, yoff, zoff = np.indices((3,3,3))-1  #gives [-1,0,1] indices in xoff yoff and zoff which will be used for rolling
count = np.zeros_like(dskel2) #returns zero of same dimentions as input array
count.astype(np.int8) #type cast bool to int8 [only 26 neighbour
for x,y,z in zip(xoff.ravel(), yoff.ravel(), zoff.ravel()): #zips x,  y, z
    count += np.roll(dskel2, (x,y,z), axis=(0,1,2)) #Rolling to count neighbour pixels
    
    
#ploting Count
out = np.where(count)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(out[0],out[1],out[2],'r,')
    