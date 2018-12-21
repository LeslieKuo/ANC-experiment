#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'experiment: mixed signal and noise manually to test the align function'

__author__ = 'Luna Lovegood'

import numpy as np
import padasip as pa
from scipy.io import wavfile

orate,signal = wavfile.read('s10.wav')
orate1,noise = wavfile.read('n10.wav')  #10s dryer noise
print("the signal type is ",signal.dtype)
delayPointNum = 30
print(noise.shape)
print(signal.shape)
cutHead_noise=noise[delayPointNum:]
cutTail_noise=noise[:441000-delayPointNum]
cutHead_signal=signal[delayPointNum:]
cutTail_signal = signal[:441000-delayPointNum]

#U = cutHead_noise + 0.05*cutTail_signal
U = cutHead_noise
V = 0.6*cutHead_signal + 0.9*cutTail_noise
# filtering
n = 20  # length of filter
Udelay = pa.input_from_history(U, n)[:-1]

Vdelay=V[n-1:-1]
f = pa.filters.FilterRLS(mu=0.99, n=n)
y, e, w = f.run(Vdelay, Udelay)
music = e.astype(signal.dtype)
music =music[44100:]
mmax =np.max(music)
print(mmax)
music = music*32768//mmax
print(np.max(music))
music = music.astype(signal.dtype)
UU = U.astype(signal.dtype)
VV = V.astype(signal.dtype)

wavfile.write('ex8Signal.wav',orate,signal)
wavfile.write('ex8Noise.wav',orate,noise)
wavfile.write('ex8U.wav',orate,UU)
wavfile.write('ex8V.wav',orate,VV)
wavfile.write('ex8result30.wav',orate,music)