# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 2020
Main update on Mon May 4 2020

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
ORIGIN = visual.Circle(my_win, units =  'pix',
                       radius = 5, pos = ORIGIN_POINT,
                       fillColor = base0, fillColorSpace = 'rgb255',
                       lineColor = base0, lineColorSpace = 'rgb255', 
                       interpolate = True)

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
four_dict = {'Up': LINE_UP,  'Down': LINE_DOWN,
             'Left': LINE_LEFT, 'Right': LINE_RIGHT}

# ===========================


for nTrial in range(10):
    # Get the ques

    tag_que = [] 
    line_pos = ORIGIN_POINT
    sti_path = [line_pos, line_pos] 

    thePath = pathGenerate(dir_DictList)

    for ques in thePath:
        ques = int(ques)
        line_pos = line_pos + four_vector[ques]
        sti_path.append(line_pos) # Coordinates
        tag_que.append(dir_DictList[ques]['main_meaning'])

    N_LINE = len(tag_que)

    # Rotate along with the last line in this path
    if thePath[-1] == '0': 
        rotate = ROTATE_270
    elif thePath[-1] == '1':
        rotate = ROTATE_90
    elif thePath[-1] == '2':
        rotate = ROTATE_180
    elif thePath[-1] == '3':
        rotate = ROTATE_0 


    # =========================
    loopStatus = 1
    iResp = 0
    resp_path = [ORIGIN_POINT, ORIGIN_POINT]
    key_meaning = 'Up'
    while loopStatus == 1 :
        '''
        Stimuli routine
        '''

        # Origin point
        ORIGIN.draw()

        # Stimuli path
        for iLine in range(N_LINE):

            # Que path (stimuli) ----
            stimuli_path = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                           lineColor = green, lineColorSpace = 'rgb255', 
                           vertices = (sti_path[iLine+1], sti_path[iLine+2]),
                           closeShape = False, pos = (0, 0))
            stimuli_path.draw()

        # Response path
        for iResp in range(len(resp_path)-1):
            response_path = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                            lineColor = magenta, lineColorSpace = 'rgb255', 
                            vertices = (sti_path[iResp], sti_path[iResp+1]),
                            closeShape = False, pos = (0, 0))
            response_path.draw()

        # Indicator
        indicator_point = visual.Circle(my_win, units =  'pix',
                           radius = 2, pos = (resp_path[iResp]),
                           fillColor = yellow, fillColorSpace = 'rgb255',
                           lineColor = yellow, lineColorSpace = 'rgb255', 
                           interpolate = True)
        indicator_line = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2,
                                     lineColor = yellow, lineColorSpace = 'rgb255',
                                     vertices = (resp_path[iResp], 
                                                 resp_path[iResp] + four_dict[key_meaning]),
                                     closeShape = False, pos = (0,0))
        # indicator_point.draw()
        indicator_line.draw()

        # End point
        end = visual.ShapeStim(my_win, units = 'pix', lineWidth = 2, 
                               lineColor = green, lineColorSpace = 'rgb255', 
                               vertices = (sti_path[-1] + np.dot(ARROW_WING1, 
                                                                  rotate), 
                                           sti_path[-1], 
                                           sti_path[-1] + np.dot(ARROW_WING2, 
                                                                  rotate)),
                               closeShape = False, pos = (0, 0))
        end.draw()

        # Flip the window
        my_win.flip()


        '''
        Response routine
        '''

        # Get response 
        response_hw, response_key, response_status = getAnything(mouse, joy)

        
        # if response_status == 1 and response_key != pre_key:
        if response_status == 1 and pre_status == 0:
            # Get current time
            print(iResp, N_LINE)
            current_time = core.getTime()
            key_meaning = interpret_key_ACC(response_hw, response_key) 

            # response determine the magenta line
            if key_meaning == tag_que[iResp]:
                resp_path.append(sti_path[iResp+2])
                iResp += 1
                if iResp >= N_LINE:
                    iResp = N_LINE
                    loopStatus = 0
            elif key_meaning == 'Abort':
                loopStatus = 0

            print(key_meaning)

            pre_key = response_key # Button status update

        pre_status = response_status  


# Close the window
my_win.close()