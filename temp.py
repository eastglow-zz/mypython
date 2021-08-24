# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#This is my first trial of python scripting. Main goal of the use of python is
#to replace what Matlab have been doing, which are, making plots, 2D images or
#even 3D images. After getting familiar with this, I'll also work on developing
#graphical user interfaces for phase-field codes, especially viewing the microstructure
#as the simulation goes.

#Import modules
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x,y)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My first graph!')

plt.show()