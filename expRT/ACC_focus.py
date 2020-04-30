# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 2020

Written by EJ_Chang
"""

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

# Color Palette ----
base03 = (0,43,54)
base0 = (131,148,150)
yellow = (181,137,0)
magenta = (211,54,130)
cyan = (42,161,152)
green = (133,153,0)

# Directions ----
dir_DictList= []
with open("dir_lim_num.txt") as f:
    for line in f:
        (number, main_dir, ortho_dir_1, ortho_dir_2) = line.split()
        sti_Dict = {
        'number': number,
        'main_dir': main_dir,
        'ortho_dir': [ortho_dir_1,ortho_dir_2]
        }
        dir_DictList.append(sti_Dict)

# Preparing Window ----
my_win = visual.Window(size=(800, 800), pos=(880,1040), 
                       color=base03, colorSpace='rgb255', 
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


# Setting Constants
ORIGIN_POINT = (0,0)

ARROW_WING1 = np.array([-10,10])
ARROW_WING2 = np.array([-10,-10])

ROTATE_0 = np.array([[1,0], [0,1]])
ROTATE_90 = np.array([[0,-1], [1,0]])
ROTATE_180 = np.array([[-1,0], [0,-1]])
ROTATE_270 = np.array([[0,1], [-1,0]])

LINE_UP = np.array([0,40])
LINE_DOWN = np.array([0,-40])
LINE_LEFT = np.array([-40,0])
LINE_RIGHT = np.array([40,0])

four_dir = [LINE_UP, LINE_DOWN, LINE_LEFT, LINE_RIGHT]
# Timer
MAX_DURATION = 3
experiment_timer = core.Clock()    
experiment_timer.reset()

core.wait(1)
current_point = ORIGIN_POINT
origin = visual.Circle(my_win, units =  'pix',
                           radius = 5, pos = (0,0),
                           fillColor = base0, fillColorSpace = 'rgb255',
                           lineColor = base0, lineColorSpace = 'rgb255', 
                           interpolate = True)




# ===========================
for nTrial in range(10):
    # Timer
    MAX_DURATION = 3
    experiment_timer = core.Clock()    
    experiment_timer.reset()


    # Get the ques
    theList = dirGenerate(dir_DictList)
    print(theList[-1], 'length = ', len(theList))

    sti_path = []
    for ques in theList:
        ques = int(ques)
        sti_path.append(four_dir[ques])

    if theList[-1] == '0': 
        rotate = ROTATE_270
    elif theList[-1] == '1':
        rotate = ROTATE_90
    elif theList[-1] == '2':
        rotate = ROTATE_180
    elif theList[-1] == '3':
        rotate = ROTATE_0 


    # Start drawing ---- 
    # current_point = ORIGIN_POINT


    # While loop here ---------------
    while experiment_timer.getTime() < MAX_DURATION:
        current_point = ORIGIN_POINT


        # # Draw origin point (larger dot)
        # origin = visual.DotStim(my_win, units = 'pix',
        #                         fieldPos = current_point, 
        #                         fieldShape = 'circle',
        #                         # fieldSize = (5,5),
        #                         dotSize=8,
        #                         color = base0, colorSpace = 'rgb255'
        #                         )
        origin.draw()


        # Draw continuous lines

        for direction in range(len(theList)):
            pre_point = current_point
            current_point = current_point + sti_path[direction]

            line_next = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                                         lineColor = green, lineColorSpace = 'rgb255', 
                                         vertices = (pre_point, current_point),
                                         closeShape = False, pos = (0, 0)
                                         )
            line_next.draw()
            # print(direction)



        # Draw ending point(with an arrow)

        


        end = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                               lineColor = green, lineColorSpace = 'rgb255', 
                               vertices = (
                                           current_point + np.dot(ARROW_WING1, 
                                                                  rotate), 
                                           current_point, 
                                           current_point + np.dot(ARROW_WING2, 
                                                                  rotate)),
                               closeShape = False, pos = (0, 0)
                               )
        end.draw()


        my_win.flip()
        # core.wait(2)

        # Get response
        response_hw, response_key, response_status = getAnything(mouse, joy)
        if response_status == 1:
            print(response_hw)




      # Get response
      # while experiment_timer.getTime() < MAX_DURATION:
      #   response_hw, response_key, response_status = getAnything(mouse, joy)
      #   if response_status == 1:
      #     print(response_hw)



# Close the window
my_win.close()