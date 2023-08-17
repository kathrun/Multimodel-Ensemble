import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
from spacepy.plot import style 

style()

# set style information
mpl.rcParams['lines.linewidth'] = 2.5
#mpl.rcParams['axes.labelsize'] = 16
#mpl.rcParams['xtick.labelsize'] = 12
#mpl.rcParams['ytick.labelsize'] = 12

npc = [1, 2, 3, 4, 5]

# creating subplots
# not sure this is the most effecent way to create them but it works?
fig = plt.figure()
fig.set_tight_layout(True)
gs = fig.add_gridspec(2, 2)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex=True, sharey=False)
fig.subplots_adjust(hspace=0.15, wspace=0.15)


# PoD
mod_b = 0.958, 0.866, 0.703, 0.472, 0.077
mod_h = 0.965, 0.918, 0.823, 0.671, 0.462
reg = 0.860, 0.680, 0.485, 0.297, 0.119

ax1.set_title('PoD', fontsize=16)

ax1.axhline(y=0.698, color='grey', linestyle="--")

ax1.plot(npc, reg, '-o', color='black', alpha=0.75)
ax1.plot(npc, mod_b, '-o')
ax1.plot(npc, mod_h, '-o')

#PoFD
mod_b = 0.355, 0.189, 0.078, 0.022, 0.0
mod_h = 0.391, 0.210, 0.110, 0.044, 0.011
reg = 0.221, 0.073, 0.023, 0.003, 0.001

ax2.set_title('PoFD', fontsize=16)

ax2.axhline(y=0.110, color='grey', linestyle="--", label='Deterministic')

ax2.plot(npc, reg, '-o', color='black', alpha=0.75, label='Set Threshold')
ax2.plot(npc, mod_b, '-o', label='Scaled Bias')
ax2.plot(npc, mod_h, '-o', label='Scaled HSS')


#HSS
mod_b = 0.619, 0.679, 0.610, 0.427, 0.070
mod_h = 0.606, 0.718, 0.698, 0.588, 0.403
reg = 0.637, 0.613, 0.471, 0.302, 0.122

ax3.set_title('HSS', fontsize=16)
ax3.set_xlabel('NPC Members Required', fontsize=14)
ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))

ax3.axhline(y=0.593, color='grey', linestyle="--")

ax3.plot(npc, reg, '-o', color='black', alpha=0.75)
ax3.plot(npc, mod_b, '-o')
ax3.plot(npc, mod_h, '-o')

# Bias
mod_b = 1.24, 1.021, 0.767, 0.490, 0.077
mod_h = 1.235, 1.063, 0.817, 0.702, 0.470
reg = 1.100, 0.759, 0.509, 0.301, 0.120
# set labels and titles
ax4.set_title('Bias', fontsize=16)
ax4.set_xlabel('NPC Members Required', fontsize=14)
ax4.xaxis.set_major_locator(ticker.MultipleLocator(1))

ax4.axhline(y=0.817, color='grey', linestyle="--")

ax4.plot(npc, reg, '-o', color='black', alpha=0.75)
ax4.plot(npc, mod_b, '-o')
ax4.plot(npc, mod_h, '-o')


# legend
ax2.legend(loc='upper right', edgecolor='white', framealpha=1)

plt.show()