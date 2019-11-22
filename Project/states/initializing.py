import logging


def initializing(gandalf):
    say = "initializing"
    logging.info(say)

    # configure text to speech
    gandalf.robot.ALTextToSpeech.setVolume(0.5)
    gandalf.robot.ALTextToSpeech.say(say)

    # trigger next state
    gandalf.trigger("detecting_face")
