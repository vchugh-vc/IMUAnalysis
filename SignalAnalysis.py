from FeatureClass import DataPreparation, Features
import pandas as pd
import numpy
from scipy.signal import butter, lfilter
from DTW import DataTimeWarping
from FrailtyIndex import Frailty
import matplotlib.pyplot as plt

FILE = 'CollectionData/2024-03-05-P1-Dom-3.csv'

FilteredData = DataPreparation(file=FILE)
AccZ = FilteredData.AccZ_Trimmed
AccX = FilteredData.AccX_Trimmed
DTWPhases = DataTimeWarping(AccZ, AccX)
TimeStamps = DTWPhases.movement_stamps
up_data = Features(FilteredData, TimeStamps, 'up')
middle_data = Features(FilteredData, TimeStamps, 'middle')
Frailty(up_data, middle_data)


def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Jerk = DataFeatures.Jerk
# AccX = DataFeatures.AccX
# AccY = DataFeatures.AccY
# AccZ = DataFeatures.AccZ
# Jerk_RMS = numpy.sqrt(numpy.mean(Jerk ** 2))
# print(f"Average Jerk of Movement: {Jerk_RMS} m/s-3")
# print(f"Length of movemenet {len(Jerk)} at {DataFeatures.time}")
# print(f"Dominant Freq is {DataFeatures.FFTFreq}")


# new = butter_lowpass_filter(FilteredData.AccZ_Trimmed, 5, 104, 6)
# plt.subplot(2, 1, 1)
# plt.plot(FilteredData.AccZ_Trimmed)
# plt.subplot(2, 1, 2)
# plt.plot(new)
# plt.show()


def minmax_spread(array):  # Returns Min-Max Data of an Array
    max_data = max(array)
    min_data = min(array)
    minmax_data = max_data - min_data
    peak_data = max(max_data, min_data)
    rms_data = numpy.sqrt(numpy.mean(array ** 2))
    std_data = numpy.nanstd(array)
    var_data = numpy.nanvar(array)
    print(
        f"Max: {max_data}, Min: {min_data}, Range : {minmax_data}, Peak {peak_data}, RMS {rms_data}, STD {std_data}, Var {var_data}")

