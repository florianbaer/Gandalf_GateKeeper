from Project.StartupState import StartupState


class StateMachine:
    """
    The state machine that mimics the functionality of Pepper from a higher level.
    """
    robot = None
    _current_state = None
    _next_state = None

    def __init__(self, robot):
        """
        Initialize the state machine with the default state "Ready"
        """

        self.robot = robot
        self._next_state = StartupState(self.robot)

    def run(self):
        while self._next_state is not None:
            self._current_state = self._next_state
            print(self._current_state)
            self._current_state.run()
            self._next_state = self._current_state.next_state()
