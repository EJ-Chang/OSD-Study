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


# Preparing Window ----
my_win = visual.Window(size = (800, 600), pos = (880,1040), 
                       color = SOLARIZED['base03'], colorSpace = 'rgb255', 
                       monitor = mon, units = 'pix', screen = 1)


# Import files from sub-folder ---- 
IMG_START = 'OSD_ImgFolder/start.png'
IMG_REST = 'OSD_ImgFolder/rest.png'
IMG_THX = 'OSD_ImgFolder/thanks.png'


for image in range(8):

    img = visual.ImageStim(win = my_win, image = imageLUT[image]['path'],
                           units = 'pix', pos = pos_list[image])

    img.draw()


my_win.flip()
core.wait(2)

img = visual.ImageStim(win = my_win, image = imageLUT[5]['path'],
                           units = 'pix', pos = pos_list[image])

for image in range(8):

    for ruler in range(8):

        rulerimg = visual.ImageStim(win = my_win, image = imageLUT[ruler]['path'],
                               units = 'pix', pos = pos_list_high[ruler])

        rulerimg.draw()

    img.pos = pos_list[image]

    img.draw()
    my_win.flip()
    core.wait(1)


# Close the window
my_win.close()