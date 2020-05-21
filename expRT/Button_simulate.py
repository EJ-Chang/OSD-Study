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

# Default value
pre_key = []
response = []
x = np.array([0, 1, 2])
requestList = np.repeat(x, [1, 1, 1], axis = 0)
random.shuffle(requestList)


# Import files from sub-folder ---- 
IMG_START = 'OSD_ImgFolder/start.png'
IMG_REST = 'OSD_ImgFolder/rest.png'
IMG_THX = 'OSD_ImgFolder/thanks.png'
block_ins = {
    'Wheel': 'OSD_ImgFolder/block_w.png',
    'dPad' : 'OSD_ImgFolder/block_d.png'
    }
    


# Strat the experiment ---- 
for block in range(2):

    # instruction here
    req_hw = hw_required[block]
    img = visual.ImageStim(my_win, image = block_ins[req_hw], pos = (0,0))
    img.draw()
    my_win.flip()
    core.wait(1)

    for iTrial in range(len(requestList)):
        trialStatus = 1
        iCol = 1
        iRow = 0
        reqButton = requestList[iTrial]
        reqCol = random.randrange(1,3)
        reqRow = random.randrange(0,4)

        BUTTON_STATUS = 'off'
        final_answer = 0

        stimuli_time = core.getTime()


        while trialStatus == 1:

            # Background (all blank)
            for image in range(5):
                img = visual.ImageStim(my_win,
                    image = backgroundLUT[image]['path'],
                    pos = backgroundLUT[image]['position'])
                img.draw()

            # String (icon)
            for lay in range(reqCol+1):
                img = visual.ImageStim(my_win,
                    image = strLUT[lay]['path'],
                    pos = strLUT[lay]['position'])
                img.draw()

            # UI buttons
            for req in range(2):
                request = visual.ImageStim(my_win,
                    image = requestLUT[reqButton][BUTTON_STATUS], # On/Off switch here
                    pos = indicatorLUT[reqCol]['position'][reqRow])

                request.draw()

            if requestLUT[reqButton]['hint'] == 1:
                if (iRow == reqRow and iCol == reqCol):
                    hint = visual.ImageStim(my_win,
                        image = strLUT[reqCol+1]['hint'],
                        pos = strLUT[reqCol+1]['position'])
                    hint.draw()


            # Indicator
            indicator = visual.Rect(my_win, 
                width = indicatorLUT[iCol]['width'], 
                height = indicatorLUT[iCol]['height'], 
                fillColor = SOLARIZED['grey01'], fillColorSpace='rgb255', 
                lineColor = SOLARIZED['grey01'], lineColorSpace ='rgb255', 
                pos= indicatorLUT[iCol]['position'][iRow], opacity = 0.5)


            if BUTTON_STATUS == 'on':
                hint = visual.ImageStim(my_win,
                        image = strLUT[reqCol+1]['path'],
                        pos = strLUT[reqCol+1]['position'])
                hint.draw()
                my_win.flip()
                core.wait(1)
                interval = visual.ImageStim(my_win,
                    image = 'OSD_ImgFolder/BetweenTrial.png',
                    pos = (0,0), opacity = 0.9)
                    # pos = indicatorLUT[iCol]['position'][iRow], opacity = 0.8)

                for image in range(5):
                    img = visual.ImageStim(my_win,
                        image = backgroundLUT[image]['path'],
                        pos = backgroundLUT[image]['position'])
                    img.draw()

                interval.draw()
                my_win.flip()
                core.wait(1)
                trialStatus = 0

            elif BUTTON_STATUS == 'off':
                indicator.draw()
                my_win.flip()
                # Get response
                response_hw, response_key, response_status = getAnything(mouse, joy)

                if response_status == 1 and response_key != pre_key:

                    key_meaning = interpret_key(response_hw, response_key)
                    final_answer, BUTTON_STATUS = reponse_checker_BTS(
                        BUTTON_STATUS, req_hw, response_hw,
                        key_meaning, iRow, iCol, reqRow, reqCol)

                    # Save responses 
                    if BUTTON_STATUS == 'on':
                        current_time = core.getTime()
                        response.append([
                                        req_hw, response_hw, 
                                        requestLUT[reqButton]['name'],
                                        reqRow, reqCol,
                                        key_meaning,
                                        final_answer,
                                        current_time - stimuli_time,
                                        current_time
                                        ]) 

                    iRow, iCol, trialStatus = determine_behavior_BTS(key_meaning, iRow, iCol)

            pre_key = response_key


# Close the window
my_win.close()


# Experiment record file
os.chdir('/Users/YJC/Dropbox/ExpRecord_BTS')
filename = ('%s_%s.txt' % (today, username))
filecount = 0

while os.path.isfile(filename):
    filecount += 1
    filename = ('%s_%s_%d.txt' % (today, username, filecount))

with open(filename, 'w') as filehandle: # File auto closed
    filehandle.writelines("%s\n" % key for key in response)

