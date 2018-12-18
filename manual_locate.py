# -*- coding: UTF-8 -*-

'Manually locate alignment points'

__author__='Leslie Kuo'

from scipy.io import wavfile
import numpy as np
import padasip as pa
import ANCfunc as anc

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