import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors
from cycler import cycler

#syle
plt.style.use('seaborn-notebook')
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12

#set points 
##How to automaticlly pull data from analyze/output files?
npc = [1, 2, 3, 4, 5]

D1_all = 0.151, 0.051, 0.009, 0, -0.003
D1_hi = 0.161, 0.058, 0.013, 0.001, 0.001
D1_lo = 0.125, 0.034, 0.001, -0.001, -0.001

#set labels and titles
plt.title('0.3nT/s Threshold')
plt.ylabel('$\Delta$PoD')
plt.xlabel('NPC Members Required')

plt.xticks(ticks=npc)

#0 line for refernce
plt.axhline(y=0, color='grey', linestyle = "--")

#plot mag groups
plt.plot(npc, D1_all, '-oC1', label='All')
plt.plot(npc, D1_hi, '-oC0', label ='High')
plt.plot(npc, D1_lo, '-oC2', label="Low")

#legend
plt.legend(loc='upper right', edgecolor='white', framealpha=1, title='Magnetometers')

plt.show()