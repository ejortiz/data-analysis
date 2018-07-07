import thinkdsp
class SpectrumHelper:
    @staticmethod
    def get_spectrum_peaks_from(wave_obj, start=None, duration=None, peak_start_index=0, peak_end_index=30):
        trimmed_wave = wave_obj.segment(start, duration)
        spectrum = trimmed_wave.make_spectrum()
        spectrum_peaks = spectrum.peaks()[peak_start_index:peak_end_index]
        amplitudes = []
        frequencies = []
        for amplitude, frequency in spectrum_peaks:
            amplitudes.append(amplitude)
            frequencies.append(frequency)
        return amplitudes, frequencies
