# -*- coding: utf-8 -*-

import os 


imageList = []
path = "/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/Stimulus"
for file in os.listdir(path):
    if file.endswith(".png"):
        imageList.append(os.path.join(path, file))

imageList = sorted(imageList)
print(imageList[2])
