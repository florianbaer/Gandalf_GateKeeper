import logging
import random
import time

from Project.excercises.dialog import Dialog

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

def ensure_human_is_ready(count, dialog):
    question_text = "Are you ready"

    if count == 0:
        question_text = question_text + "?"
    else:
        question_text = question_text + " now ?"

    topic_name = dialog.load_yes_no_question(question_text, "Good", "Okay")
    answer = dialog.ask_yes_no_question(topic_name)
    dialog.stop_topic(topic_name)
    dialog.close_session()
    return answer


def recognizing_face(gandalf):
    name = None
    gandalf.robot.ALTextToSpeech.setLanguage("English")

    # subscribe to the face detection service
    logging.info("recognizing face")
    gandalf.robot.ALFaceDetection.subscribe(FACE_CHECK, 2000, 0.0)

    # get face data related to the given MEM_VALUE
    val = gandalf.robot.ALMemory.getData(FACE_DETECTED_MEM_VALUE)

    # A simple loop that reads the memValue and checks whether faces are detected.
    while not (val and isinstance(val, list) and len(val) >= 2):
        time.sleep(1)
        val = gandalf.robot.ALMemory.getData(FACE_DETECTED_MEM_VALUE)
        name = _face_already_known(gandalf, val)

    # get number of faces that are detected
    number_of_faces = get_count_of_faces_in_front(val)
    logging.debug("Number of faces is: ")
    logging.debug(number_of_faces)
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

        # make sure human is ready, max number of tries is 2
        dialog = Dialog(gandalf.robot)
        count, ready = 0, 0
        while int(ready) == 0 and count < 2:
            ready = ensure_human_is_ready(count, dialog)
            count = count + 1

            if count != 2:
                time.sleep(1)

        if int(ready):
            gandalf.robot.ALAnimatedSpeech.say("I'm trying to learn your face now")
            success = gandalf.robot.ALFaceDetection.learnFace(name)
        else:
            success = False

        gandalf.robot.ALFaceDetection.unsubscribe(FACE_CHECK)

        if success:
            gandalf.current_person = name
            gandalf.robot.ALAnimatedSpeech.say('got it, thank you')
            gandalf.trigger("question_intention")
        else:
            gandalf.robot.ALAnimatedSpeech.say("Alright then, we have to try again. let's start again")
            gandalf.trigger("detecting_face")


