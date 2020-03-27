# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:55:21 2019

Special thanks to: u0118077
"""

from psychopy import visual, event, core
from psychopy.hardware import joystick


joystick.backend='pyglet'  # must match the Window


#Variables: FIXED and others
my_win = visual.Window(size = (1920, 1080), units = 'pix', pos=(0,0), screen = 1)


nJoys = joystick.getNumJoysticks()  # to check if we have any
id = 0
joy = joystick.Joystick(id)  # id must be <= nJoys - 1

nAxes = joy.getNumAxes()  # for interest


IndiX = -231
IndiY = 115
selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0, units = 'pix')

imageList = ['Slide1.png', 'Slide2.png', 'Slide3.png', 'Slide4.png', 'Slide5.png']
secondLayer = ['Slide7.png', 'Slide8.png', 'Slide9.png', 'Slide10.png']
mergeList = [imageList, secondLayer]

MAX_DURATION = 5
mouse = event.Mouse(visible = True, win = my_win)
experiment_timer = core.Clock()

#trial_finished = False#
experiment_timer.reset()

mouse.clickReset()
#  Exp Start =======
# while experiment_timer.getTime() < MAX_DURATION:
expStatus = 1
item = 0
img = visual.ImageStim(win = my_win, image=imageList[item], units="pix")
layerNum = 1
testNum = 0
x = 0
while expStatus == 1: 
    img.draw()
    selectIndi.draw()
    # (x,y) = mouse.getWheelRel()     
    # buttons = mouse.getPressed()
    botton_x = joy.getButton(0) # 0=x 1=A 2=b 3=y
    botton_a = joy.getButton(1)
    botton_b = joy.getButton(2)
    botton_y = joy.getButton(3)
    buttons = [botton_x,botton_y,botton_a,botton_b]
    j =joy.getAllHats()

    if botton_x == True:
        break
        
    if layerNum ==1:
        if j == [(0,-1)] :
            print('Wheel Position:',j,'; Button Pressed:', buttons)
            # expStatus = 0
            item = item + 1
            if item >=4:
                item = 4
            img = visual.ImageStim(win = my_win, image=imageList[item], units="pix")
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0, units = 'pix')

            # break
        elif j == [(0,1)] :
            print('Wheel Position:',j, '; Button Pressed:', buttons)
            item = item - 1
            if item <= 0:
                item = 0
            img = visual.ImageStim(win = my_win, image=imageList[item], units="pix")
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0, units = 'pix')

        elif j == [(1,0)] :
            print('no!')
        elif j == [(-1,0)] :
            print('go to layer 2')
            layerNum = 2
            core.wait(0.1)
        my_win.flip()

    elif layerNum == 2:
        IndiX = -231
        if j == [(0,-1)]:
            print('Wheel Position:', j, '; Button Pressed:', buttons)

            IndiY = IndiY - 46
            if IndiY <= -115:
                IndiY = -115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')

        elif j == [(0,1)]:
            print('Wheel Position:', j, '; Button Pressed:', buttons)
            IndiY = IndiY + 46
            if IndiY >= 115:
                IndiY = 115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
        elif j == [(1,0)]:
            print('BACK to layer 1')
            layerNum = 1
            core.wait(0.1)

        elif j == [(-1,0)]:
            print('go to layer 3')
            layerNum = 3
            core.wait(0.1)

        my_win.flip()
    elif layerNum == 3:

        IndiX = -231+270
        if j == [(0,-1)]:
            print('Wheel Position:', j, '; Button Pressed:', buttons)
            IndiY = IndiY - 46
            if IndiY <= -115:
                IndiY = -115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')

        elif j == [(0,1)]:
            print('Wheel Position:', j, '; Button Pressed:', buttons)
            IndiY = IndiY + 46
            if IndiY >= 115:
                IndiY = 115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
        elif j == [(1,0)]:
            print('BACK to layer 2')
            layerNum = 2
            core.wait(0.1)

        elif j == [(-1,0)]:
            print('go to layer 4')
            layerNum = 4
            core.wait(0.1)

        my_win.flip()
    elif layerNum == 4:
        
        IndiX = -231+270 +270
        if j == [(0,-1)]:
            print('Wheel Position:', j, '; Button Pressed:', buttons)
            IndiY = IndiY - 46
            if IndiY <= -115:
                IndiY = -115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')

        elif j == [(0,1)]:
            print('Wheel Position:', j, '; Button Pressed:', buttons)
            IndiY = IndiY + 46
            if IndiY >= 115:
                IndiY = 115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
        elif j == [(1,0)]:
            print('back to layer 3')
            layerNum = 3
            core.wait(0.1)

        elif j == [(-1,0)]:
            print('no more')
        my_win.flip()


my_win.close()


# if experiment_timer.getTime() > MAX_DURATION:
# break