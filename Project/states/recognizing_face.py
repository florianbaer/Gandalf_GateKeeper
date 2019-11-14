import logging
import time


def recognizing_face(gandalf):
    faceDetectedMemValue = "FaceDetected"

    logging.info("recognizing face")
    gandalf.robot.ALFaceDetection.subscribe("Test_Face", 2000, 0.0)

    val = gandalf.robot.ALMemory.getData(faceDetectedMemValue)
    name = None
    # A simple loop that reads the memValue and checks whether faces are detected.
    while not (val and isinstance(val, list) and len(val) >= 2):
        time.sleep(0.5)
        val = gandalf.robot.ALMemory.getData(faceDetectedMemValue)
        name = _face_already_known(gandalf, val)

    gandalf.face_in_front = True
    # Check whether we got a valid output.
    logging.info("face found")
    gandalf.robot.ALFaceDetection.unsubscribe("Test_Face")
    if name is not None:
        gandalf.robot.ALAnimatedSpeech.say('I know you {}'.format(val[1][1][1][0]))
    gandalf.trigger("question_intention")


def _face_already_known(gandalf, val):
    faces = gandalf.robot.ALFaceDetection.getLearnedFacesList()
    logging.debug(faces)
    if (val and isinstance(val, list) and len(val) >= 2 and len(val[1][1]) > 0):
        logging.debug(val[1][1][1][0])
        return val[1][1][1][0]
    # gandalf.robot.ALFaceDetection.reLearnFace("Peter")
    faces = gandalf.robot.ALFaceDetection.getLearnedFacesList()
    logging.debug(faces)
    logging.debug(val)
    return None

