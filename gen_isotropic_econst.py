#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:13:46 2021

@author: donguk
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import proj3d
from itertools import product, combinations

#Generate isotropic elastic constant tensor in Voight notation
# Unit = GPa

E = 100  # Elastic constant (GPa)
nu = 0.25   # Poisson's ratio

prefac = E/(1+nu)/(1-2*nu)
Emat = np.array([[1-nu, nu, nu, 0, 0, 0],
        [nu, 1-nu, nu, 0, 0, 0],
        [nu, nu, 1-nu, 0, 0, 0],
        [0, 0, 0, (1-2*nu)/2, 0, 0],
        [0, 0, 0, 0, (1-2*nu)/2, 0],
        [0, 0, 0, 0, 0, (1-2*nu)/2]])
C = prefac * Emat
print(C)