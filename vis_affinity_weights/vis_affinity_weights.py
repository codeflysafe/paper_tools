import torch
import seaborn as sns
import pandas as pd
import torch
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.01378721, 0.00188351, 0.00256839, 0.02656049, 0.24754906, 0.00767636, 0.00590704, 0.00808847, 0.12233777, 0.04628615, 0.14342889, 0.20172444, 0.15029208, 0.01494246, 0.00279765, 0.00417007])
f,ax = plt.subplots(figsize = (10, 3))
fontdict={'family' : 'Times New Roman', 'size'   : 14}
# plt.title(station, fontdict={'family' : 'Times New Roman', 'size'   : 14})
plt.rc('font',family='Times New Roman')
plt.subplots_adjust(left=0.05,right=0.95,top=0.8,bottom=0.6)
# left bottom w h
char_ax = f.add_axes([0.05,0.3,0.6,0.05])
a_s = a.reshape((1,16))
# 't-15','t-14','t-13','t-12','t-11','t-10','t-9','t-8','t-7','t-6','t-5','t-4','t-3','t-2','t-1','t'
ax = sns.heatmap(a_s, cmap='PuBu', vmin=0.0, vmax=0.5, ax = ax, cbar_ax=char_ax,
cbar_kws = {'orientation':'horizontal','shrink':2},
xticklabels = ['t-15','t-14','t-13','t-12','t-11','t-10','t-9','t-8','t-7','t-6','t-5','t-4','t-3','t-2','t-1','t'],
yticklabels=['t'])
# plt.text(x = 0, y = 1.8, s = 'Time: t-15 - t', fontdict= fontdict)
plt.savefig('vis_affinity_weights.png',dip = 300)
plt.show()

