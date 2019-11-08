from Project.State import State
from dialog import Dialog


class IntentionRecognizedState(State):
    _next_state = None

    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """
        self.robot.ALTextToSpeech.say("Please show me your validation card.")



    def next_state(self):
        """
        Returns the next state (or None) for the state machine.
        """
        return self._next_state
