
##### TRIALS #####
#experiment itself: The trials: a for loop of the list with all pairs of stimuli
for stimulus_1, stimulus_2 in Stimuli_List:
    while scale.noResponse:
        
        #Integrate an escape button
        if event.getKeys(keyList= ['escape']):
            esc_screen.draw()
            win.flip()
            event.waitKeys(keyList= key_presses)
            win.close()
        
        #defining + drawing the left and right images
        Image_Left = visual.ImageStim(win, image=stimulus_1, pos=POS_LEFT, size=SIZE_STIMULI)
        Image_Right = visual.ImageStim(win, image=stimulus_2, pos=POS_RIGHT, size=SIZE_STIMULI)    
        Image_Left.draw()
        Image_Right.draw()
        
        #drawing the scale + digits 1-7
        scale.draw()
        digits_scale.draw()
            
        win.flip()

    #reset the scale + get the rating + ReactionTimes
    scale.reset()
    rating = scale.getRating()
    decisionTime.append(scale.getRT())
    choiceHistory = scale.getHistory()
    
    #reset scale.noresponse for next trial
    scale.noResponse = True

##### END #####
#ending of the experiment: thank you screen
end_screen.draw()
win.flip()
event.waitKeys(keyList= key_presses)
win.close()
