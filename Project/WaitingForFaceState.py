import time

from Project.State import State
from Project.WelcomeDialogueState import WelcomeDialogueState


class WaitingForFaceState(State):
    memValue = "FaceDetected"
    _next_state = None


    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """
        print "Waiting for face"

        self.robot.ALFaceDetection.subscribe("Test_Face", 2000, 0.0 )

        val = self.robot.ALMemory.getData(self.memValue)
        # A simple loop that reads the memValue and checks whether faces are detected.
        while not (val and isinstance(val, list) and len(val) >= 2):
            time.sleep(0.5)
            val = self.robot.ALMemory.getData(self.memValue)

        # Check whether we got a valid output.
        print "face found"

        self._next_state = WelcomeDialogueState(self.robot)

    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """

        self.robot.ALFaceDetection.unsubscribe("Test_Face")
        pass