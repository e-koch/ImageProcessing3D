#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:41:47 2018

@author: haswani
"""
import scipy.ndimage as nd
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

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


footprint=np.ones((3,3,3))

count = nd.generic_filter(dskel2.astype(np.int), np.sum, footprint=footprint)

out = np.where(count)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(out[0],out[1],out[2],'r,')
    