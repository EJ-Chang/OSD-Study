# -*- coding: utf-8 -*-
"""
Created on Wed May 6 2020

Written by EJ_Chang
"""

import os, random
import numpy as np
from datetime import date
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from ResponseTrigger import *
from Solarized import * # Import solarized color palette
from ExpMaterial import *

nRow = 5
nCol = 4
pseudo_randomList = []
queNum = 0
for i in range(1000):
  reqRow = random.randrange(1, nRow)
  pseudo_randomList.append(reqRow)

# # Experiment record file
# # os.chdir('/Users/YJC/Dropbox/ExpRecord_OSD')
# filename = ('PseudoQue.txt')


# with open(filename, 'w') as filehandle: # File auto closed
#     filehandle.writelines("%s\n" % key for key in pseudo_randomList)
for un in range(1,20):
    reqRow = PseudoRandomRow[queNum]
    print(reqRow, queNum)
    queNum += 1
    
