# -*- coding: utf-8 -*-

import os, random
import numpy as np
from DirGenerator import *

dir_DictList= []
with open("dir_lim_num.txt") as f:
    for line in f:
        (number, main_dir, ortho_dir_1, ortho_dir_2) = line.split()
        sti_Dict = {
        'number': number,
        'main_dir': main_dir,
        'ortho_dir': [ortho_dir_1,ortho_dir_2]
        }
        dir_DictList.append(sti_Dict)

# print(type(dir_DictList))
theList = dirGenerate(dir_DictList)

print(theList)

line_up = np.array([0,50])
line_down = np.array([0,-50])
line_right = np.array([50,0])
line_left = np.array([-50,0])
four_dir = [line_up, line_down, line_left, line_right]
stimulusList = []

for ques in theList:
    ques = int(ques)
    stimulusList.append(four_dir[ques])
    print(ques, type(ques))

print(stimulusList)


