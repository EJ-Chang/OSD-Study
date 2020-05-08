# -*- coding: utf-8 -*-
"""
Created on Wed May 6 2020

Written by EJ_Chang
"""

import os, random
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from datetime import date
import numpy as np
from ResponseTrigger import *


# Make screen profile ----
widthPix = 2560 # screen width in px
heightPix = 1440 # screen height in px
monitorwidth = 60 # monitor width in cm
viewdist = 60 # viewing distance in cm
monitorname = 'ProArt27'
scrn = 0 # 0 to use main screen, 1 to use external screen
mon = monitors.Monitor(monitorname, width = monitorwidth, distance = viewdist)
mon.setSizePix((widthPix, heightPix))
mon.save()


# Color Palette ----
base03 = (0,43,54)
base01 = (88,110,117)
base0 = (131,148,150)
yellow = (181,137,0)
magenta = (211,54,130)
cyan = (42,161,152)
green = (133,153,0)

# Preparing Window ----
my_win = visual.Window(size = (800, 600), pos = (880,1040), 
                       color = base03, colorSpace = 'rgb255', 
                       monitor = mon, units = 'pix', screen = 1)



# Import files from sub-folder
Welcome = 'OSD_ImgFolder/start.png'

img = visual.ImageStim(win = my_win, image = Welcome, 
                       units = 'pix')
img.draw()
my_win.flip()
core.wait(2)



# Close the window
my_win.close()