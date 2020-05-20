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


optionLUT = {
    'name' : 'test',
    'status' : ['on', 'on'],
    'default' : ['def', 'def']
}


for i in range(2):
    print(optionLUT['name'])
    print(optionLUT['status'][i])
    stat = input("Please enter status:")
    optionLUT['status'][i] = stat
    print(optionLUT['status'])

print('set to default=======')
optionLUT['status'] = optionLUT['default']

print(optionLUT['status'])