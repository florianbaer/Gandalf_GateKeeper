import time

from dialog import Dialog
import logging


def intention_recognizing(gandalf):
    log = logging.getLogger(__name__)
    log.debug("starting dialogue")
    dialog = Dialog(gandalf.robot)

    # simple yes no question
    topic_name = dialog.load_yes_no_question("Do you want to enter?", "Cool", "Pity")
    answer = dialog.ask_yes_no_question(topic_name)
    time.sleep(20)
    dialog.stop_topic(topic_name)
    dialog.close_session()

    # if answer YES set next state to IntentionRecognizedState
    if answer == 1:
        gandalf.wants_to_enter = True

    # else set next state to InitializedState
    else:
        gandalf.wants_to_enter = False