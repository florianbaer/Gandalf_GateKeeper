import logging
import random
import time

FACE_CHECK = "Test_Face"
FACE_DETECTED_MEM_VALUE = "FaceDetected"


def _face_already_known(gandalf, val):

    if (val and isinstance(val, list) and len(val) >= 2 and len(val[1][1]) > 0):
        logging.debug(val[1][1][1][0])
        return val[1][1][1][0]
    logging.debug(val)
    return None


def get_count_of_faces_in_front(val):
    logging.debug(val)
    return len(val) >= 2 and len(val[1][1])


def recognizing_face(gandalf):
    gandalf.robot.ALTextToSpeech.setLanguage("English")

    logging.info("recognizing face")
    gandalf.robot.ALFaceDetection.subscribe(FACE_CHECK, 2000, 0.0)

    val = gandalf.robot.ALMemory.getData(FACE_DETECTED_MEM_VALUE)
    logging.debug("Debug dump from face")
    logging.debug(val)
    name = None

    # A simple loop that reads the memValue and checks whether faces are detected.
    while not (val and isinstance(val, list) and len(val) >= 2):
        time.sleep(1)
        val = gandalf.robot.ALMemory.getData(FACE_DETECTED_MEM_VALUE)
        name = _face_already_known(gandalf, val)

    number_of_faces = get_count_of_faces_in_front(val)
    logging.debug("Number of faces is: ")
    logging.debug(number_of_faces)

    # Check whether we got a valid output.
    logging.info("face found")
    gandalf.face_in_front = True

    if name is not None:
        name = val[1][1][1][0]
        gandalf.robot.ALAnimatedSpeech.say('I know you {}'.format(name))
        gandalf.current_person = name
        gandalf.robot.ALFaceDetection.unsubscribe(FACE_CHECK)
        gandalf.trigger("question_intention")
    else:
        rand = random.randint(0, 50000000)
        name = 'Peter{}'.format(rand)
        gandalf.robot.ALAnimatedSpeech.say('I don\'t know you, but i will learn you: {}'.format(name))
        gandalf.robot.ALAnimatedSpeech.say('Please look in my eyes, so i can learn recognizing you. i will tell you when i am done'.format(name))
        success = gandalf.robot.ALFaceDetection.learnFace(name)

        gandalf.robot.ALFaceDetection.unsubscribe(FACE_CHECK)

        if success:
            gandalf.current_person = name
            gandalf.robot.ALAnimatedSpeech.say('got it, thank you')
            gandalf.trigger("question_intention")
        else:
            gandalf.robot.ALAnimatedSpeech.say('we have to try again')
            gandalf.trigger("detecting_face")



    # Trigger transition
    # gandalf.trigger("detecting_face")

