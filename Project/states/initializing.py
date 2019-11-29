import logging
DISABLED = 'disabled'


def initializing(gandalf):

    gandalf.robot.ALTextToSpeech.setLanguage("English")
    say = "initializing"
    logging.info(say)
    # configure text to speech
    if gandalf.testing_mode:
        gandalf.robot.ALTextToSpeech.setVolume(1)
        gandalf.robot.ALTextToSpeech.say(say)

    if gandalf.robot.ALAutonomousLife.getState() != DISABLED:
        gandalf.robot.ALAutonomousLife.setState(DISABLED)
        gandalf.robot.ALRobotPosture.goToPosture("Stand", 0.8)
    # caution: collision system disabled!
    gandalf.robot.ALMotion.setExternalCollisionProtectionEnabled("Move", False)
    if gandalf.testing_mode:
        for face in gandalf.robot.ALFaceDetection.getLearnedFacesList():
            gandalf.robot.ALFaceDetection.forgetPerson(face)
            gandalf.robot.ALTextToSpeech.say('Instant alzheimer')

    # trigger next state
    gandalf.trigger("detecting_face")
