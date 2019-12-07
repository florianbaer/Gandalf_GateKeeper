import logging
import time
from math import pi

def move_back(gandalf):
    say = "Move back"
    val = []
    person_passed = False
    logging.debug(say)

    # as long as nobody passed pepper, it shall wait
    while len(val) != 0 or not person_passed:
        # magic event handling
        gandalf.robot.ALEngagementZones.subscribe("EngagementZones/PeopleInZone1", 200, 200)
        gandalf.robot.ALMemory.subscribeToEvent("EngagementZones","PeopleInZone1", "callback")
        val = gandalf.robot.ALMemory.getData("EngagementZones/PeopleInZone1")
        time.sleep(2)
        logging.debug(val)
        if len(val) > 0:
            person_passed = True
        gandalf.robot.ALMemory.unsubscribeToEvent("EngagementZones","PeopleInZone1")
        gandalf.robot.ALEngagementZones.unsubscribe("EngagementZones/PeopleInZone1")

    gandalf.robot.ALMotion.moveTo(0.4, 0, 90 * pi / 180)

    # trigger starting state
    gandalf.trigger('re_initialize')

