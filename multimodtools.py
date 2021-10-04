#!/usr/bin/env python3

'''
This is the top-level module for the MultiModel Ensemble study.
It contains tools to read data files, create ensembles, etc.
'''

import datetime as dt

import numpy as np
from dateutil.parser import parse as par

# Get install directory:
install_dir = '/'.join(__loader__.path.split('/')[:-1])+'/'

# Critical constants for handling SWPC events/models/stations etc.
models = {'2_LFM-MIX':'LFM-MIX',
          '3_WEIGEL':'Weigel',
          '4_OPENGGCM':'OpenGGCM',
          '6_WEIMER':'Weimer2010',
          '9_SWMF':'SWMF'}

hilat = ['PBQ', 'SNK', 'ABK', 'YKC']
lolat = ['WNG', 'NEW', 'OTT']

# Time limits of the events:
tlims={1:(par('October 29th, 2003 06:00UT', ignoretz=True),
          par('October 30th, 2003 06:00UT', ignoretz=True)),
       2:(par('December 14, 2006 12:00 UT', ignoretz=True),
          par('December 16, 2006 00:00 UT', ignoretz=True)),
       3:(par('August 31, 2001 00:00 UT',   ignoretz=True),
          par('September 1, 2001 00:00 UT', ignoretz=True)),
       4:(par('August 31, 2005 10:00 UT',   ignoretz=True),
          par('September 1, 2005 12:00 UT', ignoretz=True)),
       7:(par('April 5, 2010 00:00 UT',     ignoretz=True),
          par('April 6, 2010, 00:00 UT',    ignoretz=True)),
       8:(par('August 5, 2011 09:00 UT',    ignoretz=True),
          par('August 6, 2011, 09:00 UT',   ignoretz=True))}

def read_ccmcfile(filename):
    '''
    Read and parse a single SWPC file.
    
    Results are returned as a dictionary containing 'time', the three 
    components of either deltaB (perturbation of field from quiet time
    values) or dB/dt in N-E-Z coordinates, and the "H" component (tangent
    to surface) as defined in the Pulkkinen et al study.

    File 
    '''

    # Start by opening our file:
    with open(filename, 'r') as f:
        # Parse header- we only care about figuring out if this is a
        # deltaB or dB/dt file.  This will be given in the variable name
        # line.
        trash = '    '
        while trash[:4] != 'Year':
            trash = f.readline()

        # Look for dBdt in variable names to determine data type:
        is_dBdt = True if 'dBdt' in trash else False

        # Skip units line:
        trash = f.readline()

        # Slurp remainder of file:
        lines = f.readlines()
        
    # Create output container:
    data = {}  # Empty dictionary
    nlines = len(lines)  # number of data entries

    # Time is a special data type (datetimes):
    data['time'] = np.zeros(nlines, dtype=object)

    # All others get set based on type of data in file:
    for v in ['bn','be','bz']:
        data['d'*is_dBdt + v] = np.zeros(nlines)

    # Loop through and parse all data lines:
    for i, l in enumerate(lines):
        parts = l.split()

        # Extract date time:
        t = ' '.join(parts[:6])
        data['time'][i] = dt.datetime.strptime(t, '%Y %m %d %H %M %S')
        
        # Parse remaining values:
        for v, x in zip(['bn','be','bz'], parts[-3:]):
            data['d'*is_dBdt + v][i] = x

    # Calculate h component:
    data['d'*is_dBdt + 'bh'] = np.sqrt(data['d'*is_dBdt + 'bn']**2 +
                                       data['d'*is_dBdt + 'be']**2)
    
    # Return data object to caller:
    return data
