from matplotlib import rcParams
from matplotlib import pyplot as plt
import numpy as np
#changing default font
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']



def barchart_setting(axes1, axes2, upper_y_lim):
    axes1.grid(color='white', linestyle='-', linewidth=0.5, alpha=0.7, axis='both', which='both')
    axes1.set_facecolor('#F0F0F0')
    axes2.grid(color='white', linestyle='-', linewidth=0.5, alpha=0.7, axis='both', which='both')
    axes2.set_facecolor('#F0F0F0')
    axes1.set_yticks([0,200,400,600])
    axes1.set_xticks(np.arange(0,11,1))
    axes2.set_yticks([0,200,400,600])
    axes2.set_xticks(np.arange(0,11,1))
    axes1.set_ylim([0,upper_y_lim])
    axes2.set_ylim([0,upper_y_lim])
    axes1.spines[['right', 'top']].set_visible(False)
    axes2.spines[['right', 'top']].set_visible(False)
    axes1.grid(zorder=1)
    axes2.grid(zorder=1)
    