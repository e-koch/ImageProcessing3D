#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:23:25 2018

@author: haswani
"""
#closing
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from skimage.morphology import skeletonize,skeletonize_3d
from astropy.io import fits
from skimage.morphology import binary_opening,binary_dilation,binary_erosion,closing,dilation,opening,ball,remove_small_holes

cube = fits.getdata('ngc3627_co21_12m+7m+tp_mask.fits')

selem = ball(3)

dskel = skeletonize_3d(cube)
#print(dskel)
ddilate = dilation(dskel, selem)
dclose = closing(ddilate)
dskel2 = skeletonize_3d(dclose)
remove_holes = remove_small_holes(dskel2)


#dtest = opening(dskel, selem)



#print(cube)



#plotting

import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D


#subcube = remove_holes[15:, 15:45, 15:45]

out = np.where(dskel)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(out[0],out[1],out[2],'r,')


out = np.where(dclose)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(out[0],out[1],out[2],'r,')

out = np.where(dskel2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(out[0],out[1],out[2],'r,')

out = np.where(remove_holes)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(out[0],out[1],out[2],'r,')

#out = np.where(subcube)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(out[0],out[1],out[2],'r,')





plt.show()