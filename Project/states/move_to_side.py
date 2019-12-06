import logging
import time
from math import pi


def move_to_side(gandalf):
    say = "Move to side"
    logging.info(say)




    # for some reason almath is not available..
    gandalf.robot.ALMotion.moveTo(0, 0.4, -90 * pi / 180)

    # trigger next state
    gandalf.trigger('move_back')


