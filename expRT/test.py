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

a = np.array([-10,-10])
 
rotate_270 = np.array([
                      [0,1], 
                      [-1,0]
                      ])

print('Rotate 270 degree:', np.dot(rotate_270, a))
 # Rotate 270 degree anti clockwise
rotate_90 = np.array([
                     [0,-1],
                     [1,0]
                     ])

print('Rotate 90 degree:', np.dot(rotate_90, a))