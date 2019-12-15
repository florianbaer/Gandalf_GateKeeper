import logging
import math


def face_up(gandalf, angle):
    try:
        gandalf.robot.ALMotion.setAngles("HeadPitch", math.radians(angle), 0.2)
    except BaseException, err:
        logging.error("Error while moving pepper to see your face.", )
        raise err