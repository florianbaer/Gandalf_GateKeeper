import logging

def starting_up(gandalf):

    gandalf.robot.ALTextToSpeech.setLanguage("English")
    say = "Starting up"
    logging.info(say)

    # configure text to speech
    gandalf.robot.ALTextToSpeech.setVolume(1)
    gandalf.robot.ALAnimatedSpeech.say(say)

    # trigger next state
    gandalf.trigger('initializing')
