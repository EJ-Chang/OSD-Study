# -*- coding: utf-8 -*-

import os, random


imageList = []
path = "/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/StimulusPNG"
for file in os.listdir(path):
    if file.endswith(".png"):
        imageList.append(os.path.join(path, file))

imageList = sorted(imageList)
# print(imageList[2])

for n in range(3):
    print(imageList[n])

# print(random.randrange(4))