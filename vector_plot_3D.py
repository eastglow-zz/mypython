#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:54:13 2021

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
ax.view_init(azim=15, elev=30)


draw_frame(ax, "gray")


# draw a vector
O = [0,0,0]
U = [1,0,0]
V = [0,1,0]
W = [0,0,1]
C = [1,1,1]
L = [-1,0,0]
M = [0,-1,0]
N = [0,0,-1]
draw_vector_3D(ax, O, U, "black")
draw_vector_3D(ax, O, V, "black")
draw_vector_3D(ax, O, W, "black")

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
FU = np.matmul(F,U)
FV = np.matmul(F,V)
FW = np.matmul(F,W)


draw_vector_3D(ax, O, FU, "red")
draw_vector_3D(ax, O, FV, "red")
draw_vector_3D(ax, O, FW, "red")


plt.show()