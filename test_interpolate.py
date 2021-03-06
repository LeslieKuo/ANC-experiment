# !/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import pylab as pl

x = np.linspace(0, 10, 11)
print(type(x))
m = np.arange(8)
print(type(m))
# x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
y = np.sin(x)
xnew = np.linspace(0, 10, 101)
pl.plot(x, y, "ro")

for kind in ["nearest", "zero", "slinear"]:  # 插值方式
#for kind in ["nearest", "zero", "slinear", "quadratic", "cubic"]:  # 插值方式
    # "nearest","zero"为阶梯插值
    # slinear 线性插值
    # "quadratic","cubic" 为2阶、3阶B样条曲线插值
    f = interpolate.interp1d(x, y, kind=kind)
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    ynew = f(xnew)
    print(type(ynew))
    print("the len of origin is ",len(ynew))
    you = ynew[::8]
    print("the type of ynew[::8] is ",type(you))
    slice = []
    slice.append(ynew[::8])
    slice.append(ynew[1::8])
    slice.append(ynew[2::8])
    print(len(slice))
    print("the len of slice is ",len(slice))
    print("the type of slice is ",type(slice))
    print(ynew)
    print(slice[0])
    print(slice[1])
    pl.plot(xnew, ynew, label=str(kind))
pl.legend(loc="lower right")
pl.show()
