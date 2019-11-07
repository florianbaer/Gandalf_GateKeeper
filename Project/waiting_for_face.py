import time

from Project.state import state


class waiting_for_face(state):
    memValue = "FaceDetected"
    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """
        self.robot.ALTextToSpeech.say("Waiting for face")

        self.robot.ALFaceDetection.subscribe("Test_Face", 2000, 0.0 )

        val = self.robot.ALMemory.getData(self.memValue)
        # A simple loop that reads the memValue and checks whether faces are detected.
        while (val and isinstance(val, list) and len(val) >= 2):
            time.sleep(0.5)
            val = self.robot.ALMemory.getData(self.memValue)

            # Check whether we got a valid output.
            self.robot.ALTextToSpeech.say("face found. face palm!")


    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """

        self.robot.ALFaceDetection.unsubscribe("Test_Face")
        pass