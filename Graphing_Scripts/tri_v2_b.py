import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors
from cycler import cycler

#set style information
#create own style?
plt.style.use('seaborn-notebook')
mpl.rcParams['lines.linewidth'] = 2.5
mpl.rcParams["figure.titlesize"]  = 14
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12

#data for graphs
#how to pull automatically from analyze/output files?
npc = [1, 2, 3, 4, 5]

#0.3 Threshold
#PoD 0.3
D1_all = 0.151, 0.051, 0.009, 0.0, 0.0
D1_hi = 0.161, 0.058, 0.013, 0.001, 0.001
D1_lo = 0.125, 0.034, 0.001, -0.001, -0.001

#PoFD 0.3
F2_all = -0.112, -0.020, -0.004, -0.004, -0.004
F2_hi = -0.152, -0.032, -0.010, -0.008, -0.008
F2_lo = -0.095, -0.014, -0.002, -0.002, -0.002

#HSS 0.3
H3_all = 0.032, 0.030, 0.005, -0.003, -0.003
H3_hi = 0.074, 0.044, 0.008, -0.003, -0.003
H3_lo = -0.040, 0.005, -0.002, -0.004, -0.004

#0.7 Threshold
#PoD 0.7
D4_all = 0.145, 0.026, 0.001, 0.0, 0.0
D4_hi = 0.176, 0.035, 0.002, 0.0, 0.0
D4_lo = 0.056, -0.001, -0.001, -0.001, -0.001

#PoFD 0.7
F5_all = -0.066, 0.005, -0.002, -0.002, -0.002
F5_hi = -0.117, -0.009, -0.003, -0.003, -0.003
F5_lo = -0.035, -0.002, -0.001, -0.001, -0.001

#HSS 0.7
H6_all = 0.026, 0.015, -0.002, -0.003, -0.003
H6_hi = 0.044, 0.026, -0.001, -0.003, -0.003
H6_lo = -0.052, -0.008, -0.003, -0.003, -0.003

#1.1 Threshold
#PoD 1.1
D7_all = 0.112, 0.015, -0.001, -0.001, -0.001
D7_hi = 0.123, 0.019, -0.002, -0.002, -0.002
D7_lo = 0.081, 0.004, 0.004, 0.004, 0.004

#PoFD 1.1
F8_all = -0.045, -0.004, -0.001, -0.001, -0.001
F8_hi = -0.089, -0.007, -0.003, -0.003, -0.003
F8_lo = -0.012, -0.002, 0.0, 0.0, -0.004

#HSS 1.1
H9_all = 0.013, 0.005, -0.003, -0.003, 0.003
H9_hi = -0.004, 0.008, -0.006, -0.006, 0.006
H9_lo = 0.018, -0.005, 0.003, -0.003, 0.003

#1.5 Threshold
#PoD 1.5
D10_all = 0.093, 0.015, 0.003, 0.003, 0.003
D10_hi = 0.088, 0.012, 0.002, 0.002, 0.002
D10_lo = 0.111, 0.026, 0.001, 0.005, 0.005

#PoFD 1.5
F11_all = -0.042, -0.004, 0.0, 0.0, 0.0
F11_hi = -0.083, -0.007, -0.001, -0.001, -0.001
F11_lo = -0.010, -0.001, 0.0, 0.0, 0.0

#HSS 1.5
H12_all = 0.013, 0.005, -0.003, -0.003, 0.003
H12_hi = -0.004, 0.008, -0.006, -0.006, 0.006
H12_lo = 0.018, -0.005, 0.003, -0.003, 0.003


#creating subplots
fig, ((ax1, ax2, ax3),(ax4, ax5, ax6),(ax7, ax8, ax9), (ax10, ax11, ax12)) = plt.subplots(4,3, figsize = (4, 3), sharey=True, sharex=True)

fig.subplots_adjust(hspace=0, wspace=0)
#titles and lables!

ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))

#0.3 Threshold plot
#plot PoD
ax1.set_title('$\Delta$PoD',fontsize=16)
ax1.set_ylabel('0.3 nT/s\nThreshold', rotation=0, labelpad=45, fontsize=16)

ax1.plot(npc, D1_all, '-oC0', label='All')
ax1.plot(npc, D1_hi, '-oC1', label='High')
ax1.plot(npc, D1_lo, '-oC2', label='Low')

ax1.axhline(y=0, color='grey', linestyle = "--")
#ax1.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

