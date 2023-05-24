#!/usr/bin/env python
'''
CCMC has *many* issues with their file formats, including double-headers and
incorrect units.  Let's write a script to dig through the files and correct
this behavior.

This script is pretty hacky, but we just need to fix these files.
'''

import os

def fix_file(f, ftype='dBdt', replace=True):
    '''
    Open text data file *f*, read header, and fix as necessary.

    Returns boolean indicating action taken:
       True:  File was incorrect, now fixed.
       False: File was fine, no action taken.
    '''

    units = 'nT' if ftype=='B' else 'nT/s'
    
    # Set correct header based on expected file type (B vs. dB/dt):
    header = f'''Year Month Day Hour Min Sec GeomagLat GeomagLon {ftype}_NorthGeomag {ftype}_EastGeomag {ftype}_DownGeomag
[year] [month] [day] [hour] [min] [s] [deg] [deg] [{units}] [{units}] [{units}]
'''
    
    with open(f, 'r') as infile:

        # Load hash-tag-prefixed lines:
        prehead = [infile.readline()]
        while prehead[-1][0] == '#':
            prehead.append(infile.readline())

        # Pop the final line:
        line = prehead.pop(-1)

        # Check if this is the expected header:
        if ftype in line:
            # File is fine, return False to indicate no action taken.
            return False
        else:
            # File is borked; cycle through bad header.
            while 'year' in line.lower():
                line = infile.readline()

        # Create temporary file, dump preheader and header to it.
        with open('tmp.txt', 'w') as outfile:
            # Dump pre-header (hashtagged lines) to file:
            for l in prehead:
                outfile.write(l)
            # Add corrected header w/ correct units:
            outfile.write(header)
            # Dump our first line of data:
            outfile.write(line)
            # Read and dump rest of data:
            for l in infile.readlines():
                outfile.write(l)

    # Replace bad file with good file:
    if replace:
        os.rename('tmp.txt', f)

    return True
        
if __name__ == '__main__':

    from multimodtools import tlims, models, allmag, datadir

    # How many files are we fixing? Keep track!
    nFixed = 0
    
    # Right now, only correct observation files.
    # Loop over all events and stations like so:
    for ev in [1,2,3,4,7,8]:
        for mag in allmag:
            for t in ['dBdt', 'deltaB']:
                # Set our file type based on our path:
                ftype = t
                if 'delta' in ftype: ftype='B'

                # File we want to change:
                f_obs=datadir+f'/dBdt/Event{ev}/Observations/{mag.lower()}' \
                    + f'_OBS_{tlims[ev][0]:%Y%m%d}.txt'

                # It may not exist- not all mags for all events.
                if not os.path.exists(f_obs): continue

                # If it does exist, fix!
                result = fix_file(f_obs, ftype=ftype, replace=True)

                # Count up those effed files.
                nFixed += 1*result

                if result: print(f"FIXED file {f_obs}")


    # Print status report:
    print(f"\nI fixed {nFixed} files.")
