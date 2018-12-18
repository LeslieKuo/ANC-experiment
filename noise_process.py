# !/usr/bin/env python
# -*- Coding = UTF-8 -*-

'Use padasip to process noise by Adaptive Noise Cancellion'

__author__ = 'Leslie Kuo'

def main():
    print("aaa")

if __name__ == '__main__':
    main()


# #plot drone noise frequency
# from scipy.io import wavfile
# import ANCfunc as anc
#
# drone = 'F:/AllProgram/pycharmPros/padasip/drone_noise/drone.wav'
# rate, musicData = wavfile.read(drone)
#
# print(rate)
# print(len(musicData))
# # su, sv, orate = anc.splitChannel("F:/AllProgram/pycharmPros/padasip/723/726/interval_v23.wav","interval_result")
#
# anc.plotfft2(musicData, rate, 'drone2')
# anc.plotfft(musicData, rate, 'drone')
# anc.plotfft2w(musicData, rate, 'drone2w')


#