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

# 0.3 Threshold
# PoD
D1_all = 0.151, -0.028, -0.241, -0.418, -0.597
D1_hi = 0.162, -0.013, -0.205, -0.373, -0.578
D1_lo = 0.125, -0.064, -0.328, -0.523, -0.644

D4_all = 0.145, -0.146, -0.371, -0.502, -0.566
D4_hi = 0.176, -0.072, -0.299, -0.435, -0.578
D4_lo = 0.056, -0.36, -0.581, -0.695, -0.644

D7_all = 0.112, -0.212, -0.374, -0.45, -0.491
D7_hi = 0.123, -0.158, -0.328, -0.412, -0.462
D7_lo = 0.081, -0.373, -0.513, -0.562, -0.576

D10_all = 0.093, -0.176, -0.322, -0.356, -0.405
D10_hi = 0.088, -0.146, -0.289, -0.333, -0.39
D10_lo = 0.111, -0.272, -0.432, -0.432, -0.453


# -PoFD
F2_all = -0.112, 0.033, 0.085, 0.105, 0.109
F2_hi = -0.152, 0.028, 0.12, 0.158, 0.165
F2_lo =  -0.095, 0.036, 0.071, 0.084, 0.086

F5_all = -0.066, 0.031, 0.057, 0.061, 0.064
F5_hi = -0.177, 0.049, 0.1, 0.109, 0.112
F5_lo = -0.034, 0.021, 0.031, 0.033, 0.035
 
F8_all = -0.044, 0.026, 0.05, 0.057, 0.059
F8_hi = -0.09, 0.033, 0.076, 0.089, 0.092
F8_lo = 0.013, 0.021, 0.03, 0.033, 0.034

F11_all = -0.042, 0.026, 0.047, 0.051, 0.054
F11_hi = -0.083, 0.026, 0.063, 0.07, 0.073
F11_lo = -0.01, 0.028, 0.035, 0.038, 0.04

# HSS
H3_all = 0.032, 0.008, -0.15, -0.308, -0.489
H3_hi = 0.075, 0.008, -0.119, -0.239, -0.386
H3_lo =  -0.04, 0.002, -0.191, -0.391, -0.546

H6_all = 0.026, -0.087, -0.289, -0.443, -0.525
H6_hi = 0.044, -0.016, -0.192, -0.327, -0.406
H6_lo =  -0.052, -0.25, -0.484, -0.647, -0.697

H9_all = 0.013, -0.161, -0.314, -0.407, -0.464
H9_hi = -0.005, -0.115, -0.247, -0.334, -0.395
H9_lo =  0.018, -0.294, -0.461, -0.536, -0.557

H12_all = -0.006, -0.123, -0.269, -0.311, -0.384
H12_hi = -0.044, -0.114, -0.226, -0.276, -0.353
H12_lo =  0.047, -0.169, -0.383, -0.377, -0.411

# Bias 0.3
B13_all = 0.09, -0.064, -0.334, -0.532, -0.716
B13_hi = 0.23, -0.024, -0.258, -0.444, -0.652
B13_lo = -0.238, -0.157, -0.512, -0.74, -0.866

# 0.7
B14_all = 0.161, -0.221, -0.509, -0.651, -0.721
B14_hi = 0.27, -0.132, -0.423, -0.571, -0.65
B14_lo = -0.154, -0.469, -0.757, -0.881, -0.929

# 1.1
B15_all = 0.215, -0.311, -0.565, -0.667, -0.716
B15_hi =  0.287, -0.227, -0.491, -0.604, -0.661
B15_lo = -0.001, -0.56, -0.784, -0.854, -0.882

# 1.5
B16_all =  0.202, -0.325, -0.589, -0.65, -0.713
B16_hi = 0.344, -0.226, -0.492, -0.558, -0.625
B16_lo = -0.255, -0.638, -0.893, -0.936, -0.989


#creating subplots
fig, ((ax1, ax2, ax3, ax13),
      (ax4, ax5, ax6, ax14),
      (ax7, ax8, ax9, ax15),
      (ax10, ax11, ax12, ax16)) = plt.subplots(4, 4, figsize=(4, 4),
                                               sharey=True, sharex=True)

fig.subplots_adjust(hspace=0, wspace=0)
fig.supxlabel('NPC Members Required', fontsize=16)
fig.set_tight_layout(True)
#titles and lables!

ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax13.xaxis.set_major_locator(ticker.MultipleLocator(1))

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

ax2.axhline(y=0, color='grey', linestyle="--")
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

#plot HSS
ax12.plot(npc, H12_all, '-oC0', label='All')
ax12.plot(npc, H12_hi, '-oC1', label ='High')
ax12.plot(npc, H12_lo, '-oC2', label="Low")

ax12.axhline(y=0, color='grey', linestyle = "--")
#ax12.fill_between(npc, y1=0, y2=0.2, color ='gainsboro')

# Bias
ax13.set_title('Change in Bias from 1',fontsize=16)
# plot Bias 0.3
ax13.plot(npc, B13_all, '-oC0', label='All')
ax13.plot(npc, B13_hi, '-oC1', label ='High')
ax13.plot(npc, B13_lo, '-oC2', label="Low")

ax13.axhline(y=0, color='grey', linestyle="--")

# plot Bias 0.7
ax14.plot(npc, B14_all, '-oC0', label='All')
ax14.plot(npc, B14_hi, '-oC1', label ='High')
ax14.plot(npc, B14_lo, '-oC2', label="Low")

ax14.axhline(y=0, color='grey', linestyle="--")

# plot Bias 1.1
ax15.plot(npc, B15_all, '-oC0', label='All')
ax15.plot(npc, B15_hi, '-oC1', label ='High')
ax15.plot(npc, B15_lo, '-oC2', label="Low")

ax15.axhline(y=0, color='grey', linestyle="--")

# plot Bias 1.5
ax16.plot(npc, B16_all, '-oC0', label='All')
ax16.plot(npc, B16_hi, '-oC1', label ='High')
ax16.plot(npc, B16_lo, '-oC2', label="Low")

ax16.axhline(y=0, color='grey', linestyle="--")

#legend
ax13.legend(loc='upper right', edgecolor='white', framealpha=1,
            title='Magnetometers')


plt.show()