#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:09:42 2021

@author: donguk
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from itertools import product, combinations
from draw_obj_3D import *

fig = plt.figure()
ax = plt.subplot(projection='3d')
# ax.set_aspect("auto")
ax.set_box_aspect((1, 1, 1))
ax.view_init(azim=60, elev=30)


draw_frame(ax, "gray")


# Basis
O = [0,0,0]
X = [1,0,0]
Y = [0,1,0]
Z = [0,0,1]
C = [1,1,0]
ZX = [1,0,1]
ZY = [0,1,1]
draw_vector_3D(ax, O, X, "black") #bottom 00-10
draw_vector_3D(ax, O, Y, "black") #bottom 00-01
draw_vector_3D(ax, X, Y, "black") #bottom 10-11
draw_vector_3D(ax, Y, X, "black") #bottom 01-11
draw_vector_3D(ax, Z, X, "black") #top 00-10
draw_vector_3D(ax, Z, Y, "black") #top 00-01
draw_vector_3D(ax, ZX, Y, "black") #top 10-11
draw_vector_3D(ax, ZY, X, "black") #top 01-11
draw_vector_3D(ax, O, Z, "black") #pillar 
draw_vector_3D(ax, X, Z, "black") #pillar 
draw_vector_3D(ax, Y, Z, "black") #pillar 
draw_vector_3D(ax, C, Z, "black") #pillar 




# phi1 = 45
# PHI = 54.1
# phi2 = 0
#Rz1=rot_mat_z(phi1)
# RU = np.matmul(Rz1, U)
# RV = np.matmul(Rz1, V)
#R_euler = Euler_rot_bunge(phi1, PHI, phi2)
#RU = np.matmul(R_euler,U)
#RV = np.matmul(R_euler,V)
# RU = Rz1*U
# RV = Rz1*V
#draw_vector_3D(ax, O, RU, "blue")
#draw_vector_3D(ax, O, RV, "cyan")
F = Deform_gradient()
FO = np.matmul(F,O)
FX = np.matmul(F,X)
FY = np.matmul(F,Y)
FZ = np.matmul(F,Z)
FC = np.matmul(F,C)
FZX = np.matmul(F,ZX)
FZY = np.matmul(F,ZY)

draw_vector_3D(ax, FO, FX, "red") #bottom 00-10
draw_vector_3D(ax, FO, FY, "red") #bottom 00-01
draw_vector_3D(ax, FX, FY, "red") #bottom 10-11
draw_vector_3D(ax, FY, FX, "red") #bottom 01-11
draw_vector_3D(ax, FZ, FX, "red") #top 00-10
draw_vector_3D(ax, FZ, FY, "red") #top 00-01
draw_vector_3D(ax, FZX, FY, "red") #top 10-11
draw_vector_3D(ax, FZY, FX, "red") #top 01-11
draw_vector_3D(ax, FO, FZ, "red") #pillar 
draw_vector_3D(ax, FX, FZ, "red") #pillar 
draw_vector_3D(ax, FY, FZ, "red") #pillar 
draw_vector_3D(ax, FC, FZ, "red") #pillar 


# draw_vector_3D(ax, O, FU, "red")
# draw_vector_3D(ax, O, FV, "red")
# draw_vector_3D(ax, O, FW, "red")


plt.show()