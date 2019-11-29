import logging

def starting_up(gandalf):

    gandalf.robot.ALTextToSpeech.setLanguage("English")
    say = "Starting up"
    logging.info(say)

    if gandalf.testing_mode:
    gandalf.robot.ALTextToSpeech.setLanguage("English")
    gandalf.robot.ALTextToSpeech.setVolume(1)
    gandalf.robot.ALAnimatedSpeech.say(say)

    # trigger next state
    gandalf.trigger('initializing')
