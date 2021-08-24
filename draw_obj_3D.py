#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:40:49 2021

@author: donguk
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import proj3d
from itertools import product, combinations


def draw_unit_cube(ax, T, c):
    r = [0, 1]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            s = s + T
            e = e + T
            ax.plot3D(*zip(s, e), color=c)

        
def draw_frame(ax, c):
    draw_unit_cube(ax,[0,0,0],c)
    draw_unit_cube(ax,[-1,0,0],c)
    draw_unit_cube(ax,[0,-1,0],c)
    draw_unit_cube(ax,[-1,-1,0],c)
    draw_unit_cube(ax,[0,0,-1],c)
    draw_unit_cube(ax,[-1,0,-1],c)
    draw_unit_cube(ax,[0,-1,-1],c)
    draw_unit_cube(ax,[-1,-1,-1],c)
    
def draw_vector_3D(ax, O, V, col):
    ax.quiver(O[0],O[1],O[2],V[0],V[1],V[2],length=1.0, arrow_length_ratio=0.1, color = col)
    
def rot_mat_z(theta):
    rad = theta*math.acos(-1)/180
    R = [[math.cos(rad),-math.sin(rad),0],
         [math.sin(rad),math.cos(rad),0],
         [0,0,1]]
    return R

def rot_mat_x(theta):
    rad = theta*math.acos(-1)/180
    R = [[1,0,0],
         [0,math.cos(rad),-math.sin(rad)],
         [0,math.sin(rad),math.cos(rad)]]
       
    return R

def Euler_rot_bunge(phi1, PHI, phi2):
    R1 = np.matmul(rot_mat_x(PHI),rot_mat_z(phi1))
    R = np.matmul(rot_mat_z(phi2),R1)
    return R

def Deform_gradient():
    # R = [[1.2,0,0],
    #      [0,1.2,0],
    #      [0,0,0.8]]
    R= [[0.7904,-0.0738,-0.1942],
        [0.0602, 1.1321,0.0602],
        [0.1340,-0.0738,1.1186]] 
    
    return R
    


    
    
    
    