#plot PoFD
ax2.set_title('-$\Delta$PoFD',fontsize=16)

ax2.plot(npc, F2_all, '-oC0', label='All')
ax2.plot(npc, F2_hi, '-oC1', label='High')
ax2.plot(npc, F2_lo, '-oC2', label='Low')

ax2.axhline(y=0, color='grey', linestyle = "--")
#ax2.fill_between(npc, y1=-0.7, y2=0, color ='gainsboro')

#plot HSS
ax3.set_title('$\Delta$HSS',fontsize=16)

ax3.plot(npc, H3_all, '-oC0', label='All')
ax3.plot(npc,H3_hi, '-oC1', label ='High')
ax3.plot(npc, H3_lo, '-oC2', label="Low")

ax3.axhline(y=0, color='grey', linestyle = "--")
#ax3.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

#0.7 Threshold plots
#plot PoD
ax4.plot(npc, D4_all, '-oC0', label='All')
ax4.plot(npc, D4_hi, '-oC1', label='High')
ax4.plot(npc, D4_lo, '-oC2', label='Low')

ax4.axhline(y=0, color='grey', linestyle = "--")
#ax4.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

ax4.set_ylabel('0.7 nT/s\nThreshold', rotation=0, labelpad=45, fontsize=16)

#plot PoFD
ax5.plot(npc, F5_all, '-oC0', label='All')
ax5.plot(npc, F5_hi, '-oC1', label='High')
ax5.plot(npc, F5_lo, '-oC2', label='Low')

ax5.axhline(y=0, color='grey', linestyle = "--")
#ax5.fill_between(npc, y1=-0.7, y2=0, color ='gainsboro')

#plot HSS
ax6.plot(npc, H6_all, '-oC0', label='All')
ax6.plot(npc,H6_hi, '-oC1', label ='High')
ax6.plot(npc, H6_lo, '-oC2', label="Low")

ax6.axhline(y=0, color='grey', linestyle = "--")
#ax6.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

#1.1 Threshold plots
ax7.plot(npc, D7_all, '-oC0', label='All')
ax7.plot(npc, D7_hi, '-oC1', label='High')
ax7.plot(npc, D7_lo, '-oC2', label='Low')

ax7.axhline(y=0, color='grey', linestyle = "--")
#ax7.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

ax7.set_ylabel('1.1 nT/s\nThreshold', rotation=0, labelpad=45, fontsize=16)

#plot PoFD
ax8.plot(npc, F8_all, '-oC0', label='All')
ax8.plot(npc, F8_hi, '-oC1', label='High')
ax8.plot(npc, F8_lo, '-oC2', label='Low')

ax8.axhline(y=0, color='grey', linestyle = "--")
#ax8.fill_between(npc, y1=-0.7, y2=0, color ='gainsboro')

#plot HSS
ax9.plot(npc, H9_all, '-oC0', label='All')
ax9.plot(npc,H9_hi, '-oC1', label ='High')
ax9.plot(npc, H9_lo, '-oC2', label="Low")

ax9.axhline(y=0, color='grey', linestyle = "--")
#ax9.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

#1.5 Threshold plots
ax10.plot(npc, D10_all, '-oC0', label='All')
ax10.plot(npc, D10_hi, '-oC1', label='High')
ax10.plot(npc, D10_lo, '-oC2', label='Low')

ax10.axhline(y=0, color='grey', linestyle = "--")
#ax10.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

ax10.set_ylabel('1.5 nT/s\nThreshold', rotation=0, labelpad=50, fontsize=16)

#plot PoFD
ax11.plot(npc, F11_all, '-oC0', label='All')
ax11.plot(npc, F11_hi, '-oC1', label='High')
ax11.plot(npc, F11_lo, '-oC2', label='Low')

ax11.axhline(y=0, color='grey', linestyle = "--")
#ax11.fill_between(npc, y1=-0.7, y2=0, color ='gainsboro')

ax11.set_xlabel('NPC Members Required', fontsize=16)

#plot HSS
ax12.plot(npc, H12_all, '-oC0', label='All')
ax12.plot(npc,H12_hi, '-oC1', label ='High')
ax12.plot(npc, H12_lo, '-oC2', label="Low")

ax12.axhline(y=0, color='grey', linestyle = "--")
#ax12.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

#legend
ax3.legend(loc='upper right', edgecolor='white', framealpha=1, title='Magnetometers')


plt.show()