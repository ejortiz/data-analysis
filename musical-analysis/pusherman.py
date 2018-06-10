"""
This file will be used as a test using Allen Downey's ThinkDSP library
"""
import matplotlib.pyplot as plt
import thinkdsp
from SpectrumHelper import SpectrumHelper

audio_file = 'audio_files/pusherman.wav'

pusherman_wave = thinkdsp.read_wave(audio_file)
# pusherman_wave.truncate(pusherman_wave.find_index(30))  # trim the wave to the first 30 seconds


pusherman_wave = pusherman_wave.segment(0, 100)  # also trims wave from 0 to 30

# pusherman_wave.normalize()
# pusherman_wave.plot()
# spectrum = pusherman_wave.make_spectrum()
# spectrum_peaks = spectrum.peaks()[0:30]
# plt.plot(spectrum_peaks[0], spectrum_peaks[1])
# plt.show()
#
amplitudes, frequencies = SpectrumHelper.get_spectrum_peaks_from(pusherman_wave, 0, 10, 0, 30)
plt.plot(frequencies, amplitudes, 'ro')
plt.xlabel('frequencies')
plt.ylabel('amplitudes')
plt.show()




