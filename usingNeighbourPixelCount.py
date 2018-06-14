#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:41:14 2018

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



xoff, yoff, zoff = np.indices((3,3,3))-1  #gives [-1,0,1] indices in xoff yoff and zoff which will be used for rolling
count = np.zeros_like(dskel2) #returns zero of same dimentions as input array
count.astype(np.int8) #type cast bool to int8 [only 26 neighbour
for x,y,z in zip(xoff.ravel(), yoff.ravel(), zoff.ravel()): #zips x,  y, z
    count += np.roll(dskel2, (x,y,z), axis=(0,1,2)) #Rolling to count neighbour pixels
    
#for x,y,z in zip(xoff.ravel(), yoff.ravel(), zoff.ravel()): #zips x,  y, z
#    if np.roll(count, (x,y,z), axis=(0,1,2)) > 3: #Rolling to count neighbour pixels counting if pixels > 3
#        print(x)
#    

#creating mylist containing the cordinates of neighbour pixels with then 2 neighbour pixels

    
mylist = []       

for index, x in np.ndenumerate(count):
    if x>3:
        mylist.append(index)
        
#print(mylist[3])        
#(50, 313, 152)
        
#print(mylist[3][0])
#50
        
#using subcube to represent the image of the subpart of the cube containing pixel with > 2 neighbours

xi = mylist[15][0]
yi = mylist[15][1]
zi = mylist[15][2]


plt.imshow(dskel2[xi-2,yi-20:yi+20,zi-20:zi+20])
plt.figure()
plt.imshow(dskel2[xi-1,yi-20:yi+20,zi-20:zi+20])
plt.figure()
plt.imshow(dskel2[xi,yi-20:yi+20,zi-20:zi+20])
plt.figure()
plt.imshow(dskel2[xi+1,yi-20:yi+20,zi-20:zi+20])
plt.figure()
plt.imshow(dskel2[xi+2,yi-20:yi+20,zi-20:zi+20])
plt.figure()




#plt.imshow(dskel2[xi-1,yi-20:yi+20,zi-20:zi+20])
#plt.imshow(dskel2[xi,yi-20:yi+20,zi-20:zi+20])
#plt.imshow(dskel2[xi+1,yi-20:yi+20,zi-20:zi+20])
#plt.imshow(dskel2[xi+2,yi-20:yi+20,zi-20:zi+20])
#
#
#        
         
    
    
#ploting Count
#out = np.where(subcube)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(out[0],out[1],out[2],'r,')
    