# -*- coding: utf-8 -*-

import os, random
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from datetime import date
import numpy as np
from DirGenerator import *
from ResponseTrigger import *

# Make screen profile ----
widthPix = 2560 # screen width in px
heightPix = 1440 # screen height in px
monitorwidth = 60 # monitor width in cm
viewdist = 60 # viewing distance in cm
monitorname = 'ProArt27'
scrn = 0 # 0 to use main screen, 1 to use external screen
mon = monitors.Monitor(monitorname, width=monitorwidth, distance=viewdist)
mon.setSizePix((widthPix, heightPix))
mon.save()

# Preparing Window ----
my_win = visual.Window(size=(400, 400), pos=(880,1040), 
                       color=(0,43,54), colorSpace='rgb255', 
                       monitor = mon, units = 'pix', 
                       screen = 1)


# Preparing Joystick & Mouse ----
# - Joysticks setting
joystick.backend = 'pyglet'
nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
id = 0 # I'll use the first one as input
joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)
mouse.clickReset() # Reset to its initials

# Visual sti
ORIGIN_POINT = (0,0)

current_point = ORIGIN_POINT


# Timer
MAX_DURATION = 5
experiment_timer = core.Clock()    
experiment_timer.reset()

# Draw origin point (larger dot)
# origin = visual.DotStim(my_win, units = 'pix',
#                       fieldPos = ORIGIN_POINT, fieldSize = (5,5),
#                       dotSize=8,
#                       color = (128,128,128), colorSpace = 'rgb255'
#                       )
# origin.draw()
# my_win.flip()

# While loop here
while experiment_timer.getTime() < MAX_DURATION:
    # Draw origin point (larger dot)
    # origin = visual.DotStim(my_win, units = 'pix',
    #                       fieldPos = ORIGIN_POINT, 
    #                       dotSize=10,
    #                       color = (128,128,128), colorSpace = 'rgb255'
    #                       )
    origin = visual.Circle(my_win, units =  'pix',
                           radius = 5, pos = (50,40),
                           fillColor = (128, 128,128), fillColorSpace = 'rgb255',
                           lineColor = (128,128,128), lineColorSpace = 'rgb255', 
                           interpolate = True)

    origin.draw()
    my_win.flip()
    a, b, c = getAnything(mouse, joy)
    if c == 1:
        print(a, b, c)

my_win.close()
