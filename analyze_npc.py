#!/usr/bin/env python3

'''
Analyze a multi-model Naive Probabilistic Classifier ensemble forecast for
dB/dt. When called, a new folder will be created that contains the output
files, plots, and results.

Analysis builds on Pulkkinen et al., 2013: 6 stations, 6 events, binary event
analysis tools. See that manuscript for details.
'''

import os
from datetime import datetime
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt

from spacepy.plot import style, applySmartTimeTicks
from validator import BinaryEventTable
import multimodtools as mmt

# Handle command-line arguments.
# Initialize argument parser:
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--event", type=int, default=1,
                    help="Set the event to analyze by event number (1-6).")
parser.add_argument("-d", "--debug", action="store_true",
                    help="Turn on debug mode: additional print statements, " +
                    "output saved in 'debug/' folder")
parser.add_argument("-t", "--threshold", type=float, default=0.3,
                    help="Set the threshold for dB/dt in the binary event" +
                    "analysis. Default is 0.3, standard values are " +
                    "0.3, 0.7, 1.1, and 1.5 nT/s.")
parser.add_argument("-n", "-n_models", type=int, default=2,
                    help="Set the number of models that must cross the dB/dt "+
                    "threshold in order for the NPC prediction to be counted " +
                    "as a 'hit'. Defaults to 2.")

# Process arguments:
args = parser.parse_args()

# Switch to spacepy's style:
style()

# Build output directory path (just "npc_debug" in debug mode...)
now = datetime.now() # Time of current run
t_str = f"{args.threshold:.2f}".replace('.', 'p')
fulldir = f"npc_e{args.event}_t{t_str}_{now:%Y%m%dT%H%M}/"
outdir = 'npc_debug/' if args.debug else fulldir

if args.debug:
    print('Output directory (ignored in debug mode):')
    print(f"\t{fulldir}")

# Create directory if it doesn't exist:
if not os.path.exists(outdir):
    os.mkdir(outdir)