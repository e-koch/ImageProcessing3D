import matplotlib as plt 
import math
import numpy as np
from scipy.ndimage.filters import uniform_filter
from scipy.ndimage.filters import median_filter
from astropy.io import fits
cube = fits.getdata('ngc3627_co21_12m+7m+tp_pbcorr_round_k.fits')
summ = np.nansum(cube)
print("\nSum of all pixel values treating nan as 0\n")
print(summ)
#print(cube.shape)
count2 = 0 
count1 = 0
count3 = 0 
for i in cube.flat:
   # if i>1.0:
        #print(i)
    if not math.isnan(i) and i>0.25:
        count1 = count1 + 1 #important
    if not math.isnan(i) and i>1.0:
        count2 = count2+1
    if not math.isnan(i) and i>5.0:
        count3 = count3+1    
#print(count2)
#print("\n")
#rint(cube.size)
fraction5 = count3/cube.size
fraction1 = count2/cube.size
fraction25 = count1/cube.size 
print("\nFraction of elements larger than 0.25 values = \n")
print(fraction25)
print("\nFraction of elements larger than 1.0 values = \n")
print(fraction1)
print("\nFraction of elements larger than 5.0 values = \n")
print(fraction5)


#3.What is the standard deviation of the noise value? Assume the image has a Gaussian noise distribution. Hint: the first few channels in the image are usually entirely noise.
vals = cube[0:10,:,:].ravel()
sd = np.nanstd(vals)
print("Standard deviation of noise : ")
print(sd)
#end of 3
#4. Make an image that is the sum of the map over the velocity axis (axis=0 in numpy).
test = np.nansum(cube,axis=(1,2))
print(test)
#end of 4


