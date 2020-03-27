# -*- coding: utf-8 -*-
"""
Created on Thu Jan 2 2020

Special thanks to: u0118077
Modified by EJ_Chang on Jan 6 2020
"""

from psychopy import visual, event, core
from psychopy.hardware import joystick


# Preparing window
my_win = visual.Window(size = (1920, 1080), units = 'pix', pos = (0, 0), screen = 1)

# Basic parameters for controller(joystick/wheel)
mouse = event.Mouse(visible = True, win = my_win)

# Basic parameters for visual objects(stimulu/indication)
# imageList = ['Slide1.png', 'Slide2.png', 'Slide3.png', 'Slide4.png', 'Slide5.png']
imageList = [
    'Slide1.png', 
    'Slide2.png', 
    'Slide3.png', 
    'Slide4.png', 
    'Slide5.png'
    ]

IndiX = [0, -231, -231+270, -231+540]
IndiY = [115, 115-46, 115-92, 115-138, -115]


# Timer setting
MAX_DURATION = 5
experiment_timer = core.Clock()

# Reset everything with pre-sets
experiment_timer.reset()
mouse.clickReset()

item = 0
img = visual.ImageStim(win = my_win, image = imageList[item], units = 'pix')
# slctHL: selected and highlighted = hover on
slctHL = visual.Rect(my_win, width = 270, height = 60, 
                        fillColor = (-0.7, -0.7, -0.7), fillColorSpace = 'rgb', 
                        pos = (IndiX[1], IndiY[item]), opacity = 0, units = 'pix')

expStatus = 1
layerNum = 1
bttnPress = mouse
NOT_STARTED = 0
STARTED = 1
bttnPress_status = NOT_STARTED
pre_X = 0
pre_Y = 0
pre_Mouse = (0, 0, 0)
preTimeStamp = 0

# ======   Exp Start ====== 
while expStatus == 1: 
# while experiment_timer.getTime() < MAX_DURATION:
    img.draw()
    slctHL.draw()

    if bttnPress_status == NOT_STARTED:
        bttnPress_status = STARTED
        (x, y) = mouse.getWheelRel()

    # Set break button
    if bttnPress_status == STARTED:
        # buttons = mouse.getPressed()
        buttons, times = mouse.getPressed(getTime = True)
        if buttons[2] == 1:
            print(times)
            break
        elif buttons[1] == 1 : # Need response interval = 250
            if buttons !=  pre_Mouse:
                layerNum = layerNum + 1
                print(times)
        pre_Mouse = buttons
        
    # Set response keysa
    if bttnPress_status == STARTED:
        (x, y) = mouse.getWheelRel()
        trialTime = experiment_timer.getTime()
        buttons = mouse.getPressed()
        if [x, y] != [pre_X, pre_Y]:
            if y <= -1:
                item = item - 1
                y = -1
            elif y >=  1:
                item = item + 1
                y = 1
            elif x >=  1 and trialTime - preTimeStamp > 0.25:
                layerNum = layerNum + 1
                item = 0
                x = 1
                core.wait(0.2)
            elif x <= -1 and trialTime - preTimeStamp > 0.25:
                layerNum = layerNum - 1            
                item = 0
                x = -1
                core.wait(0.2)

            [pre_X, pre_Y] = [x, y]
            preTimeStamp = trialTime

    # Set item limits
    if item >=  4: # Each layer has its limit number
        item = 4
    elif item <=  0:
        item = 0

    # Layer Number 
    if layerNum <=  1:
        layerNum = 1
    elif layerNum >=  4:
        layerNum = 4

    # Layer Behavior
    if layerNum == 1:
        img = visual.ImageStim(win = my_win, image = imageList[item], units = 'pix')
        slctHL = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7, -0.7, -0.7), 
                     fillColorSpace = 'rgb', pos = (IndiX[1], IndiY[item]), opacity = 0, units = 'pix')

    elif layerNum == 2: 
        slctHL = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7, -0.7, -0.7), 
                     fillColorSpace = 'rgb', pos = (IndiX[1], IndiY[item]), opacity = 0.8, units = 'pix')

    elif layerNum == 3:
        slctHL = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7, -0.7, -0.7), 
                     fillColorSpace = 'rgb', pos = (IndiX[2], IndiY[item]), opacity = 0.8, units = 'pix')

    elif layerNum == 4: 
        slctHL = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7, -0.7, -0.7), 
                     fillColorSpace = 'rgb', pos = (IndiX[3], IndiY[item]), opacity = 0.8, units = 'pix')

    my_win.flip()

# == == ==  EXp Ends == ==  == 
my_win.close()

