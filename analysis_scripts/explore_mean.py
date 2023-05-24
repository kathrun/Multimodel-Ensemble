import numpy as np
import multimodtools as mmt
import matplotlib.pyplot as plt

from argparse import ArgumentParser
parser = ArgumentParser(description=__doc__)
parser.add_argument("-e", "--events", type=int, nargs='+',
                    default=[1],
                    help="Set the events to analyze via list of event number,"
                    + "e.g., --events 1 2 7 8")
parser.add_argument("-m", "--mags", nargs='+', type=str,
                    default='YKC',
                    help= 'Set the magnetometer to analyze: ABK, PBQ, SNK, YKC, NEW, OTT, or WNG')

# Process arguments
args = parser.parse_args()

#script options into function arguments?
tab_kwargs = {'event_set':args.events, 'mag_set':args.mags, 'verbose':False}

#Loop over all models
t = {}
for m in mmt.models:
    t[mmt.models[m]] = mmt.build_table(m, **tab_kwargs)


#calculate mean
modmean = (t['SWMF'].modmax + t['LFM-MIX'].modmax + t['OpenGGCM'].modmax + t['Weimer2010'].modmax + t['Weigel'].modmax)/5


#plotting
fig = plt.figure(figsize=(10,7))
a1, a2 = fig.subplots(2,1)

fig.suptitle(f"Event: {tab_kwargs['event_set'][0]} Magnetometer: {tab_kwargs['mag_set']}", fontsize = '16')
plt.style.use('bmh')

#First plot: validation plot - each models max compared to ensemble mean
a1.plot(t['SWMF'].time, t['LFM-MIX'].modmax, c = 'gold', label ='LFM-Mix', alpha = 0.75)
a1.plot(t['SWMF'].time, t['Weigel'].modmax, c = 'firebrick', label ='Weigel', alpha = 0.75)
a1.plot(t['SWMF'].time, t['OpenGGCM'].modmax, c = 'darkorange', label ='OpenGGCM', alpha = 0.75)
a1.plot(t['SWMF'].time, t['Weimer2010'].modmax, c = 'olivedrab', label ='Weimer', alpha = 0.75)
a1.plot(t['SWMF'].time, t['SWMF'].modmax, c = 'royalblue', label ='SWMF', alpha = 0.75)
a1.plot(t['SWMF'].time, modmean, c = 'black', label = 'Ensemble Mean', linewidth = 3)

a1.set_title('Ensemble Members')
a1.set_ylabel('dB/dt')
a1.set_xlabel('Time')

a1.legend(loc='upper right', edgecolor='white', framealpha=1)

#Second plot: 
a2.plot(t['SWMF'].time, modmean,'-o', c = 'black', label = 'Ensemble Mean')
a2.plot(t['SWMF'].time, t['SWMF'].modmax, '-*', c='royalblue', label ='SWMF', alpha = 0.85)
a2.plot(t['SWMF'].time, t['SWMF'].obsmax, '-X', c='crimson', label = 'Observations', alpha = 0.85)

a2.set_title('Ensemble Mean vs Determinsitc')
a2.set_ylabel('dB/dt')
a2.set_xlabel('Time')

a2.legend(loc='upper right', edgecolor='white', framealpha=1)

plt.show()