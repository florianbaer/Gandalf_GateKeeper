import time

from Project.IntentionRecognizedState import IntentionRecognizedState
from Project.State import State
from dialog import Dialog


class WelcomeDialogueState(State):
    _next_state = None

    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """
        print "starting dialogue"
        dialog = Dialog(self.robot)

        # simple yes no question
        topic_name = dialog.load_yes_no_question("Do you want to enter?", "Cool", "Pity")
        dialog.ask_yes_no_question(topic_name)
        time.sleep(20)
        dialog.stop_topic(topic_name)
        dialog.close_session()

        from Project.InitializedState import InitializedState
        self.next_state = InitializedState(self.robot)

    def next_state(self):
        """
        Returns the next state (or None) for the state machine.
        """
        return self._next_state
