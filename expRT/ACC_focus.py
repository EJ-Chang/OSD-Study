# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 2020

Written by EJ_Chang
"""

import os, random
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from datetime import date

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

# Draw random lines

line_up = visual.ShapeStim(my_win, units = 'pix', lineWidth = 1.5, 
                          lineColor = (88,110,117), lineColorSpace = 'rgb255', 
                          vertices = ((-50, 0), (-50, 50)),
                          closeShape = False, pos = (0, 0))


# core.wait(2)
line_up.draw()
my_win.flip()
core.wait(2)


line_left = visual.ShapeStim(my_win, units = 'pix', lineWidth = 1.5, 
                          lineColor = (88,110,117), lineColorSpace = 'rgb255', 
                          vertices = ((-50, 0), (0, 0)),
                          closeShape = False, pos = (0, 0))

line_left.draw()
my_win.flip()
core.wait(2)

# Close window
my_win.close()

