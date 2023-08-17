import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
from cycler import cycler

#set style information
#create own style?
plt.style.use('seaborn-notebook')
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams["figure.titlesize"]  = 20
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
plt.rcParams['figure.constrained_layout.use'] = True

#data for graphs
#how to pull automatically from analyze/output files?
npc = [1, 2, 3, 4, 5]

#legend
#ax1.legend(loc='upper left')
#plt.legend(frameon=False)

#creating subplots
#not sure this is the most effecent way to create them but it works?
fig = plt.figure()
gs = fig.add_gridspec(2,2)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.15, wspace=0)


#0.3 Threshold
#HSS Data
H_all = 0.032, 0.007, -0.151, -0.308, -0.489
H_hi = 0.074, 0.007, -0.119, -0.239, -0.386
H_lo = -0.040, 0.003, -0.190, -0.391, -0.545

#set labels and titles
ax1.set_title('0.3nT/s Threshold', fontsize = 16)
ax1.set_ylabel('$\Delta$HSS', fontsize=14)


#0 line for refernce
ax1.axhline(y=0, color='grey', linestyle = "--")

#plot mag groups
ax1.plot(npc, H_all, '-oC1')
ax1.plot(npc,H_hi, '-oC0')
ax1.plot(npc, H_lo, '-oC2')

#0.7 Threshold
#HSS Data
H_all = 0.026, -0.087, -0.289, -0.443, -0.525
H_hi = 0.044, -0.015, -0.191, -0.327, -0.406
H_lo = -0.052, -0.250, -0.483, -0.647, -0.697

#set labels and titles
ax2.set_title('0.7nT/s Threshold', fontsize = 16)

#0 line for refernce
ax2.axhline(y=0, color='grey', linestyle = "--")

#plot mag groups
ax2.plot(npc, H_all, '-oC1', label='All')
ax2.plot(npc,H_hi, '-oC0', label ='High')
ax2.plot(npc, H_lo, '-oC2', label="Low")

#1.1 Threshold
#HSS Data
H_all = 0.013,-0.161, -0.314, -0.407, -0.464
H_hi = -0.004, -0.114, -0.246, -0.334, -0.394
H_lo = 0.018, -0.294, -0.461, -0.536, -0.557

#set labels and titles
ax3.set_title('1.1nT/s Threshold', fontsize = 16)
ax3.set_ylabel('$\Delta$HSS', fontsize=14)
ax3.set_xlabel('NPC Members Required', fontsize=14)
ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))

#0 line for refernce
ax3.axhline(y=0, color='grey', linestyle = "--")

#plot mag groups
ax3.plot(npc, H_all, '-oC1')
ax3.plot(npc,H_hi, '-oC0')
ax3.plot(npc, H_lo, '-oC2')

#1.5 Threshold
#HSS Data
H_all = -0.006, -0.123, -0.270, -0.311, -0.385
H_hi = -0.044, -0.113, -0.226, -0.275, -0.353
H_lo = 0.047, -0.169, -0.383, -0.377, -0.411

#set labels and titles
ax4.set_title('1.5nT/s Threshold', fontsize = 16)
ax4.set_xlabel('NPC Members Required', fontsize=14)
ax4.xaxis.set_major_locator(ticker.MultipleLocator(1))

#0 line for refernce
ax4.axhline(y=0, color='grey', linestyle = "--")

#plot mag groups
ax4.plot(npc, H_all, '-oC1')
ax4.plot(npc,H_hi, '-oC0')
ax4.plot(npc, H_lo, '-oC2')

#legend
ax2.legend(loc='upper right', edgecolor='white', framealpha=1, title='Magnetometers')

plt.show()