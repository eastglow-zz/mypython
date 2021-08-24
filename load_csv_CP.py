#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:43:35 2021

@author: donguk
"""

# Load csv data from the crystal plasticity example simulations
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd


def load_csv_CP(fname):
    data = np.genfromtxt(fname, dtype = float, delimiter = ',', names = True)
    print("Name field of",fname, ":")
    print(data.dtype.names)
    return data
    