from Project.State import State
from Project.WaitingForFaceState import WaitingForFaceState


class InitializedState(State):
    _next_state = None

    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """
        self.robot.ALTextToSpeech.say("Initialized")

        self._next_state = WaitingForFaceState(self.robot)

    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """
        return self._next_state
