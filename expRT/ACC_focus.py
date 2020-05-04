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
from StiGenerator import *
from ResponseTrigger import *

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
        (number, main_dir, ortho_dir_1, ortho_dir_2, \
         main_meaning, ortho_meaning_1, ortho_meaning_2) = line.split()

        # Write a dictionary
        sti_Dict = {
        'number': number,
        'main_dir': main_dir,
        'ortho_dir': [ortho_dir_1,ortho_dir_2],
        'main_meaning': main_meaning,
        'ortho_meaning': [ortho_meaning_1, ortho_meaning_2]
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


# Setting Constants ----
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

four_vector = [LINE_UP, LINE_DOWN, LINE_LEFT, LINE_RIGHT]
four_dict = {'Up': LINE_UP, 
             'Down': LINE_DOWN,
             'Left': LINE_LEFT,
             'Right': LINE_RIGHT}

# Timer
MAX_DURATION = 30
experiment_timer = core.Clock()    
experiment_timer.reset()
# Prepare for response
pre_key = []
key_meaning = 'Up'
stimuli_time = core.getTime()

# ===========================
for nTrial in range(10):

    # Get the ques
    thePath = pathGenerate(dir_DictList)
    # print(thePath[-1], 'length = ', len(thePath))

    resp_path = []
    sti_path = [] # Array of ques
    tag_que = [] # Word tag of ques
    line_pos = ORIGIN_POINT
    for ques in thePath:
        ques = int(ques)
        line_pos = line_pos + four_vector[ques]
        sti_path.append(four_vector[ques])
        tag_que.append(dir_DictList[ques]['main_meaning'])

    print(tag_que) # Direction by name(up, down left, right. in string)
    print(line_pos)

    # Rotate along with the last line in this path
    if thePath[-1] == '0': 
        rotate = ROTATE_270
    elif thePath[-1] == '1':
        rotate = ROTATE_90
    elif thePath[-1] == '2':
        rotate = ROTATE_180
    elif thePath[-1] == '3':
        rotate = ROTATE_0 


    # Start drawing ---- 
    current_point = ORIGIN_POINT
    origin = visual.Circle(my_win, units =  'pix',
                           radius = 5, pos = (0,0),
                           fillColor = base0, fillColorSpace = 'rgb255',
                           lineColor = base0, lineColorSpace = 'rgb255', 
                           interpolate = True)



    loop_Status = 1
    # While loop here ---------------
    # while experiment_timer.getTime() < MAX_DURATION:
    while loop_Status == 1:

        # Get back to origin point
        current_point = ORIGIN_POINT
        response_point= ORIGIN_POINT

        # Draw origin point
        origin.draw()

        # Define path length
        nLine = len(thePath)

        # Draw lines
        for iLine in range(nLine):

            # Que path (stimuli) ----
            pre_point = current_point
            current_point = current_point + sti_path[iLine]

            path_sti = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                                        lineColor = green, lineColorSpace = 'rgb255', 
                                        vertices = (pre_point, current_point),
                                        closeShape = False, pos = (0, 0)
                                        )
            path_sti.draw()

            # Response path (reponse) ----
            pre_resp_point = response_point
            response_point = response_point + sti_path[iLine]

            path_resp = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                                         lineColor = magenta, lineColorSpace = 'rgb255', 
                                         vertices = (pre_point, response_point), # Change needed
                                         closeShape = False, pos = (0,0)
                                         )

            path_resp.draw()

        # Draw indicator
        indicator = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2,
                                     lineColor = yellow, lineColorSpace = 'rgb255',
                                     vertices = (pre_point, pre_point + four_dict[key_meaning]),
                                     closeShape = False, pos = (0,0)
                                     )
        indicator.draw()
        # Draw ending point (with an arrow)

        end = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                               lineColor = green, lineColorSpace = 'rgb255', 
                               vertices = (current_point + np.dot(ARROW_WING1, 
                                                                  rotate), 
                                           current_point, 
                                           current_point + np.dot(ARROW_WING2, 
                                                                  rotate)),
                               closeShape = False, pos = (0, 0))
        end.draw()


        my_win.flip()
        # core.wait(2)

        '''
        Response Block
        '''
        # Get response 
        response_hw, response_key, response_status = getAnything(mouse, joy)

        
        # if response_status == 1 and response_key != pre_key:
        if response_status == 1 and pre_status == 0:
            # Get current time
            current_time = core.getTime()
            key_meaning = interpret_key(response_hw, response_key) 
            # response determine the magenta line
            
            # resp_direction, loop_Status = determine_nextline(key_meaning, iLine, 
                                                           # nLine, loop_Status)

            # resp_path.append(four_vector[resp_direction])


            print(key_meaning)




            pre_key = response_key # Button status update
            loop_Status = 0



        pre_status = response_status    



# Close the window
my_win.close()