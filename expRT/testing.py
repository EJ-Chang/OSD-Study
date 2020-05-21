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


x = np.array([0,1,2])
a = np.repeat(x, [2,2,2], axis = 0)
random.shuffle(a)
print (a)
