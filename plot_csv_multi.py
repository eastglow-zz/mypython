#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:26:10 2021

@author: donguk
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
from load_csv_CP import *
# import tkinter as tk

f_eul_0_0 = '/Users/donguk/projects/myxtalplast/custom/eul0_0_0_out.csv'
f_eul_45_0 = '/Users/donguk/projects/myxtalplast/custom/eul0_45_0_out.csv'
f_eul_45_45 = '/Users/donguk/projects/myxtalplast/custom/eul45_45_0_out.csv'
f_eul_111 = '/Users/donguk/projects/myxtalplast/custom/eul_111nd_out.csv'
f_iso_0_0 = '/Users/donguk/projects/myxtalplast/custom/iso0_0_0_out.csv'
f_iso_45_0 = '/Users/donguk/projects/myxtalplast/custom/iso0_45_0_out.csv'
f_iso_45_45 = '/Users/donguk/projects/myxtalplast/custom/iso45_45_0_out.csv'
f_iso_111 = '/Users/donguk/projects/myxtalplast/custom/iso_111nd_out.csv'

d_0_0_0 = load_csv_CP(f_eul_0_0)
d_0_45_0 = load_csv_CP(f_eul_45_0)
d_45_45_0 = load_csv_CP(f_eul_45_45)
d_111 = load_csv_CP(f_eul_111)
i_0_0_0 = load_csv_CP(f_iso_0_0)
i_0_45_0 = load_csv_CP(f_iso_45_0)
i_45_45_0 = load_csv_CP(f_iso_45_45)
i_111 = load_csv_CP(f_iso_111)

plotfont = {'fontname':'Times New Roman'}

fig = plt.figure(dpi=300)
fig, ax = plt.subplots()

ax.plot(d_0_0_0['e_zz'],d_0_0_0['stress_zz'])
ax.plot(d_0_45_0['e_zz'],d_0_45_0['stress_zz'])
ax.plot(d_45_45_0['e_zz'],d_45_45_0['stress_zz'])
ax.plot(d_111['e_zz'],d_111['stress_zz'])
# ax.plot(i_0_0_0['e_zz'],i_0_0_0['stress_zz'])
# ax.plot(i_0_45_0['e_zz'],i_0_45_0['stress_zz'])
# ax.plot(i_45_45_0['e_zz'],i_45_45_0['stress_zz'])
plt.xlabel(r'$\epsilon_{zz}$', fontsize=20)
plt.ylabel(r'$\sigma_{zz}$', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Single crystal FCC', **plotfont, fontsize=20)
plt.legend(["001//z", "011//z","(45,45,0)", "111//z"])

plt.show()

fig.savefig('./sig_eps_anisoE.eps',format = 'eps', bbox_inches='tight')

fig = plt.figure(dpi=300)
fig, ax = plt.subplots()

# ax.plot(d_0_0_0['e_zz'],d_0_0_0['stress_zz'])
# ax.plot(d_0_45_0['e_zz'],d_0_45_0['stress_zz'])
# ax.plot(d_45_45_0['e_zz'],d_45_45_0['stress_zz'])
ax.plot(i_0_0_0['e_zz'],i_0_0_0['stress_zz'])
ax.plot(i_0_45_0['e_zz'],i_0_45_0['stress_zz'])
ax.plot(i_45_45_0['e_zz'],i_45_45_0['stress_zz'])
ax.plot(i_111['e_zz'],i_111['stress_zz'])
plt.xlabel(r'$\epsilon_{zz}$', fontsize=20)
plt.ylabel(r'$\sigma_{zz}$', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Single crystal FCC isotropic elasticity', **plotfont, fontsize=20)
plt.legend(["001//z", "011//z","(45,45,0)", "111//z"])

plt.show()

fig.savefig('./sig_eps_isoE.eps',format = 'eps', bbox_inches='tight')


fig = plt.figure(dpi=300)
fig, ax = plt.subplots()

ax.plot(d_0_0_0['e_zz'],d_0_0_0['gss'])
plt.xlabel(r'$\epsilon_{zz}$', fontsize=20)
plt.ylabel('Slip resistance', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Single crystal FCC', **plotfont, fontsize=20)
plt.show()

fig.savefig('./SR_eps.eps',format = 'eps', bbox_inches='tight')


fig = plt.figure(dpi=300)
fig, ax = plt.subplots()

ax.plot(d_0_0_0['e_zz'],d_0_0_0['slip_increment'])
plt.xlabel(r'$\epsilon_{zz}$', fontsize=20)
plt.ylabel('Slip increment', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Single crystal FCC', **plotfont, fontsize=20)
plt.show()

fig.savefig('./SI_eps.eps',format = 'eps', bbox_inches='tight')