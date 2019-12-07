import logging
import time
from math import pi


def move_to_side(gandalf):
    say = "Move to side"
    logging.info(say)

    # enable laser
    gandalf.robot.ALLaser.laserON()
    gandalf.robot.ALLaser.setDetectingLength(20, 3000)
    gandalf.robot.ALLaser.setOpeningAngle(1.0, 1.0)

    lef_side_y = gandalf.robot.ALMemory.getData(
        "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg01/Y/Sensor/Value")

    while lef_side_y < 0.5:
        lef_side_y = gandalf.robot.ALMemory.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg01/Y/Sensor/Value")
        gandalf.robot.ALAnimatedSpeech.say("There's an obstacle to my left, move the obstacle away please.")
        time.sleep(2)

    # for some reason almath is not available..
    gandalf.robot.ALMotion.moveTo(0, 0.4, -90 * pi / 180)
    gandalf.robot.ALLaser.laserOFF()
    gandalf.trigger('move_back')



