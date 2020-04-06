# -*- coding: utf-8 -*-

import os, random


imageList = []
path = "/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/StimulusPNG"
for file in os.listdir(path):
    if file.endswith(".png"):
        imageList.append(os.path.join(path, file))

imageList = sorted(imageList)
presentList = []
# print(imageList[2])
seq = [1,2,3,4,5,6,7,8,9,10,11,12]
for seq in range(3):
    random.shuffle(seq)
    print(seq)
    presentList.append(seq)
    print(presentList)  # Q: how to save current sequnce?

# for n in range(3):
    # print(imageList[seq[n]])

# print(random.randrange(4))