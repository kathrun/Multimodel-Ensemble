#!/usr/bin/env python3

'''
Explore impacts of changing model's threshold (but not obs. threshold).
'''

import numpy as np
import multimodtools as mmt
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Create arrays of lowered thresholds.
thresh = .3
tScaled = np.linspace(0, .9 * thresh, 21)
threshes = thresh - tScaled

# Create an empty dictionary to store results.
results = {}

# Loop over all models.
for m in mmt.models:

    # Create a set of containers for the results of changing
    # the model thresholds.
    heidke = np.zeros(tScaled.size)
    bias = np.zeros(tScaled.size)
    pod = np.zeros(tScaled.size)
    pofd = np.zeros(tScaled.size)

    # Loop over all thresholds.
    for i, dthresh in enumerate(tScaled):
        # Create the table for the given threshold:
        table = mmt.build_table(m, thresh=thresh - dthresh)

        # Calculate and stash the associated metrics:
        heidke[i] = table.calc_heidke()
        bias[i] = table.calc_bias()
        pod[i] = table.calc_HR()
        pofd[i] = table.calc_FARate()

    # Stash the result in the results dictionary:
    results[m] = {'heidke': heidke,
                  'bias': bias,
                  'pod': pod,
                  'pofd': pofd}

# Create a figure to plot results:
fig, axes = plt.subplots(2, 2, figsize=[8, 8])
axes = axes.flatten()

# Plot'em.
for m in mmt.models:
    axes[0].plot(threshes, results[m]['heidke'], label=mmt.models[m])
    axes[1].plot(threshes, results[m]['bias'], label=None)
    axes[2].plot(threshes, results[m]['pod'], label=None)
    axes[3].plot(threshes, results[m]['pofd'], label=None)

# Details details.
fig.legend(loc='lower center', ncol=3)
labs = ('Heidke Skill Score', 'Bias', 'Prob. of Detection', 'False Alarm Rate')
for ax, lab in zip(axes, labs):
    ax.set_ylabel(lab)
    ax.set_xlabel('dB/dt Threshold')
fig.suptitle('Forecast vs. Model Threshold')

# These values create a nice, tight figure with the figure legend:
fig.subplots_adjust(top=0.949, bottom=0.167, left=0.107,
                    right=0.972, hspace=0.26, wspace=0.286)

#for finding max threshold
y_h = heidke.argmax()
print("Heidke Max Threshold:", threshes.take(y_h))

y_b = bias.argmax()
print("Bias Max Threshold:", threshes.take(y_b))

y_PoD = pod.argmax()
print("PoD Max Threshold:", threshes.take(y_PoD))

y_PoFD = bias.argmax()
print("PoFD Max Threshold:", threshes.take(y_PoFD))