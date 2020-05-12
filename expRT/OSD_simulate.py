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

# Subject profile
today = date.today()
print('Today is %s:' % today)
usernum = int(input('Please enter subject number:'))
username = input("Please enter your name:").upper()
print('Hi %s, welcome to our experiment!' % username)

if usernum % 2 == 1:
    hw_required = ['Wheel','dPad']
elif usernum % 2 == 0:
    hw_required = ['dPad', 'Wheel']

print(hw_required) 

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
block_ins = {
    'Wheel': 'OSD_ImgFolder/block_w.png',
    'dPad' : 'OSD_ImgFolder/block_d.png'
    }
    
# Initial values for the whole experiment
pre_key = []
response = []


# Strat the experiment ---- 
for block in range(2):
    # instruction here
    img = visual.ImageStim(my_win, image = block_ins[hw_required[block]], pos = (0,0))
    img.draw()
    my_win.flip()
    core.wait(3)

    print('Block #', block, 'Start!')
    nRow = 4
    nCol = 3
    for trial in range(3):    
        print(block, '/', trial)
        # Initial values for every trial
        trialStatus = 1
        iRow = 0
        iCol = 0
        reqCol = 0
        reqRow = random.randrange(nRow + 1)
        stimuli_time = core.getTime()

        while trialStatus == 1:
            # Background OSD
            for image in range(5):
                img = visual.ImageStim(my_win,
                    image = imageLUT[image]['path'],
                    pos = imageLUT[image]['position'])

                img.draw()

            # Request
            request = visual.Rect(my_win,
                width = requestLUT[reqCol]['width'],
                height = requestLUT[reqCol]['height'],
                fillColor = SOLARIZED['yellow'], fillColorSpace='rgb255', 
                lineColor = SOLARIZED['base01'], lineColorSpace ='rgb255', 
                pos= indicatorLUT[reqCol]['position'][reqRow], opacity = 1)
            request.draw()
            # Indicator
            indicator = visual.Rect(my_win, 
                width = indicatorLUT[iCol]['width'], 
                height = indicatorLUT[iCol]['height'], 
                fillColor = SOLARIZED['base01'], fillColorSpace='rgb255', 
                lineColor = SOLARIZED['base01'], lineColorSpace ='rgb255', 
                pos= indicatorLUT[iCol]['position'][iRow], opacity = 0.5)

            indicator.draw()

            # OSD strings
            for image in range(2):
                img = visual.ImageStim(my_win,
                    image = strLUT[image]['path'],
                    pos = strLUT[image]['position'])

                img.draw()

            # Everything has been drawn. Flip to show.
            my_win.flip()

            # Get response
            response_hw, response_key, response_status = getAnything(mouse, joy)

            if response_status == 1 and response_key != pre_key:
                current_time = core.getTime()

                key_meaning = interpret_key(response_hw, response_key)

                # Reveal next que only when Correct answer was pressed
                key_judgement, final_answer = reponse_checker_OSD(
                                                hw_required[block],
                                                response_hw, 
                                                iRow, iCol, 
                                                reqRow, reqCol
                                                )

                # Save responses 
                response.append([
                                response_hw, key_meaning,
                                iRow, iCol,
                                reqRow, reqCol,
                                final_answer,
                                current_time - stimuli_time,
                                current_time
                                ]) 
                # Next que
                iRow, iCol, trialStatus = determine_behavior_OSD(key_meaning, 
                                                                 iRow, iCol)

                if final_answer == 1 and key_meaning == 'OK':
                    reqCol += 1
                    if reqCol > nCol:
                        trialStatus = 0
                    reqRow = random.randrange(nRow + 1)
                    stimuli_time = core.getTime()

            pre_key = response_key

# Close the window
my_win.close()


# Experiment record file
os.chdir('/Users/YJC/Dropbox/ExpRecord_OSD')
filename = ('%s_%s.txt' % (today, username))
filecount = 0

while os.path.isfile(filename):
    filecount += 1
    filename = ('%s_%s_%d.txt' % (today, username, filecount))

with open(filename, 'w') as filehandle: # File auto closed
    filehandle.writelines("%s\n" % key for key in response)
