# -*- coding: utf-8 -*-

import os, random
import numpy as np

x = (1,2)
y = (3,3)
a = [1,2]
b = [3,3]

print(x+y)
print(a+b)

a = np.array([1,2])
b = np.array([3,3])
print(a+b)

posList = np.array([(-350,0), (-300,0), (-300,50)])
pos2List = np.array([(-300,0), (-300,50), (-250, 50)])
c = posList + pos2List
print(c)
print(type(c[0]))