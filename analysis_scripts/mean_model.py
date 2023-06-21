#Attempt to recreate model data output files for mean 'model'

import os, sys
from datetime import datetime, timedelta
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt

from spacepy.plot import style, applySmartTimeTicks
from validator import BinaryEventTable
import multimodtools as mmt

### Argparser lines in order to change the event, station, and model
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mags", nargs='+', type=str,
                    default='YKC',
                    help= 'Set the magnetometer to analyze: ABK, PBQ, SNK, YKC, NEW, OTT, or WNG')
parser.add_argument("-d", "--debug", action="store_true",
                    help="Turn on debug mode: additional print statements, " +
                    "output saved in 'debug/' folder")

# Process arguments
args = parser.parse_args()

#script options into function arguments?
tab_kwargs = {'event_set':args.events, 'mag_set':args.mags, 'verbose':False}

#Calculate Mean Model
#Loop over all models
t = {}
for m in mmt.models:
    t[mmt.models[m]] = mmt.build_table(m, **tab_kwargs)


#calculate mean
modmean = (t['SWMF'].modmax + t['LFM-MIX'].modmax + t['OpenGGCM'].modmax + t['Weimer2010'].modmax + t['Weigel'].modmax)/5

# Path to output directory
now = datetime.now()

fulldir = f"Mean_{now:%Y%m%dT%H%M}"
outdir = 'mean_debug/' if args.debug else fulldir

# Create directory if it doesn't exist:
if not os.path.exists(outdir) and not(args.debug):
    os.mkdir(outdir)

# Create ascii output file, switch to stdout if in debug mode:
if args.debug:
    outfile = sys.stdout
else:
    outfile = open(outdir+'Mean Forecast.txt', 'w')

# Print info 
outfile.write(f"# run: Mean_{now:%Y%m%dT}\n")
outfile.write(f"# model: Mean\n")
outfile.write(f"# Shielding angle [deg.]:      -90.0000\n")
outfile.write(f"# North, East and vertical components of magnetic field\n")
outfile.write(f"# Station: {args.mags}\n")
outfile.write(f"#Position (GEO): lon=        lat=      \n") #Hard code or utilize argparse
outfile.write(f"Year Month Day Hour Min Sec GeomagLat GeomagLon dBdt_Horizonatl \n")
outfile.write(f"[year] [month] [day] [hour] [min] [s] [deg] [deg] [nT/s]\n\n")

#trying to fill array properly formated
#this took me way longer to figre out than it should have 
#datetime: ?????? 
#only have db_h not each component...
for x in (modmean):
    outfile.write('{0}     {1}     {2}     {3}     {4}     {5}     {6}     {7}     {8}\n'.format('year','month','day','hour','min', 'sec',65.1120,102.3080, '{:.5f}'.format(x)))

if not args.debug:
    outfile.close()
#not creating .txt file into the right folder?