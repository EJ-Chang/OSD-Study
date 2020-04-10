# -*- coding: utf-8 -*-

def getAnything(mouse, joy):
    buttons = mouse.getPressed()
    (wheel_x, wheel_y) = mouse.getWheelRel()
    dPad = joy.getAllHats()
    botton_x = joy.getButton(0)
    return buttons, (wheel_x, wheel_y), dPad, botton_x
