# -*- coding: utf-8 -*-

from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
import os, random
from testFunc import getAnything

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

# Make initials
experiment_timer = core.Clock()
experiment_timer.reset()
MAX_DURATION = 7
previous_resp = []
# Open window (for joystick)
my_win = visual.Window(size=(400, 400), pos=(0,0), monitor = mon, units = 'pix', 
                       screen = 1)

# Get mouse and joystick
joystick.backend = 'pyglet'
nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
id = 0 # Use the first one as input
joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)
mouse.clickReset() # Reset to its initials

# start
while experiment_timer.getTime() < MAX_DURATION:
    my_win.flip()
    a,b,c,d = getAnything(mouse, joy)
    if previous_resp != [a,b,c,d]:
        print(a,b,c,d)
    previous_resp = [a,b,c,d]

my_win.close()
