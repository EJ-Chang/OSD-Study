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
my_win = visual.Window(size = (880, 440), pos = (880,1040), 
                       color = SOLARIZED['base03'], colorSpace = 'rgb255', 
                       monitor = mon, units = 'pix', screen = 1)


# Preparing Joystick & Mouse
# - Joysticks setting
joystick.backend = 'pyglet'
nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
id = 0 # I'll use the first one as input
joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)
mouse.clickReset() # Reset to its initials


# Import files from sub-folder ---- 
IMG_START = 'OSD_ImgFolder/start.png'
IMG_REST = 'OSD_ImgFolder/rest.png'
IMG_THX = 'OSD_ImgFolder/thanks.png'

# Initial values
pre_key = []
expStatus = 1
nTrials = 4
item = 0

# Strat the experiment ---- 
while expStatus == 1:
    # Background OSD
    for image in range(5):
        img = visual.ImageStim(win = my_win, image = imageLUT[image]['path'],
                               units = 'pix', pos = imageLUT[image]['position'])

        img.draw()

    # Selection / indicator
    selection = visual.Rect(my_win, 
                            width = indicatorLUT[item]['width'], 
                            height = indicatorLUT[item]['height'], 
                            fillColor = SOLARIZED['yellow'], fillColorSpace='rgb255', 
                            lineColor = SOLARIZED['base01'], lineColorSpace ='rgb255', 
                            pos= indicatorLUT[item]['position'][item], opacity = 50)

    selection.draw()

    # OSD strings
    for image in range(2):
        img = visual.ImageStim(win = my_win, image = strLUT[image]['path'],
                               units = 'pix', pos = strLUT[image]['position'])

        img.draw()

    # Everything has been drawn. Flip to show.
    my_win.flip()
    # core.wait(2)

    # Get response
    response_hw, response_key, response_status = getAnything(mouse, joy)

    if response_status == 1 and response_key != pre_key:
        # core.quit()
        key_meaning = interpret_key(response_hw, response_key)
        print(key_meaning)
        item, expStatus = determine_behavior(key_meaning, item, nTrials, expStatus)
        # break


# Close the window
my_win.close()