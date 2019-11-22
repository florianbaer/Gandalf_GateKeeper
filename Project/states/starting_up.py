import logging

def starting_up(gandalf):
    say = "Starting up"
    logging.info(say)

    # configure text to speech
    gandalf.robot.ALTextToSpeech.setVolume(0.5)
    gandalf.robot.ALAnimatedSpeech.say(say)

    # trigger next state
    gandalf.trigger('initializing')
