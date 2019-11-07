from Project.InitializedState import InitializedState
from Project.State import State


class StartupState(State):
    _next_state = None

    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """

        self.robot.ALTextToSpeech.say("Initializing")

        self._next_state = InitializedState(self.robot)

    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """
        return self._next_state
