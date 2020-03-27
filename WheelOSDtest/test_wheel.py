# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:55:21 2019

@author: u0118077
"""

from psychopy import visual, event, core


#Variables: FIXED and others
my_win = visual.Window(size = (600, 400), units = 'pix', pos=(200,40))
sscale = visual.RatingScale(my_win, pos=(0, -100), textSize=0.75,
 textColor='#808080', marker='glow', markerStart=4, stretch=1.2, 
 acceptPreText=' ', acceptText=' ', labels=(), scale=None, showValue=False)
MAX_DURATION = 5
mouse = event.Mouse(visible=True,win=my_win)
experiment_timer = core.Clock()    

#trial_finished = False#
experiment_timer.reset()

mouse.clickReset()
    
while experiment_timer.getTime() < MAX_DURATION:
        sscale.draw()
        
        (x,y) = mouse.getWheelRel()     
        print(x,y)
        my_win.flip()
                
                    #reset the scale + get the rating + ReactionTimes
        sscale.reset()
        if experiment_timer.getTime() > MAX_DURATION:
            break

my_win.close()