import logging

from Project.excercises.dialog import Dialog


def intention_recognizing(gandalf):
    log = logging.getLogger(__name__)

    log.debug("starting dialogue")
    dialog = Dialog(gandalf.robot)

    # configure text to speech
    gandalf.robot.ALTextToSpeech.setVolume(0.5)

    # simple yes no question
    topic_name = dialog.load_yes_no_question("Do you want to enter?", "Cool", "Pity")
    answer = dialog.ask_yes_no_question(topic_name)
    dialog.stop_topic(topic_name)
    dialog.close_session()

    # if answer YES set next state to IntentionRecognizedState
    if answer == "1":
        gandalf.wants_to_enter = True

    # else set next state to InitializedState
    else:
        gandalf.wants_to_enter = False

    if gandalf.wants_to_enter:
        gandalf.trigger("validate_entry")
    else:
        gandalf.trigger("re_initialize")
