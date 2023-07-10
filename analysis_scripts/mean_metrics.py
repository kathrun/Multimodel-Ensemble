#!/usr/bin/env python3

'''
Small script to create forecast metric comparison between mean and
deterministic forecasts.
'''
from argparse import ArgumentParser

import multimodtools as mmt

# Argparser lines in order to change the event, station, and model
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--event", type=int, default=1,
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mag", type=str, default='YKC',
                    help='Set the magnetometer to analyze: ABK, PBQ, ' +
                    'SNK, YKC, NEW, OTT, or WNG')
parser.add_argument("-t", "--thresh", type=float, default=0.3,
                    help="Set the threshold to analyze: 0.3, 0.7, 1.1, or 1.5")
parser.add_argument("-d", "--debug", action="store_true",
                    help="Turn on debug mode")

# Process arguments
args = parser.parse_args()

# script options into function arguments?
tab_kwargs = {'event_set': args.event, 'mag_set': args.mag, 'thresh': args.thresh}

swmf = mmt.build_table('9_SWMF', **tab_kwargs)
mean_tab = mmt.build_table('Mean', **tab_kwargs)

print(f'Station: {args.mag}\tEvent: {args.event}\tThreshold: {args.thresh}')
print('Metric | Determ | Ensemb | Diff \n')
print('----------------------------------\n')
print(f"  PoD  | {swmf.calc_HR():+6.3f} | {mean_tab.calc_HR():+6.3f} |" +
      f" {mean_tab.calc_HR() - swmf.calc_HR():+6.3f}\n")
print(f"  PoFD | {swmf.calc_FARate():+6.3f} | {mean_tab.calc_FARate():+6.3f} |" +
      f" {mean_tab.calc_FARate() - swmf.calc_FARate():+6.3f}\n")
print(f"  HSS  | {swmf.calc_heidke():+6.3f} | {mean_tab.calc_heidke():+6.3f} |" +
      f" {mean_tab.calc_heidke() - swmf.calc_heidke():+6.3f}\n")
print(f"  Bias | {swmf.calc_bias():+6.3f} | {mean_tab.calc_bias():+6.3f} |" +
      f" {mean_tab.calc_bias() - swmf.calc_bias():+6.3f}\n\n")