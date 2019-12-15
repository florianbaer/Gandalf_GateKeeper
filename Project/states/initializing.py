import logging
import time

from Project.helper import movement

DISABLED = 'disabled'


def initializing(gandalf):
    say = "initializing"
    logging.info(say)

    # configure text to speech
    if gandalf.testing_mode:
        gandalf.robot.ALTextToSpeech.setLanguage("English")
        gandalf.robot.ALTextToSpeech.setVolume(1)
        gandalf.robot.ALTextToSpeech.say(say)

    # make sure autonomous life is disabled and pepper is standing upright
    if gandalf.robot.ALAutonomousLife.getState() != DISABLED:
        gandalf.robot.ALAutonomousLife.setState(DISABLED)

    # make robot stand upright at the beginning
    gandalf.robot.ALRobotPosture.goToPosture("Stand", 0.8)
    time.sleep(1)
    movement.face_up(gandalf, -10)

    # set Engagement Mode
    gandalf.robot.ALBasicAwareness.setEngagementMode("FullyEngaged")
    gandalf.robot.ALBasicAwareness.setStimulusDetectionEnabled("People", True)
    gandalf.robot.ALBasicAwareness.setTrackingMode("Head")
    gandalf.robot.ALBasicAwareness.startAwareness()

    # caution: collision system disabled!
    gandalf.robot.ALMotion.setExternalCollisionProtectionEnabled("Move", False)
    if gandalf.testing_mode:
        for face in gandalf.robot.ALFaceDetection.getLearnedFacesList():
            gandalf.robot.ALFaceDetection.forgetPerson(face)
            gandalf.robot.ALTextToSpeech.say('Instant alzheimer')

    # trigger next state
    gandalf.trigger("detecting_face")
