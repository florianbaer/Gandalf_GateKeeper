class state:
    """
    Defines the state of the pepper application
    """

    def __init__(self):
        print 'Start running state:', self.__str__()

    def run(self):
        """
        Handle events that are delegated to the current state.
        """
        pass

    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """
        pass

    def __str__(self):
        """
        Returns the name of the current State.
        """
        return self.__class__.__name__
