# -*- coding: utf-8 -*-
#為替の予測を最小二乗法で回帰する。

import numpy as np
import scipy as sp
from scipy import optimize as op
import matplotlib.pyplot as plt
import pandas as pd
import math

data = pd.read_csv("2016-03-17_price.csv")

usd = data.USDJPY
usd_x = np.array(range(len(usd)))



def f(x,a,b,c,d=0):
	return a + b*x + c*x*x + d*x**3

parameter_initial = np.array([0.0, 0.0, 0.0,0.0]) #a, b, c
result, covariance = op.curve_fit(f, usd_x, usd, p0=parameter_initial)

print result

y = f(usd_x,result[0],result[1],result[2],result[3])
print y

plt.plot(usd_x, usd, 'o')
plt.plot(usd_x, y, '-')

plt.show()


# print min(usd)
# print max(usd)
# print usd.last
# plt.ylim(round(min(usd),2),round(max(usd),2))
# plt.show()

