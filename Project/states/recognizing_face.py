import logging
import random
import time


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

def recognizing_face(gandalf):

    gandalf.robot.ALTextToSpeech.setLanguage("English")
    face_detected_mem_value = "FaceDetected"

    logging.info("recognizing face")
    gandalf.robot.ALFaceDetection.subscribe("Test_Face", 2000, 0.0)

    val = gandalf.robot.ALMemory.getData(face_detected_mem_value)
    name = None

    # A simple loop that reads the memValue and checks whether faces are detected.
    while not (val and isinstance(val, list) and len(val) >= 2):
        time.sleep(1)
        val = gandalf.robot.ALMemory.getData(face_detected_mem_value)
        name = _face_already_known(gandalf, val)

    gandalf.face_in_front = True

    # Check whether we got a valid output.
    logging.info("face found")

    if name is not None:
        gandalf.robot.ALAnimatedSpeech.say('I know you {}'.format(val[1][1][1][0]))
    else:
        rand = random.randint(0, 50000000)
        name = 'Peter{}'.format(rand)
        gandalf.robot.ALAnimatedSpeech.say('I don\'t know you, but i will learn you: {}'.format(name))
        gandalf.robot.ALAnimatedSpeech.say('Please look in my eyes, so i can learn recognizing you. i will tell you when i am done'.format(name))
        success = gandalf.robot.ALFaceDetection.learnFace(name)
        if success:
            gandalf.allowed_people_dict[name] = False
            gandalf.current_person = name
            gandalf.robot.ALAnimatedSpeech.say('got it, thank you')
        else:
            gandalf.robot.ALAnimatedSpeech.say('we have to try again')

    gandalf.robot.ALFaceDetection.unsubscribe("Test_Face")


    # Trigger transition
    # gandalf.trigger("detecting_face")
    gandalf.trigger("question_intention")

