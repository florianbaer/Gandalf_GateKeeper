import logging
from math import pi


def move_to_side(gandalf):
    say = "Move to side"
    logging.info(say)

    gandalf.robot.ALMotion.moveTo(0, 0.4, -90 * pi / 180)

    # trigger next state
    gandalf.trigger('move_back')
