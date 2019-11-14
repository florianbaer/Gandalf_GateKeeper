import logging

def initializing(gandalf):
    say = "initializing"
    logging.info(say)
    gandalf.robot.ALTextToSpeech.setLanguage("English")
    #gandalf.robot.ALTextToSpeech.say(say)
    gandalf.trigger("detecting_face")
