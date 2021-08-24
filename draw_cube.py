#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:40:49 2021

@author: donguk
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from itertools import product, combinations


def draw_unit_cube(ax, r, T, c):
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            s = s + T
            e = e + T
            ax.plot3D(*zip(s, e), color=c)

        
def draw_vector_3D(O, V, col):
    x.quiver(O[0],O[1],O[2],V[0],V[1],V[2],length=1.0, arrow_length_ratio=0.1, color = col)