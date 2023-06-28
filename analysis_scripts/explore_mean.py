#!/usr/bin/env python3

'''
This script creates a mean forecast by averaging the max db_h/dt values in a
twenty minutes time intervalfrom the five models used in Pulkkinen et al. 2013.
'''

import numpy as np
import multimodtools as mmt
import matplotlib.pyplot as plt

from argparse import ArgumentParser

parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mag", type=str, default='YKC',
                    help='Set the magnetometer to analyze: ABK, PBQ, ' +
                    'SNK, YKC, NEW, OTT, or WNG')

# Process arguments
args = parser.parse_args()

# script options into function arguments?
tab_kwargs = {'event_set': args.events, 'mag_set': args.mag, 'verbose': False}

# Loop over all models
t = {}
for m in mmt.models:
    t[m] = mmt.build_table(m, **tab_kwargs)

# Get time array into convenience variable:
plottime = t['9_SWMF'].time

# calculate mean
modmean = np.zeros(plottime.size)
for m in mmt.models:
    modmean += t[m].modmax
modmean /= 5

# plotting
plt.style.use('bmh')
fig = plt.figure(figsize=(10, 7))
a1, a2 = fig.subplots(2, 1)

fig.suptitle(f"Event: {tab_kwargs['event_set'][0]} " +
             f"Magnetometer(s): {tab_kwargs['mag_set']}", fontsize='16')

# First plot: validation plot - each models max compared to ensemble mean
for mod in mmt.modnames:
    a1.plot(plottime, t[mod].modmax, c=mmt.cols[mod],
            label=mmt.models[mod], alpha=0.75)
a1.plot(plottime, modmean, c='k', label='Ensemble Mean', linewidth=3)

a1.set_title('Ensemble Members')
a1.set_ylabel('dB/dt')
a1.set_xlabel('Time')

a1.legend(loc='upper right', edgecolor='white', framealpha=1)

# Second plot:
a2.plot(plottime, modmean, '-o', c='black', label='Ensemble Mean')
a2.plot(plottime, t['9_SWMF'].modmax, '-*', c='royalblue', label='SWMF',
        alpha=0.85)
a2.plot(plottime, t['9_SWMF'].obsmax, '-X', c='crimson', label='Observations',
        alpha=0.85)

a2.set_title('Ensemble Mean vs Determinsitc')
a2.set_ylabel('dB/dt')
a2.set_xlabel('Time')

a2.legend(loc='upper right', edgecolor='white', framealpha=1)
fig.tight_layout()
plt.show()
