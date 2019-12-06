import logging
import time
from math import pi
gotit = False

def move_back(gandalf):
    say = "Move back"
    val = []
    logging.debug(say)
    while len(val) == 0:
        gandalf.robot.ALMemory.subscribeToEvent("EngagementZones","PersonEnteredZone1", "callback")
        val = gandalf.robot.ALMemory.getData("EngagementZones/PeopleInZone1")
        logging.debug(val)
        time.sleep(2)
        gandalf.robot.ALMemory.unsubscribeToEvent("EngagementZones","PersonEnteredZone1")

    gandalf.robot.ALMotion.moveTo(0.4, 0, 90 * pi / 180)

    gandalf.trigger('re_initialize')

