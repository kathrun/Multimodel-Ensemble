#!/usr/bin/env python3

'''
Analyze a multi-model Naive Probabilistic Classifier ensemble forecast for
dB/dt. When called, a new folder will be created that contains the output
files, plots, and results.

Analysis builds on Pulkkinen et al., 2013: 6 stations, 6 events, binary event
analysis tools. See that manuscript for details.
'''

import os
from datetime import datetime, timedelta
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt

from spacepy.plot import style, applySmartTimeTicks
from validator import BinaryEventTable
import multimodtools as mmt

# Handle command-line arguments.
# Initialize argument parser:
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1, 2, 3, 4, 7, 8],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-d", "--debug", action="store_true",
                    help="Turn on debug mode: additional print statements, " +
                    "output saved in 'debug/' folder")
parser.add_argument("-t", "--threshold", type=float, default=0.3,
                    help="Set the threshold for dB/dt in the binary event" +
                    "analysis. Default is 0.3, standard values are " +
                    "0.3, 0.7, 1.1, and 1.5 nT/s.")
parser.add_argument("-n", "--n_models", type=int, default=2,
                    help="Set the number of models that must cross the dB/dt "+
                    "threshold in order for the NPC prediction to be counted " +
                    "as a 'hit'. Defaults to 2.")
parser.add_argument("-m", "--mags", nargs='+', type=str,
                    default=['all', 'hi', 'lo'],
                    help="Set which group of magnetometers to use. Can be a " +
                    "list of 3-letter magnetometer station name codes or a " +
                    "string indicating what group to use, e.g., 'hi', 'lo', " +
                    "'all' for high latitude, mid-latitude, or both. " +
                    "e.g., --mags all hi low pbq, would run 'hi' and 'low' " +
                    "magnetometers and the PBQ station by itself.")

# Process arguments:
args = parser.parse_args()

# Switch to spacepy's style:
style()

# Build output directory path (just "npc_debug" in debug mode...)
now = datetime.now() # Time of current run
t_str = f"{args.threshold:.2f}".replace('.', 'p')
ev_str = ''
for i in args.events:
    ev_str = ev_str + str(i)
fulldir = f"npc_e{ev_str}_t{t_str}_n{args.n_models}_{now:%Y%m%dT%H%M}/"
outdir = 'npc_debug/' if args.debug else fulldir

# Print info to screen:
print(f"Creating NPC analysis using following parameters:")
print(f"\tEvents = {args.events}")
print(f"\tThreshold = {args.threshold:0.2f}")
print(f"\tNumber of members required for NPC threshold crossing: {args.n_models}")
print(f"\tMagnetometer sets used: {args.mags}")
print(f'\tOutput directory (ignored in debug mode):')
print(f"\t\t{fulldir}")

# Create directory if it doesn't exist:
if not os.path.exists(outdir) and not(args.debug):
    os.mkdir(outdir)

####### Create top-level binary event tables and NPC #######
# Loop over the key mag groupings: all, hi, lo
for group in args.mags:
    # Turn our script options into function arguments:
    tab_kwargs = {'event_set':args.events, 'mag_set':group,
                  'thresh':args.threshold, 'verbose':False}

    # Create tables for all 5 models:
    tables = {}
    for m in mmt.models:
        tables[mmt.models[m]] = mmt.build_table(m, **tab_kwargs)

    # Create NPC by counting the number of crossings in each bin
    # across all ensemble members (i.e., models)
    npc_size, obs_size = tables['SWMF'].obsmax.size, tables['SWMF'].Obs.size
    mod = np.zeros(tables['SWMF'].obsmax.size)
    for tab in tables:
        mod += 1*tables[tab].bool
    npc_forecast = 1.1 * args.threshold * (mod>=2)

    # Create a synthetic time series to match the number of data points.
    # Doing this instead of relying on the original times, with multi-year
    # long gaps, greatly speeds processing.
    tstart = datetime(2000,1,1,0,0,0)
    t_npc = [tstart + timedelta(minutes=i*20 + 10) for i in range(npc_size)]
    t_npc = np.array(t_npc)

    # Build table using times/dates and observed values from all included
    # events, stored in any of the other tables (but we'll use SWMF for ease.)
    #npc_tab = BinaryEventTable(tables['SWMF'].tObs, tables['SWMF'].Obs,
    #                           tables['SWMF'].time, npc_forecast,
    npc_tab = BinaryEventTable(t_npc, tables['SWMF'].obsmax,
                               t_npc, npc_forecast,
                               args.threshold, window=20*60, verbose=False)
