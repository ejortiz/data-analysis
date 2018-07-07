"""
This file will be used as a test using Allen Downey's ThinkDSP library
"""
import matplotlib.pyplot as plt
import thinkdsp
from SpectrumHelper import SpectrumHelper

audio_file = 'audio_files/sample-clap.wav'

sample_wave = thinkdsp.read_wave(audio_file)
# pusherman_wave.truncate(pusherman_wave.find_index(30))  # trim the wave to the first 30 seconds


sample_wave = sample_wave.segment(0, 100)  # also trims wave from 0 to 30
sample_wave.normalize()
#
amplitudes, frequencies = SpectrumHelper.get_spectrum_peaks_from(sample_wave, 0, 10, 0, 30)
plt.plot(frequencies, amplitudes, 'ro')
plt.xlabel('frequencies')
plt.ylabel('amplitudes')
plt.show()

plt.plot(sample_wave.ts, sample_wave.ys)
plt.show()




