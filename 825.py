#This file is made by using time field shuffle to reduce noise
#Example: ../mic/AUDIO1.wav
#Manual measure result: delta T = 56 point Rdelay，cutRtail. Power R0.025 L0.08
from scipy.io import wavfile
import numpy as np
import padasip as pa
import ANCfunc as anc

name = "interval_v23_"
# alignnum = 74 #for Vol20
# alignnum = 70 #for vol18
alignnum = 824 #for AUDIO.wav

su, sv, orate = anc.splitChannel("F:/AllProgram/pycharmPros/padasip/output/8.24/LS_LR.wav","interval_result")
# su, sv, orate = anc.splitChannel("F:/AllProgram/pycharmPros/padasip/723/726/sin1000vol18.wav","interval_result")
# su_new = anc.test_interpolate_wav(su,0.125)
# sv_new = anc.test_interpolate_wav(sv,0.125)
# test = anc.mergeChannel(su_new,sv_new,orate*8,str="825test_interpolate.wav")

wavfile.write("./output/8.24/"+'_824origin_sv.wav', orate, sv)
type1 = anc.mergeChannel(su,sv,orate,str="afterInverse"+str(alignnum)+".wav")

# anc.plotfft2(su, orate, 'origin_su')
anc.plotfft(su, orate, 'origin_su')
# anc.plotfft2(sv, orate, 'origin_sv')
anc.plotfft(sv, orate, 'origin_sv')

# # alignnum = 70 #for Val13
# su = su[:-alignnum]
# sv = sv[alignnum:]
# # su, sv = anc.correlationFunc(su, sv)

# anc.plotfft2(su, orate, ' u')
# anc.plotfft2(sv, orate, ' v')
# print("near noise data is ", su)
# print("near signal data is ", sv)
# type = anc.mergeChannel(su,sv,orate,str="afterAlign"+str(alignnum)+".wav")
#
# su, sv, key = anc.changeAmplitude(su, sv)
# type2 = anc.mergeChannel(su,sv,orate,str="afterChangeAmplit"+str(alignnum)+".wav")
# result = sv - su
# result = result/key
# result = result.astype(np.int16)
# # result = anc.boundary(result)
# # print(result.dtype)
#
#
# wavfile.write("./output/"+name+str(alignnum)+'_result.wav', orate, result)
# anc.plotfft2(result, orate, str(alignnum)+'result')
# anc.plotfft(result, orate, str(alignnum)+'result')

#测试插值
su, sv, key = anc.changeAmplitude(su, sv)
anc.plotfft(sv, orate, 'changeAmplitude_sv')
anc.plotfft2(sv, orate, 'changeAmplitude_sv')


type2 = anc.mergeChannel(su,sv,orate,str="afterChangeAmplit"+str(alignnum)+".wav")

ulist ,vlist = anc.interpolate_value(su, 0.125), anc.interpolate_value(sv, 0.125)
(align_num_0, min_dist_0) = anc.test(ulist[0], sv, 29)
(align_num_1, min_dist_1) = anc.test(ulist[1], sv, 29)
(align_num_2, min_dist_2) = anc.test(ulist[2], sv, 29)
(align_num_3, min_dist_3) = anc.test(ulist[3], sv, 29)
(align_num_4, min_dist_4) = anc.test(ulist[4], sv, 29)
(align_num_5, min_dist_5) = anc.test(ulist[5], sv, 29)
(align_num_6, min_dist_6) = anc.test(ulist[6], sv, 29)
(align_num_7, min_dist_7) = anc.test(ulist[7], sv, 29)
print("after interpolate 0.125 from 29 to 30")
print(align_num_0,min_dist_0)
print(align_num_1,min_dist_1)
print(align_num_2,min_dist_2)
print(align_num_3,min_dist_3)
print(align_num_4,min_dist_4)
print(align_num_5,min_dist_5)
print(align_num_6,min_dist_6)
print(align_num_7,min_dist_7)
print("that's all")

(num_,dist_) = anc.test(su,sv,30)
print("testnum is ", num_)
print("test dist is ", dist_)
(num, dist) = anc.align_ref(30,su,sv)
print("after align_ref, the align Num is ",num)
print("after align_ref, the dist is ",dist)
# succ, svcc = anc.correlationFunc(su, sv)
(align_num, min_dist) = anc.find_min_positition(su, sv)
print("After find min positition, min_dist is ",min_dist)
print("After find min position, align_num is ",align_num)
# num = 50
csu = su[:-num]
csv = sv[num:]
type = anc.mergeChannel(csu,csv,orate,str="afterAlign824"+str(num)+".wav")


#以上结果是已经对齐了，下边用直接相减的方法来去噪声
result = csv - csu
result = result/key
result_abs = np.abs(result)
result_abs = result_abs.astype(np.int16)
result = result.astype(np.int16)
# anc.plotfft2(result, orate, 'result')
wavfile.write("./output/8.24/"+name+str(num)+'_result.wav', orate, result)
# wavfile.write("./output/"+name+'_absresult.wav', orate, result_abs)


#以上为测试内容