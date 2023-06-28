#!/usr/bin/env python3

'''
This script creates a median forecast model output by averaging the max 
db_h/dt values in a twenty minutes time interval from the five models used in 
Pulkkinen et al. 2013.

Note: Lat. and Lon. are hard coded in.
'''

import os
import sys
from datetime import datetime, timedelta
from argparse import ArgumentParser

import numpy as np

from validator import BinaryEventTable
import multimodtools as mmt

# Argparser lines in order to change the event, station, and model
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--event", type=int, default=1,
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mag", type=str, default='YKC',
                    help='Set the magnetometer to analyze: ABK, PBQ, ' +
                    'SNK, YKC, NEW, OTT, or WNG')
parser.add_argument("-d", "--debug", action="store_true",
                    help="Turn on debug mode: additional print statements, " +
                    "output saved in 'debug/' folder")

# Process arguments
args = parser.parse_args()

# script options into function arguments?
tab_kwargs = {'event_set': args.event, 'mag_set': args.mag, 'verbose': False}

# Calculate Median Model
# Loop over all models
t = {}
for m in mmt.models:
    t[m] = mmt.build_table(m, **tab_kwargs)

# Get time array into convenience variable:
plottime = t['9_SWMF'].time
modmedian = np.zeros(plottime.size)

# Stack and calculate medians
modmedian = np.vstack([t['9_SWMF'].modmax, t['2_LFM-MIX'].modmax, t[
    '4_OPENGGCM'].modmax, t['6_WEIMER'].modmax, t['3_WEIGEL'].modmax])
modmedian = np.median(modmedian, axis=0)

# Path to output directory
now = datetime.now()

# Create ascii output file, switch to stdout if in debug mode:
if args.debug:
    outfile = sys.stdout
else:
    outfile = open(f'{args.mag}_Median_Event{args.event}.txt', 'w')

# Print info 
outfile.write(f"# run: Median_{now:%Y%m%d}\n")
outfile.write("# model: Median\n")
outfile.write("# Shielding angle [deg.]:      -90.0000\n")
outfile.write("# North, East and vertical components of magnetic field\n")
outfile.write(f"# Station: {args.mag}\n")
outfile.write("#Position (GEO): lon=       242.880 lat=      62.4830\n")
# Hard code or utilize argparse
outfile.write("Year Month Day Hour Min Sec GeomagLat GeomagLon dBdt_Horizonatl\n")
outfile.write("[year] [month] [day] [hour] [min] [s] [deg] [deg] [nT/s]\n\n")

# Trying to fill array properly formated
# This took me way longer to figre out than it should have 
# Datetime: ?????? 
# Only have db_h not each component...
for t, db in zip(plottime, modmedian): 
    outfile.write('{0}     {1}     {2}     {3}\n'
                  .format(t.strftime('%Y %m %d %H %M %S'), 69.7140, 299.3950,
                          '{:.5f}'.format(db)))

if not args.debug:
    outfile.close()
# Not creating .txt file into the right folder?