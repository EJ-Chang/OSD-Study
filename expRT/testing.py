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
from StiGenerator import *

# Directions ----
dir_DictList= []
with open("dir_limit.txt") as f:
    for line in f:
        (number, main_dir, ortho_dir_1, ortho_dir_2, \
         main_meaning, ortho_meaning_1, ortho_meaning_2) = line.split()

        # Write a dictionary
        sti_Dict = {
        'number': number,
        'main_dir': main_dir,
        'ortho_dir': [ortho_dir_1,ortho_dir_2],
        'main_meaning': main_meaning,
        'ortho_meaning': [ortho_meaning_1, ortho_meaning_2]
        }

        dir_DictList.append(sti_Dict)

PseudoRandomPath = []
for path in range(30):
    thePath = pathGenerate(dir_DictList)
    PseudoRandomPath.append(thePath)



# Experiment record file
filename = ('PseudoPath.txt')

with open(filename, 'w') as filehandle: # File auto closed
    filehandle.writelines("%s\n" % key for key in PseudoRandomPath)