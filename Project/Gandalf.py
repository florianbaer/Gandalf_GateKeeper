from transitions.extensions import GraphMachine as Machine

from Project.states.initializing import initializing
from Project.states.recognizing_face import recognizing_face
from Project.states.starting_up import starting_up
from Project.states.intention_recognizing import intention_recognizing
from Project.states.validation_card_reading import validation_card_reading


class Gandalf(object):

    face_in_front = False
    wants_to_enter = None

    STATES = ["start", "started", "initialized", "face_detected", "intention_recognized", "validate_card"]

    def __init__(self, robot):
        self.robot = robot

        # Initialize the state machine
        self.state_machine = Machine(model=self, states=self.STATES, queued=True, initial="start")

        self.state_machine.add_transition(
            trigger="starting_up",
            source="start",
            dest="started",
            after=lambda *args, **kwargs: starting_up(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="initializing",
            source="started",
            dest="initialized",
            after=lambda *args, **kwargs: initializing(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="detecting_face",
            source="*",
            dest="face_detected",
            after=lambda *args, **kwargs: recognizing_face(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="question_intention",
            source="face_detected",
            dest="intention_recognized",
            after=lambda *args, **kwargs: intention_recognizing(self, *args, **kwargs)
        )

        self.state_machine.add_transition(
            trigger="validate_entry",
            source="intention_recognized",
            dest="validate_card",
            after=lambda *args, **kwargs: validation_card_reading(self, *args, **kwargs)
        )

        self.state_machine.add_transition(
            trigger="re_initialize",
            source="*",
            dest="initialized",
            after=lambda *args, **kwargs: initializing(self, *args, **kwargs)
        )



    def wants_to_enter(self):
        return self.wants_to_enter

    def _next_state(self):
        return self.next_state()
