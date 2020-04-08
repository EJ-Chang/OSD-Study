# -*- coding: utf-8 -*-

import os, random
from testFunc import sum_UP

# imageList = []
# path = "/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/StimulusPNG"
# for file in os.listdir(path):
#     if file.endswith(".png"):
#         imageList.append(os.path.join(path, file))

# imageList = sorted(imageList)

# # print(imageList[2])
# seq = [1,2,3,4,5,6,7,8,9,10,11,12]
# presentList = []
# for n in range(3):
#     random.shuffle(seq)
#     n_seq = tuple(seq)
#     presentList.append(n_seq)
#     print(n_seq)
#     # presentList = [presentList[index] for index in seq]
#     print(presentList[n])  

# sum_UP(1,2)

# aa, bb = sum_UP(2,4)
# cc = sum_UP(2,4)

# print(aa)
# print(bb)
# print(cc)

testVar = range(3)
testList = list(testVar)
random.shuffle(testList)
print(testVar)
print(testList)