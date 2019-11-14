import logging
import time


def recognizing_face(gandalf):
    faceDetectedMemValue = "FaceDetected"

    say = "recognizing face"
    logging.info(say)
    gandalf.robot.ALFaceDetection.subscribe("Test_Face", 2000, 0.0)

    val = gandalf.robot.ALMemory.getData(faceDetectedMemValue)
    # A simple loop that reads the memValue and checks whether faces are detected.
    while not (val and isinstance(val, list) and len(val) >= 2):
        time.sleep(0.5)
        val = gandalf.robot.ALMemory.getData(faceDetectedMemValue)
    gandalf.face_in_front = True
    # Check whether we got a valid output.
    logging.info("face found")
    gandalf.robot.ALFaceDetection.unsubscribe("Test_Face")
    gandalf.trigger("question_intention")



