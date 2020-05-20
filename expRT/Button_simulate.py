# -*- coding: utf-8 -*-
"""
Created on Wed May 13 2020

Written by EJ_Chang
"""

import os, random
import numpy as np
from datetime import date
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from ResponseTrigger import *
from Solarized import * # Import solarized color palette
from ButtonSim_Material import *


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

# Default value
pre_key = []
iCol = 0
iRow = 0

# random 

for ima in range(10):
    trialStatus = 1
    reqButton = random.randrange(1,3)
    reqCol = random.randrange(1,3)
    reqRow = random.randrange(0,4)

    BUTTON_STATUS = 'off'
    


    while trialStatus == 1:
        # Background (all blank)
        for image in range(5):
            img = visual.ImageStim(my_win,
                image = backgroundLUT[image]['path'],
                pos = backgroundLUT[image]['position'])
            img.draw()

        # String (icon)
        for lay in range(4):
            img = visual.ImageStim(my_win,
                image = strLUT[lay]['path'],
                pos = strLUT[lay]['position'])
            img.draw()

        '''
        Paste buttons here
        '''
        # Random buttons at random positions

        ## Random position --> determined beforehand
        # reqCol = random.randrange(1,3)
        # reqRow = random.randrange(1,4)

        ## Random UI button 
        # reqButton = random.choice(buttonType) 
        # reqButton = random.randrange(0,3)
        # Actually I can just random shuffle number 1~4

        request = visual.ImageStim(my_win,
            image = requestLUT[reqButton][BUTTON_STATUS], # On/Off switch here
            pos = indicatorLUT[reqCol]['position'][reqRow])

        request.draw()


        # Indicator
        indicator = visual.Rect(my_win, 
            width = indicatorLUT[iCol]['width'], 
            height = indicatorLUT[iCol]['height'], 
            fillColor = SOLARIZED['grey01'], fillColorSpace='rgb255', 
            lineColor = SOLARIZED['grey01'], lineColorSpace ='rgb255', 
            pos= indicatorLUT[iCol]['position'][iRow], opacity = 0.5)

        indicator.draw()
        my_win.flip()
        # Get response
        response_hw, response_key, response_status = getAnything(mouse, joy)

        if response_status == 1 and response_key != pre_key:

            key_meaning = interpret_key(response_hw, response_key)
            final_answer, BUTTON_STATUS = reponse_checker_BTS(
                BUTTON_STATUS, key_meaning, iRow, iCol, reqRow, reqCol)
            iRow, iCol, trialStatus = determine_behavior_BTS(key_meaning, iRow, iCol)

        # if response_status == 1:
        #     optLUT[count]['status'][count] = 'on'
        #     count += 1
        #     if OPTION_STATUS == 'off':
        #         OPTION_STATUS = 'on'
        #     elif OPTION_STATUS == 'on':
        #         OPTION_STATUS = 'off'

            # if key_meaning == 'Abort':
            #     trialStatus = 0
            #     # break

        pre_key = response_key


# Close the window
my_win.close()

