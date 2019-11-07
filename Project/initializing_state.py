from Project.initialized_state import initialized_state
from Project.state import state

class initializing_state(state):

    _next_state = None

    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """

        self._next_state = initialized_state(self.robot)

        self.robot.ALTextToSpeech.say("Initializing")

    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """
        return self._next_state