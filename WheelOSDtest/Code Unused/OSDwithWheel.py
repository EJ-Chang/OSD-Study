# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:55:21 2019

Special thanks to: u0118077
"""

from psychopy import visual, event, core


#Variables: FIXED and others
my_win = visual.Window(size = (1920, 1080), units = 'pix', pos=(0,0), screen = 1)

# sscale = visual.TextStim(my_win, text = 'Say goodbye to 2019!', font = "Caecilia",
#                          pos=(400, 20))
# IndiX = [-231,-231+270,-231+270+270]
IndiX = -231
# IndiY = [115, 115-46, 115-46-46]
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
    (x,y) = mouse.getWheelRel()     
    buttons = mouse.getPressed()

    if buttons[2] == 1:
        break
        
    if layerNum ==1:
        if y >= 1 :
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)
            # expStatus = 0
            item = item + 1
            if item >=4:
                item = 4
            img = visual.ImageStim(win = my_win, image=imageList[item], units="pix")
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0, units = 'pix')

            # break
        elif y<= -1: 
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)
            item = item - 1
            if item <= 0:
                item = 0
            img = visual.ImageStim(win = my_win, image=imageList[item], units="pix")
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0, units = 'pix')

        elif x == -1:
            print('no!')
        elif x == 1 or buttons[1] ==1:
            print('go to layer 2')
            layerNum = 2
            IndiX = -231
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
            core.wait(0.1)
        my_win.flip()

    elif layerNum == 2:
        IndiX = -231
        if y >= 1:
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)

            IndiY = IndiY - 46
            if IndiY <= -115:
                IndiY = -115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')

        elif y <= -1:
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)
            IndiY = IndiY + 46
            if IndiY >= 115:
                IndiY = 115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
        elif x == -1:
            print('BACK to layer 1')
            layerNum = 1
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0, units = 'pix')
            core.wait(0.1)

        elif x == 1 or buttons[1] ==1:
            print('go to layer 3')
            layerNum = 3
            IndiX = -231+270
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
            core.wait(0.1)

        my_win.flip()
    elif layerNum == 3:

        IndiX = -231+270
        if y >= 1:
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)
            IndiY = IndiY - 46
            if IndiY <= -115:
                IndiY = -115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')

        elif y <= -1:
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)
            IndiY = IndiY + 46
            if IndiY >= 115:
                IndiY = 115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
        elif x == -1:
            print('BACK to layer 2')
            layerNum = 2
            IndiX = -231
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
            core.wait(0.1)

        elif x == 1 or buttons[1] ==1:
            print('go to layer 4')
            layerNum = 4
            IndiX = -231+270+270
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
            core.wait(0.1)

        my_win.flip()
    elif layerNum == 4:
        
        IndiX = -231+270 +270
        if y >= 1:
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)
            IndiY = IndiY - 46
            if IndiY <= -115:
                IndiY = -115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')

        elif y <= -1:
            print('Wheel Position:', int(x), int(y), '; Button Pressed:', buttons)
            IndiY = IndiY + 46
            if IndiY >= 115:
                IndiY = 115
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
        elif x == -1:
            print('back to layer 3')
            layerNum = 3
            IndiX = -231+270
            selectIndi = visual.Rect(my_win, width = 270, height = 60, fillColor = (-0.7,-0.7,-0.7), 
                                     fillColorSpace='rgb', pos=(IndiX, IndiY), opacity = 0.8, units = 'pix')
            core.wait(0.1)

        elif x == 1 or buttons[1] ==1:
            print('no more')
        my_win.flip()


my_win.close()


# if experiment_timer.getTime() > MAX_DURATION:
# break