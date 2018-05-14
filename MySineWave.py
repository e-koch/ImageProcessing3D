#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:20:03 2018

@author: haswani
"""

def MySineWave(wavelength):
    import numpy as np
    from numpy import pi

    x = np.linspace(-2*pi,2*pi,100)

    f = np.sin(2*pi*x/wavelength)

    import matplotlib.pyplot as plt
    plt.plot(x,f)
    plt.show()
    
MySineWave(2.3)

