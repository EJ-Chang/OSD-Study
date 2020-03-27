# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 2020

Written by EJ_Chang on Jan 6 2020
"""

from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
import os # Make reading files from directory available


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

path = "/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/Stimulus"
for file in os.listdir(path):
    if file.endswith(".png"):
        imageList.append(os.path.join(path, file))
imageList = sorted(imageList)

img = visual.ImageStim(win = my_win, image = imageList[0], units = 'pix')
img.autoDraw = True
message = visual.TextStim(my_win, units ='norm', pos=[0.7, 0.1], 
 text='Wheel', height = 0.2)
message.autoDraw = True  # Automatically draw every frame



# Preparing experiment timer
experiment_timer = core.Clock()
experiment_timer.reset()
MAX_DURATION = 5 # Unit: second

# Preparing experiment trials

my_win.flip()
core.wait(2.0)
# message.text = 'D Pad'  # Change properties of existing stim
img = visual.ImageStim(win = my_win, image = imageList[2], units = 'pix')
img.autoDraw = True


my_win.flip()
core.wait(2.0)

"""
TODO:
# Practice Trials ----
# Experiment Trials ----
# Save files & Thanks ----
"""