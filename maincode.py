import IPython.display as ipd

import librosa

import librosa.display

import matplotlib.pyplot as plt


filename='Location_Here'
plt.figure(figsize=(14,5))
data,sr=librosa.load(filename)
librosa.display.waveplot(data,sr)
ipd.Audio(filename)
