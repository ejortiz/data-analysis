"""
This file will be used as a test using Allen Downey's ThinkDSP library
"""
import matplotlib.pyplot as plt
import thinkdsp
import numpy as np
from SpectrumHelper import SpectrumHelper

audio_file = 'audio_files/pusherman.wav'

pusherman_wave = thinkdsp.read_wave(audio_file)
# pusherman_wave.truncate(pusherman_wave.find_index(30))  # trim the wave to the first 30 seconds


pusherman_wave_segment = pusherman_wave.segment(0, 8)  # also trims wave from 0 to 30
pusherman_wave_segment.normalize()
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

plt.plot(np.array(pusherman_wave_segment.ts), np.array(pusherman_wave_segment.ys), color='blue')
plt.plot(np.array(pusherman_wave_segment.ts), np.square(np.array(pusherman_wave_segment.ys)), color='red')
plt.show()


print(len(np.array(pusherman_wave_segment.ts)))
print(len(np.square(np.array(pusherman_wave_segment.ts))))

