import logging
import time
from math import pi

def move_back(gandalf):
    say = "Move back"
    val = []
    person_passed = False
    logging.debug(say)

    gandalf.robot.ALPeoplePerception.subscribe("ALPeoplePerception", 2, 5)
    gandalf.robot.ALEngagementZones.subscribe("ALEngagementZones", 2, 5)

    # as long as nobody passed pepper, it shall wait
    while len(val) != 0 or not person_passed:

        val = gandalf.robot.ALMemory.getData("EngagementZones/PeopleInZone1")
        time.sleep(0.5)
        logging.debug(val)
        if len(val) > 0:
            person_passed = True
    gandalf.robot.ALPeoplePerception.unsubscribe("ALPeoplePerception")
    gandalf.robot.ALEngagementZones.unsubscribe("ALEngagementZones")
    gandalf.robot.ALMotion.moveTo(0.4, 0, 90 * pi / 180)

    # trigger starting state
    gandalf.trigger('re_initialize')

def callback():
    name, id, subId = 1
    logging.warning("OH nooooo {}{}{}",  name, id, subId)