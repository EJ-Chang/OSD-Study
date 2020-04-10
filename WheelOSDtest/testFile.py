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


testVar = [(1,2,3)]
testList = ([1,2,3])
testd = (1,2,3)
# random.shuffle(testList)
print(testVar)
print(type(testVar), len(testVar))
print(type(testList), len(testList))
print(type(testd), len(testd))