import multimodtools as mmt
import matplotlib.pyplot as plt

t1 = mmt.build_table('2_LFM-MIX', event_set=[2], mag_set='ABK')
t2 = mmt.build_table('3_WEIGEL', event_set=[2], mag_set='ABK')
t3 = mmt.build_table('4_OPENGGCM', event_set=[2], mag_set='ABK')
t4 = mmt.build_table('6_WEIMER', event_set=[2], mag_set='ABK')
t5 = mmt.build_table('9_SWMF', event_set=[2], mag_set='ABK')

modmean = (t1.modmax + t2.modmax + t3.modmax + t4.modmax + t5.modmax)/5

# ploting
plt.style.use('fivethirtyeight')
plt.plot(t1.time, modmean, 'o')
plt.show()

# Combine arrys to find the median
stack = np.vstack([t['SWMF'].modmax, t['LFM-MIX'].modmax, t['OpenGGCM'].modmax, t['Weimer2010'].modmax, t['Weigel'].modmax])
median = np.median(stack, axis=0)