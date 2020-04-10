# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 2020

Written by EJ_Chang on Jan 6 2020
"""

from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
import os, random
from ResponseTrigger import response_key

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
imageList = []
path = "/Users/YJC/Dropbox/UsabilityTesting/WheelOSDtest/StimulusPNG"
for file in os.listdir(path):
    if file.endswith(".png"):
        imageList.append(os.path.join(path, file))
imageList = sorted(imageList) # Make a list of stimulus pics

# Randomizing the list
nStimulus = len(imageList)  # nStimulus = 12
playList = list(range(nStimulus)) # playList = [0,1,2,...11]
random.shuffle(playList) # Shuffle the playList
stimulus_seq = tuple(playList) # Make it unchangable
print(stimulus_seq)


# Preparing experiment timer
experiment_timer = core.Clock()
experiment_timer.reset()

# Setting initial numbers
item = 0
pre_Mouse = []
expStatus = 1
response = []

# Start experiment 
while expStatus == 1:
    img = visual.ImageStim(win = my_win, image = imageList[stimulus_seq[item]], 
                           units = 'pix')
    img.draw()
    my_win.flip()

    # Get response
    buttons, times = mouse.getPressed(getTime = True)
    (wheel_x, wheel_y) = mouse.getWheelRel()
    dPad = joy.getAllHats()
    botton_x = joy.getButton(0)
    # I should put all triggers in one buket

    if buttons != pre_Mouse and buttons != [0,0,0]:
        print(core.getTime())
        print(times)
        item, expStatus = response_key(buttons, times, item, nStimulus, expStatus) 
        # response.append([stimulus_seq[item], buttons])
        # Determine response key & time
        response.append([buttons, stimulus_seq[item]])

    pre_Mouse = buttons # Button status update


# Exp END ========
print(response)
# Save & close
my_win.close()
