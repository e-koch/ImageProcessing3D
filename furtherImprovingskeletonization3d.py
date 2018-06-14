#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 16:51:55 2018

@author: haswani
"""

import numpy as np
from skimage.morphology import skeletonize,skeletonize_3d
from astropy.io import fits
from skimage.morphology import binary_opening,binary_dilation,binary_erosion,closing,dilation,opening,ball,remove_small_holes

cube = fits.getdata('ngc3627_co21_12m+7m+tp_mask.fits')

selem = ball(3)

#dskel = skeletonize_3d(cube)
#print(dskel)
ddilate = dilation(cube, selem)
dclose = closing(ddilate)
dskel2 = skeletonize_3d(dclose)


#dtest = opening(dskel, selem)
#
##print(dskel)
#ddilate2 = dilation(dskel, cube)
#dclose2 = closing(ddilate2)
#dskel3 = skeletonize_3d(dclose2)

#print(cube)



#plotting

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#subcube = remove_holes[15:, 15:45, 15:45]

out = np.where(dskel2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(out[0],out[1],out[2],'r,')


#out = np.where(dskel3)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(out[0],out[1],out[2],'r,')

#out = np.where(subcube)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(out[0],out[1],out[2],'r,')





plt.show()