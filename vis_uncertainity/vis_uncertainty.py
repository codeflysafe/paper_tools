import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

y = [0.12, 0.14, 0.2, 0.53, 0.67]
x = [0,1,2,3,4]
plt.bar(x, height= y, width= 0.5 , color = 'darkblue')
ax = plt.gca()
ax.yaxis.set_ticks_position('right')
ax.yaxis.set_label_position("right")
# ax.invert_yaxis()
# ax.set_ylabel('uncertainty',labelpad = 10)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
# plt.axis(False)
plt.xticks([])
plt.savefig('vis_uncertainty.png', dpi = 200)
plt.show()

