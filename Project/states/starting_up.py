import logging

def starting_up(gandalf):
    say = "Starting up"
    logging.info(say)
    gandalf.robot.ALAnimatedSpeech.say(say)
    gandalf.trigger('initializing')
