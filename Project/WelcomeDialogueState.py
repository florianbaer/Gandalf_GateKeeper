import time

from Project.State import State
from dialog import Dialog
from Project.InitializedState import InitializedState


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

        topic_name = dialog.load_yes_no_question("Do you want to enter?", "Cool", "Pitty")

        dialog.start_topic(topic_name)
        time.sleep(20)
        dialog.stop_topic(topic_name)

        dialog.close_session()

        self._next_state = InitializedState(self.robot)

    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """
        return self._next_state