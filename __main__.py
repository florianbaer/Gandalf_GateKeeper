from Project.Gandalf import Gandalf
from lib.PepperConfiguration import PepperConfiguration
from lib.Robot import Robot
import logging
import sys

# configure logging
logging.basicConfig(level=logging.DEBUG)

config = PepperConfiguration("Amber")
robot = Robot(config)

if __name__ == "__main__":
    gandalf = Gandalf(robot, testing_mode=False)
    #gandalf.state_machine.get_graph().draw(sys.argv[1], prog="dot")
    gandalf.starting_up()
