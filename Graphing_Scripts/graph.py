import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
from cycler import cycler
from spacepy.plot import style 

style()

# set style information
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12

plt.tight_layout()

# set points 

npc = [1, 2, 3, 4, 5]

D1_all = 0.151, 0.051, 0.009, 0, 0
D1_hi = 0.161, 0.058, 0.013, 0.001, 0.001
D1_lo =  0.125, 0.034, 0.001, -0.001, -0.001

# set labels and titles
plt.title('0.3nT/s Threshold', fontsize=20)
plt.ylabel('$\Delta$PoD', fontsize=16)
plt.xlabel('NPC Members Required', fontsize=16)

plt.xticks(ticks=npc)

# 0 line for refernce
plt.axhline(y=0, color='grey', linestyle="--")

# plot mag groups
plt.plot(npc, D1_all, '-oC1', label='All')
plt.plot(npc, D1_hi, '-oC0', label='High')
plt.plot(npc, D1_lo, '-oC2', label="Low")

# legend
plt.legend(loc='upper right', edgecolor='white', framealpha=1, 
           title='Magnetometers')

plt.show()