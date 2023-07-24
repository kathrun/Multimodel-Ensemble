# /usr/bin/env python3
'''
Testing a modified threshold NPC. If working as intended create a script
to handle all events and mags.
'''

import numpy as np
from validator import BinaryEventTable
import multimodtools as mmt

# Set metric parameters added modthresh:
mag, event, thresh, modthresh = 'WNG', 7, 0.3, 0.205
tab_kwargs = {'event_set': [event], 'mag_set': [mag],
              'modthresh': modthresh}

# Create tables for all 5 models.
tables = {}
for m in mmt.models:
    tables[mmt.models[m]] = mmt.build_table(m, **tab_kwargs)

# Deterministic table for comparison
det_tab = mmt.build_table("9_SWMF", event, mag, thresh)

# Create NPC by counting the number of crossings in each bin
# across all ensemble members (i.e., models)
mod = np.zeros(det_tab.obsmax.size)
for tab in tables:
    mod += 1*tables[tab].bool

npc_forecast = 1.1 * thresh * (mod >= 2)
npc_tab = BinaryEventTable(det_tab.tObs, det_tab.Obs, det_tab.time,
                           npc_forecast, modthresh, trange=mmt.tlims[event],
                           window=20*60)

# Now, make some sweet sweet metrics.
swmf = det_tab
print(f'Station: {mag}\tEvent: {event}\tThreshold: {thresh}\tModified Threshold: {modthresh}')
print(f'Deterministic Forecast:\n\tPoD = {swmf.calc_HR()}\n\tPoFD = {swmf.calc_FARate()} \n\tHSS = {swmf.calc_heidke()}\n\tBias = {swmf.calc_bias()}')
print(f'Ensemble Forecast:\n\tPoD = {npc_tab.calc_HR()}\n\tPoFD = {npc_tab.calc_FARate()} \n\tHSS = {npc_tab.calc_heidke()}\n\tBias = {npc_tab.calc_bias()}')