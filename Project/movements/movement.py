import logging
import math


def hands_down(gandalf):

    try:
        pass
    except BaseException, err:
        print err


def face_up(gandalf, angle):

    names = list()
    times = list()
    keys = list()

    """
    names.append("HeadPitch")
    times.append([0.64, 0.84, 1.28, 1.8])
    keys.append([-0.060645, 0.0181879, -0.240011, -0.178764])

    names.append("HeadYaw")
    times.append([0.64, 0.84, 1.28, 1.8])
    keys.append([0.032172, 0.032172, 0.032172, 0.032172])
    """
    try:
        gandalf.robot.ALMotion.setAngles("HeadPitch", math.radians(angle), 0.2)
    except BaseException, err:
        logging.error("Error while moving pepper to see your face.", )
        raise err