from transitions.extensions import GraphMachine as Machine

from Project.states.initializing import initializing
from Project.states.move_back import move_back
from Project.states.move_to_side import move_to_side
from Project.states.recognizing_face import recognizing_face
from Project.states.starting_up import starting_up
from Project.states.intention_recognizing import intention_recognizing
from Project.states.validation_card_reading import validation_card_reading
import logging

class Gandalf(object):

    face_in_front = False
    wants_to_enter = None
    testing_mode = False
    allowed_people_dict = {}
    current_person = None
    delete_faces = True
    force_make_queue = False

    STATES = ["start", "started", "initialized", "face_detected", "intention_recognized", "validate_card", "on_side", "access_denied"]

    def __init__(self, robot, testing_mode=False):
        self.robot = robot
        self.testing_mode = testing_mode

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
            source=["intention_recognized", "validate_card"],
            dest="validate_card",
            after=lambda *args, **kwargs: validation_card_reading(self, *args, **kwargs)
        )

        self.state_machine.add_transition(
            trigger="move_to_side",
            source="validate_card",
            dest="on_side",
            after=lambda *args, **kwargs: move_to_side(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
            trigger="move_back",
            source="on_side",
            dest="initialized",
            after=lambda *args, **kwargs: move_back(self, *args, **kwargs)
        )

        self.state_machine.add_transition(
            trigger="deny_access",
            source="validate_card",
            dest="access_denied",
            after=lambda *args, **kwargs: initializing(self, *args, **kwargs)
        )

        self.state_machine.add_transition(
            trigger="re_initialize",
            source="*",
            dest="initialized",
            after=lambda *args, **kwargs: initializing(self, *args, **kwargs)
        )

