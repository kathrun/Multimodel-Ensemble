import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
from cycler import cycler
from spacepy.plot import style 

style()

# set style information
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams["figure.titlesize"]  = 20
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12

# data for graphs
npc = [1, 2, 3, 4, 5]

# creating subplots
fig = plt.figure()
gs = fig.add_gridspec(2, 2)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex=True, sharey=False)
fig.set_tight_layout(True)
fig.subplots_adjust(hspace=0.15, wspace=0.1)
fig.suptitle('0.3nT/s Threshold')


# PoD
all = 0.151, 0.051, 0.009, 0, 0
hi = 0.161, 0.058, 0.013, 0.001, 0.001
low = 0.125, 0.034, 0.001, -0.001, -0.001

# set labels and titles
ax1.set_title('$\Delta$PoD', fontsize=16)

# 0 line for refernce
# ax1.axhline(y=1, color='grey', linestyle="--")

# plot mag groups
ax1.plot(npc, all, '-oC1')
ax1.plot(npc, hi, '-oC0')
ax1.plot(npc, low, '-oC2')

# PoFD
all = 0.112, 0.02, 0.004, 0.004, 0.004
hi = 0.152, 0.032, 0.01, 0.008, 0.008
low = 0.095, 0.014, 0.002, 0.002, 0.002

# set labels and titles
ax2.set_title('-$\Delta$PoFD', fontsize=16)

# 0 line for refernce
# ax2.axhline(y=0, color='grey', linestyle="--")

# plot mag groups
ax2.plot(npc, all, '-oC1', label='All')
ax2.plot(npc, hi, '-oC0', label='High')
ax2.plot(npc, low, '-oC2', label="Low")

# HSS
all = 0.032, 0.03, 0.005, -0.003, -0.003 
hi =  0.074, 0.044, 0.008, -0.003, -0.003 
low =  -0.04, 0.005, -0.002, -0.004, -0.004

#set labels and titles
ax3.set_title('$\Delta$HSS', fontsize=16)
ax3.set_xlabel('NPC', fontsize=14)
ax3.set_xticks(npc)
# ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))

# 0 line for refernce
# ax3.axhline(y=1, color='grey', linestyle="--")

# plot mag groups
ax3.plot(npc, all, '-oC1')
ax3.plot(npc, hi, '-oC0')
ax3.plot(npc, low, '-oC2')

# Bias
all = 0.181, 0.073, 0.015, 0.005, 0.005
hi = -0.075, 0.074, 0.019, 0.006, 0.006
low =  -0.024, 0.063, 0.007, 0.005, 0.005

# set labels and titles
ax4.set_title('Change in Bias from 1', fontsize=16)
ax4.set_xlabel('NPC', fontsize=14)
# ax4.xaxis.set_major_locator(ticker.MultipleLocator(1))

# 0 line for refernce
# ax4.axhline(y=1, color='grey', linestyle="--")

# plot mag groups
ax4.plot(npc, all, '-oC1', label='All')
ax4.plot(npc, hi, '-oC0', label='High')
ax4.plot(npc, low, '-oC2', label="Low")

# legend
ax4.legend(loc='upper right', edgecolor='white', framealpha=1,
           title='Magnetometers')

plt.show()