import logging
from math import pi


def move_back(gandalf):
    say = "Move back"
    logging.info(say)

    gandalf.robot.ALMotion.moveTo(0.4, 0, 90 * pi / 180)

    # trigger next state
    gandalf.trigger('re_initialize')
