# -*- coding: UTF-8 -*-

'Manually locate alignment points in triple interval 800_1200_1600hz on March 11th'

__author__ = 'Leslie Kuo'


from scipy.io import wavfile
import numpy as np
import padasip as pa
import ANCfunc as anc

name = "2019March"
date = "3.11"

alignnum = 256 # the alin number of the record result audio by eyes

su, sv, orate = anc.splitChannel("F:/AllProgram/pycharmPros/Align_Nov13/March_test_audio/trip_result1.wav","March_interval_result")
print(orate)

# Plot the frequency spectrum of the split channel
anc.plotfft2(sv, orate, 'before_sv')
anc.plotfft2(su, orate, 'before_su')

# Octave interpolate
# pay attention the sample rate changes. new rate = rate*8
su_new8 = anc.test_interpolate_wav(su, 0.125)
sv_new8 = anc.test_interpolate_wav(sv, 0.125)
anc.plotfft2(sv_new8, orate*8, 'origin_sv')
test = anc.mergeChannel(su_new8, sv_new8, orate*8, str=date+"afterOctave.wav")

# 根据刚才afterOctave 的八倍内插结果 肉眼找到对齐点
# amplitude_subtract 对齐结果相减
(align_num_0, min_dist_0),uu,vv = anc.amplitude_subtract(su_new8, sv_new8, 256)
test = anc.mergeChannel(uu, vv, orate*8, str=date+"afterSubtract.wav")
tu,tv = anc.test_changeAmplitude(uu,vv,5.56)
test2 = anc.mergeChannel(tu, tv, orate*8, str=date+"afterAmplitude.wav")


# anc.plotfft2(sv, orate, 'origin_sv')
# anc.plotfft2(tv, orate*8, 'amplitude_sv')
#
#
# result = anc.subtract(tu,tv,5.56)
# anc.plotfft2(result, orate*8, 'subtract_sv')
# wavfile.write("./output/"+name+'831_result.wav', orate*8, result)


# if __name__ == '__main__':
#     main()