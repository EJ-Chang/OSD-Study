# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 2020

Written by EJ_Chang
"""

import os, random
from psychopy import visual, event, core, monitors
from psychopy.hardware import joystick
from datetime import date
import numpy as np

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

# Color Palette ----
base03 = (0,43,54)
base0 = (131,148,150)
yellow = (181,137,0)
magenta = (211,54,130)
cyan = (42,161,152)
green = (133,153,0)


# Directions ----
dir_DictList= []
with open("dir_limit.txt") as f:
    for line in f:
        (number, main_dir, ortho_dir_1, ortho_dir_2) = line.split()
        sti_Dict = {
        'number': number,
        'main_dir': main_dir,
        'ortho_dir': [ortho_dir_1,ortho_dir_2]
        }
        dir_DictList.append(sti_Dict)


# Load initial setting ----
# Preparing Window
my_win = visual.Window(size=(800, 600), pos=(880,1040), 
                       color=base03, colorSpace='rgb255', 
                       monitor = mon, units = 'pix', 
                       screen = 1)

# Preparing Joystick & Mouse
# - Joysticks setting
joystick.backend = 'pyglet'
nJoys = joystick.getNumJoysticks() # Check if I have any joysticks
id = 0 # I'll use the first one as input
joy = joystick.Joystick(id) # ID has to be nJoys - 1
# - Mouse setting
mouse = event.Mouse(visible = True, win = my_win)

# Setting initials
ORIGIN_POINT = (-350, 0) # Y axis = 0


arrow_up = np.array([-10,10])
arrow_down = np.array([-10,-10])

rotate_270 = np.array([[0,1], [-1,0]])
rotate_90 = np.array([[0,-1], [1,0]])

line_up = np.array([0,50])
line_down = np.array([0,-50])
line_right = np.array([50,0])
line_left = np.array([-50,0])

# =====

# ------ Stimulus list
random.range(4)


sti_path = [line_right, line_up, line_right, line_down]

# ======

current_point = ORIGIN_POINT

print(current_point)

# Draw continuous lines
origin = visual.DotStim(my_win, units = 'pix',
                        fieldPos = ORIGIN_POINT, fieldSize = (3,3),
                        dotSize=10,
                        color = base0, colorSpace = 'rgb255'
                        )
origin.draw()


for item in range(4):
    pre_point = current_point
    current_point = current_point + sti_path[item]

    line_next = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = green, lineColorSpace = 'rgb255', 
                          vertices = (pre_point, current_point),
                          closeShape = False, pos = (0, 0)
                          )
    line_next.draw()
    print(item)



end = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                          lineColor = green, lineColorSpace = 'rgb255', 
                          vertices = (current_point + np.dot(arrow_down, rotate_90), 
                                      current_point, 
                                      current_point + np.dot(arrow_up, rotate_90)),
                          closeShape = False, pos = (0, 0)
                          )
end.draw()


my_win.flip()
core.wait(2)

# Close window
my_win.close()

