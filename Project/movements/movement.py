import logging


def hands_down(gandalf):
    names = list()
    times = list()
    keys = list()

    names.append("KneePitch")
    times.append([0.64, 1.04, 1.6])
    keys.append([0.116811, 0.127372, -0.030751])

    names.append("LElbowRoll")
    times.append([0.52, 0.96, 1, 1.24, 1.4, 1.88])
    keys.append([-0.98262, -0.441337, -0.832522, -0.892776, -0.981718, -1.05995])

    names.append("LElbowYaw")
    times.append([0.52, 0.96, 1, 1.24, 1.4, 1.88])
    keys.append([-1.23918, -1.13535, -1.62148, -1.57847, -1.51563, -1.49723])

    names.append("LHand")
    times.append([0.52, 1, 1.24, 1.4, 1.88])
    keys.append([0.856834, 0.8596, 0.796134, 0.6988, 0.5484])

    names.append("LShoulderPitch")
    times.append([0.52, 1, 1.24, 1.4, 1.88])
    keys.append([1.48267, 1.47567, 1.48182, 1.48487, 1.4772])

    names.append("LShoulderRoll")
    times.append([0.52, 0.96, 1, 1.24, 1.4, 1.88])
    keys.append([0.23781, -0.0226224, 0.246893, 0.231631, 0.216213, 0.220816])

    names.append("LWristYaw")
    times.append([0.52, 1, 1.24, 1.4, 1.88])
    keys.append([-0.709103, -0.70108, -0.713353, -0.730227, -0.72409])

    names.append("RElbowRoll")
    times.append([0.44, 0.92, 1.16, 1.32, 1.8])
    keys.append([1.30376, 0.941918, 0.992485, 1.02782, 1.1214])

    names.append("RElbowYaw")
    times.append([0.44, 0.92, 1.16, 1.32, 1.8])
    keys.append([1.2425, 1.89019, 1.59687, 1.47106, 1.46186])

    names.append("RHand")
    times.append([0.44, 0.92, 1.16, 1.32, 1.8])
    keys.append([0.1084, 0.8564, 0.760105, 0.6984, 0.5428])

    names.append("RShoulderPitch")
    times.append([0.44, 0.92, 1.16, 1.32, 1.8])
    keys.append([1.29538, 1.51257, 1.52171, 1.5187, 1.51563])

    names.append("RShoulderRoll")
    times.append([0.44, 0.92, 1.16, 1.32, 1.8])
    keys.append([-0.309147, -0.404274, -0.380428, -0.371443, -0.295341])

    names.append("RWristYaw")
    times.append([0.44, 0.92, 1.16, 1.32, 1.8])
    keys.append([0.791502, 0.868202, 0.880473, 0.89428, 0.891212])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        gandalf.robot.ALMotion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        logging.error("Error while moving pepper to see your face.", )
        raise err


def face_up(gandalf):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.64, 0.84, 1.28, 1.8])
    keys.append([-0.060645, 0.0181879, -0.240011, -0.178764])

    names.append("HeadYaw")
    times.append([0.64, 0.84, 1.28, 1.8])
    keys.append([0.032172, 0.032172, 0.032172, 0.032172])

    try:
        self.robot.ALMotion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        logging.error("Error while moving pepper to see your face.", )
        raise err