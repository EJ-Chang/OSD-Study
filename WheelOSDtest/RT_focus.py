# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 2020

Written by EJ_Chang on Jan 6 2020
"""

from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
import os, random


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
# nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
# id = 0 # I'll use the first one as input
# joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)
mouse.clickReset() # Reset to its initials

# Preparing experiment stimulus
imageList = []
path = "/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/StimulusPNG"
for file in os.listdir(path):
    if file.endswith(".png"):
        imageList.append(os.path.join(path, file))
imageList = sorted(imageList) # Make a list of stimulus pics


# Preparing experiment timer
experiment_timer = core.Clock()
experiment_timer.reset()
MAX_DURATION = 5 # Unit: second
expStatus = 1
# nTrial = 1

# Preparing experiment trials
for nTrial in range(12):
# while expStatus == 1:
    img = visual.ImageStim(win = my_win, image = imageList[random.randrange(12)], 
                           units = 'pix')
    img.draw()
    my_win.flip()
    core.wait(1) # TODO: turn into waiting for mouse click
    buttons, times = mouse.getPressed(getTime = True) # Needs a while loop
    if buttons[0] == 1:
        print(times)
    elif buttons[2] == 1:
        break
    #     nTrial = nTrial + 1
    # if nTrial >= 4:
    #     break        

"""
TODO:
# Practice Trials ----
# Experiment Trials ----
# Save files & Thanks ----
"""