# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:55:21 2019

@author: u0118077
"""

from psychopy import visual, event, core,  monitors
from psychopy.hardware import joystick


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


joystick.backend='pyglet'  # must match the Window
# my_win = visual.Window(size = (600, 400), units = 'pix', pos=(200,40), winType='pyglet')

# Load initial setting ----
# Preparing Window
my_win = visual.Window(size=(600, 400), pos=(0,0), monitor = mon, units = 'pix', 
                       screen = 1)




nJoys = joystick.getNumJoysticks()  # to check if we have any
id = 0
joy = joystick.Joystick(id)  # id must be <= nJoys - 1

nAxes = joy.getNumAxes()  # for interest

#Variables: FIXED and others

sscale = visual.RatingScale(my_win, pos=(0, -100), textSize=0.75, textColor='#808080', marker='glow', markerStart=4, stretch=1.2, acceptPreText=' ', acceptText=' ', labels=(), scale=None, showValue=False)
MAX_DURATION = 5
mouse = event.Mouse(visible=True,win=my_win)
experiment_timer = core.Clock()    

#trial_finished = False#
experiment_timer.reset()

mouse.clickReset()

j = 0    
while experiment_timer.getTime() < MAX_DURATION:
    sscale.draw()

    # (x,y) = mouse.getWheelRel()   
    # j =joy.getAllHats()
    j = joy.getButton(0) # 0= x 1 = A 2 =b 3=y
    # j = joy.getAxis(0) # 0= left

    print(j)
    # if j == [(-1,0)]:
        # print(j)

    # print(nJoys, id, joy, nAxes)
    my_win.flip()

    #reset the scale + get the rating + ReactionTimes
    sscale.reset()
    if experiment_timer.getTime() > MAX_DURATION:
        break

my_win.close()