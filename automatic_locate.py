# -*- coding: UTF-8 -*-

'Manually locate alignment points'

__author__='Leslie Kuo'

from scipy.io import wavfile
import numpy as np
import padasip as pa
import ANCfunc as anc
from scipy import interpolate
import pylab as pl
from pylab import *

class AutoTimeDelayEstimation(object):
    def __init__(self, orate, u, v):
        self.rate = orate
        self.u = u
        self.v = v

    # def phase_shift(self,signal, phase):
    def phase_shift(self, phase):
        assert 0 <= phase <= 1
        x = np.arange(0, len(self.u))
        y = np.array(self.u)
        f = interpolate.interp1d(x, y)
        xnew = np.arange(phase, len(self.u) - 1, 1)
        self.u = f(xnew)

    def find_localmin_ref(self, ref):
        assert 20 <= ref <= 100
        min_result = (0, math.inf)
        for align in range(ref-20, ref+20):
            su = self.u[:-align]
            sv = self.v[align:]
            value_ave = np.average(np.abs(su - sv))
            # value_max = np.max(np.abs(su_-sv_))
            # value = min(value_ave,value_max)
            if value_ave < min_result[1]:
                min_result = (align, value_ave)
        return min_result
    def globalmin(self, ref):
        final_result = (0, math.inf)
        for i in range(8):
            phase = i * 0.125
            self.phase_shift(phase)
            minresult = self.find_localmin_ref(ref)

            if minresult[1] < final_result[1]:
                final_result = minresult
        return final_result

class ManualTimeDelayEstimation(object):
    pass


name = "830"

alignnum = 256 #for AUDIO.wav

su, sv, orate = anc.splitChannel("F:/AllProgram/pycharmPros/padasip/output/8.24/LS_LR.wav","interval_result")
print(orate)
# su, sv, orate = anc.splitChannel("F:/AllProgram/pycharmPros/padasip/723/726/interval_v23.wav","interval_result")

anc.plotfft2(sv, orate, 'before_sv')
anc.plotfft2(su, orate, 'before_su')

su_new8 = anc.test_interpolate_wav(su, 0.125)
sv_new8 = anc.test_interpolate_wav(sv, 0.125)
anc.plotfft2(sv_new8, orate*8, 'origin_sv')
test = anc.mergeChannel(su_new8, sv_new8, orate*8, str="831_8interpolate.wav")
(align_num_0, min_dist_0),uu,vv = anc.test(su_new8, sv_new8, 256)
test = anc.mergeChannel(uu, vv, orate*8, str="831_8align.wav")
tu,tv = anc.test_changeAmplitude(uu,vv,5.56)
test2 = anc.mergeChannel(tu, tv, orate*8, str="831_8Amplitude.wav")


# anc.plotfft2(sv, orate, 'origin_sv')
anc.plotfft2(tv, orate*8, 'amplitude_sv')


result = anc.subtract(tu,tv,5.56)
anc.plotfft2(result, orate*8, 'subtract_sv')
wavfile.write("./output/"+name+'831_result.wav', orate*8, result)


# if __name__ == '__main__':
#     main()