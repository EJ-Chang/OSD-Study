# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 2020

Written by EJ_Chang on Jan 6 2020
"""

import os, random
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from ResponseTrigger import *


# Make screen profile ----
widthPix = 2560 # screen width in px
heightPix = 2440 # screen height in px
monitorwidth = 60 # monitor width in cm
viewdist = 60 # viewing distance in cm
monitorname = 'ProArt27'
scrn = 0 # 0 to use main screen, 1 to use external screen
mon = monitors.Monitor(monitorname, width=monitorwidth, distance=viewdist)
mon.setSizePix((widthPix, heightPix))
mon.save()


# Load initial setting ----
# Preparing Window
my_win = visual.Window(size=(800, 600), pos=(0,0), monitor = mon, units = 'pix', 
                       screen = 1)

# Preparing Joystick & Mouse
# - Joysticks setting
joystick.backend = 'pyglet'
nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
id = 0 # I'll use the first one as input
joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)
mouse.clickReset() # Reset to its initials


# Preparing experiment stimulus
img_start = '/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/StimulusPNG/start.png'
img_rest = '/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/StimulusPNG/rest.png'

lineNumber = 1
imageLUT = [] # list of image dictionary
with open("sti_files.txt") as f:
    for line in f:
        (number, hw, mean, filepath) = line.split()
        sti_Dict = {
        'number': lineNumber,
        'hardware': hw,
        'meaning': mean,
        'path': filepath
        }
        lineNumber += 1
        imageLUT.append(sti_Dict)


# Randomizing the list
nStimulus = len(imageLUT)  # nStimulus = 10
playList = list(range(nStimulus)) # playList = [0,1,2,...11]
random.shuffle(playList) # Shuffle the playList
stimulus_seq = tuple(playList) # Make it unchangable
print(stimulus_seq)

# Preparing experiment timer
experiment_timer = core.Clock()
experiment_timer.reset()

# Setting initial numbers
item = 0
pre_key = []
expStatus = 1
response = []


# Start experiment 
# Greeting page

img = visual.ImageStim(win = my_win, image = img_start, 
                       units = 'pix')
img.draw()
my_win.flip()
core.wait(2)

# Trials
while expStatus == 1:
    # img = visual.ImageStim(win = my_win, image = imageList[stimulus_seq[item]], 
    #                        units = 'pix')
    img = visual.ImageStim(win = my_win, 
                           image = imageLUT[stimulus_seq[item]]['path'],
                           units = 'pix')
    img.draw()
    my_win.flip()

    # Get response
    response_hw, response_key, response_status = getAnything(mouse, joy)
    
    # if clicks != pre_mouse and response_status == 1:
    if response_status == 1 and response_key != pre_key:
        # Add interval picture here --------
        current_time = core.getTime()
        # item, expStatus = response_key(clicks, item, nStimulus, expStatus) 
        key_meaning = interpret_key(response_hw, response_key) 

        key_judgement, final_answer = reponse_checker(response_hw, 
                                                      key_meaning, 
                                                      imageLUT[stimulus_seq[item]])
        
        item, expStatus = determine_behavior(key_meaning, item,
         nStimulus, expStatus)

        print(key_judgement, final_answer)

        # Determine response key & time
        response.append([stimulus_seq[item-1], 
                        response_hw, 
                        key_meaning,
                        imageLUT[stimulus_seq[item]]['hardware'],
                        imageLUT[stimulus_seq[item]]['meaning'],
                        final_answer
                        ]) # correct/not, RT, real time

        # Instruction between stimulus
        img = visual.ImageStim(win = my_win, image = img_rest, 
                           units = 'pix')
        img.draw()
        my_win.flip()

        # Stimulus interval
        t = 1 + random.randrange(1)
        core.wait(t)
        print(t)

    pre_key = response_key # Button status update


# Exp END ========
print('Get your responses:', response)
# Save & close
my_win.close()
