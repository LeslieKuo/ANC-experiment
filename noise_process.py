# !/usr/bin/env python
# -*- Coding = UTF-8 -*-

'Use padasip to process noise based on Adaptive Noise Cancellion Algorithm'

__author__ = 'Leslie Kuo'

# import ANCfunc as anc
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


#simulation
# su, sv, orate = anc.splitChannel("F:/AllProgram/pycharmPros/padasip/723/sweep20-20k.wav","raw_manual")
#
# anc.plotfft2(su, orate, 'origin_sv')
# anc.plotfft(su, orate, 'origin_sv')

# orate, signal = wavfile.read('ex9splitU.wav')
# orate2, noise = wavfile.read('ex9splitV.wav')
# u,v = anc.pre_combine(signal, noise, 0.1,1,0.2,0.9,1,-1,-1,1)
# wavfile.write('ex9combineU.wav',orate, u)
# wavfile.write('ex9combineV.wav',orate, v)
# su,sv = anc.pre_combine(3000,signal, noise, 0.1,1,0.2,0.6,1,-1,-1,1)
# wavfile.write('ex9combineU.wav', orate, su)
# wavfile.write('ex9combineV.wav', orate, sv)





# u ,v = signal,noise
# u, v = anc.correlationFunc(u, v)
# print(type(u))
# wavfile.write('ex9corru.wav', orate, u)
# wavfile.write('ex9corrv.wav', orate, v)
# music = anc.ANC_filter(u, v)
# wavfile.write('ex9filtermusic.wav', orate, music)
