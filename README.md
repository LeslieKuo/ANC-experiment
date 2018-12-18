"# ANC-experiment" 
Adaptive Noise Cancellation :actual experiment STM32F4 records signal and drone noise with a common I2S bus to collecting sounds synchronously. The noise mixed signal input is the reference input of the ANC system. The signal mixed heavy noise input is the origial input of the ANC system. The noise process project mainly consists of 2 parts：

signal preprocessing.Namely, two-channel sound timeline alignment(based on the noise timeline alignment)

Using adaptive algorithm to finish ANC

What's more, the timeline alignment includs 2 steps

(1)Manual locate the align timeline point

(2)Automatic locate
