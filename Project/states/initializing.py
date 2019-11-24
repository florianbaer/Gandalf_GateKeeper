import logging


def initializing(gandalf):
    say = "initializing"
    logging.info(say)
    # configure text to speech
    gandalf.robot.ALTextToSpeech.setVolume(0.5)
    gandalf.robot.ALTextToSpeech.say(say)

    for face in gandalf.robot.ALFaceDetection.getLearnedFacesList():
        gandalf.robot.ALFaceDetection.forgetPerson(face)
        gandalf.robot.ALTextToSpeech.say('Instant alzheimer')
    # trigger next state
    gandalf.trigger("detecting_face")
