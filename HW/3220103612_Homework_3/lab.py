
##最小二乘法
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.rcParams['font.sans-serif'] = ['SimHei']

Xi = np.array([0.041666667,	0.037037037,	0.033333333	,0.03030303	,0.027777778	,0.025641026,	0.023809524	,0.022222222	,0.020833333,	0.019607843
])
Yi = np.array([0.03058104	,0.027472527	,0.024813896,	0.022675737	,0.021052632	,0.019569472,	0.018281536,	0.017211704	,0.016260163	,0.015384615
])


def func(p, x):
    k, b = p
    return k * x + b
def error(p, x, y):
    return func(p, x) - y


p0 = [1, 1]

Para = leastsq(error, p0, args=(Xi, Yi))

k, b = Para[0]
print("k=", k, "b=", b)
print("cost：" + str(Para[1]))
print("求解的拟合直线为:")
print("y=" + str(round(k, 4)) + "x+" + str(round(b, 4)))

plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color="green", label="样本数据", linewidth=2)

x = np.array([0.041666667,	0.037037037,	0.033333333	,0.03030303	,0.027777778	,0.025641026,	0.023809524	,0.022222222	,0.020833333,	0.019607843])
y = k * x + b
plt.plot(x, y, color="red", label="拟合直线", linewidth=2)
plt.xlabel('1/t(℃)')
plt.ylabel('1/U(mV)')
plt.title('y={}x+{}'.format(k, b))
plt.legend(loc='lower right')
plt.show()