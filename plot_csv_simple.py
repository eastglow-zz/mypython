#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:28:58 2021

@author: donguk
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
# import tkinter as tk

filename = '/Users/donguk/projects/myxtalplast/single_crystal_test_out.csv'

data = np.genfromtxt(filename, dtype = float, delimiter = ',', names = True)
print(data['stress_zz'])

x = data['e_zz']
y = data['stress_zz']
t = data['time']
slip_resistance = data['gss']
slip_increment = data['slip_increment']

plotfont = {'fontname':'Times New Roman'}

fig = plt.figure(dpi=300)
fig, ax = plt.subplots()

ax.plot(x,y)
plt.xlabel(r'$\epsilon_{zz}$', fontsize=20)
plt.ylabel(r'$\sigma_{zz}$', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Single crystal FCC', **plotfont, fontsize=20)
plt.show()

fig.savefig('./sig_eps.eps',format = 'eps', bbox_inches='tight')


fig = plt.figure(dpi=300)
fig, ax = plt.subplots()

ax.plot(x,slip_resistance)
plt.xlabel(r'$\epsilon_{zz}$', fontsize=20)
plt.ylabel('Slip resistance', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Single crystal FCC', **plotfont, fontsize=20)
plt.show()

fig.savefig('./SR_eps.eps',format = 'eps', bbox_inches='tight')


fig = plt.figure(dpi=300)
fig, ax = plt.subplots()

ax.plot(x,slip_increment)
plt.xlabel(r'$\epsilon_{zz}$', fontsize=20)
plt.ylabel('Slip increment', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Single crystal FCC', **plotfont, fontsize=20)
plt.show()

fig.savefig('./SI_eps.eps',format = 'eps', bbox_inches='tight')