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

# demoList = [
#     ['dPad', 0, 0, 'dPad', [0, -1], 'Down', 'Down', 1, 0.6018327439996938, 9.388065637998807],
#     ['dPad', 0, 1, 'dPad', [0, -1], 'Down', 'Down', 1, 0.15018101300302078, 9.538246651001828]
#     ]

# with open('test.txt', 'w') as filehandle: # File auto closed
#     for key in demoList:
#         for item in key:
#             filehandle.writelines("%s " % item)
#         filehandle.writelines("\n")

astring = 'ABCDE\n'
print(astring)

astring.split('\n')
print(astring[0])