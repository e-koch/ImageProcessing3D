#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:20:03 2018

@author: haswani
"""
import matplotlib.pyplot as plt

def MySineWave(wavelength):
    import numpy as np
    
    x = np.linspace(-2*np.pi,2*np.pi,100)
    f = np.sin(2*np.pi*x/wavelength)

    plt.plot(x,f)
    plt.show()
    
MySineWave(2.3)

