import time
import cv2
import numpy as np
from Project.helper.camera import Camera
from Project.helper.dialog import Dialog
from Project.helper.file_transfer import FileTransfer


def validation_card_reading(gandalf):
    if gandalf.current_person in gandalf.allowed_people_dict and gandalf.allowed_people_dict[gandalf.current_person]:
        gandalf.robot.ALTextToSpeech.say("Nice, your access is granted. I remember you from before!")
        gandalf.trigger("move_to_side")
    else:
        check_validation_card(gandalf)


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


def check_validation_card(gandalf):
    camera = Camera(gandalf.robot)
    dialog = Dialog(gandalf.robot)
    remote_folder_path = "/home/nao/recordings/cameras/"
    file_name = "validation_card.jpeg"
    local = file_name

    # configure text to speech
    gandalf.robot.ALTextToSpeech.setVolume(1)
    gandalf.robot.ALTextToSpeech.setLanguage("English")
    gandalf.robot.ALTextToSpeech.say(
        "I'm going to have a look at your validation card. Please hold your card in front of my eyes and keep it still.")

    # make sure human is ready, max number of tries is 2
    count, ready = 0, 0
    while int(ready) == 0 and count < 2:
        ready = ensure_human_is_ready(count, dialog)
        count = count + 1

        if count != 2 and not int(ready):
            time.sleep(1)

    if int(ready):
        # take a picture
        camera.take_picture(remote_folder_path, file_name)

        # copy file to local path
        remote = remote_folder_path + file_name
        file_transfer = FileTransfer(gandalf.robot)
        file_transfer.get(remote, local)
        file_transfer.close()

        # analyse card
        img = cv2.imread(local)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_color = np.array([135, 100, 130])
        upper_color = np.array([167, 255, 255])
        mask = cv2.inRange(hsv, lower_color, upper_color)
        contours, h = cv2.findContours(mask, 1, 2)

        if gandalf.testing_mode:
            # just used for testing purposes
            cv2.imshow('img', img)
            cv2.imshow('hsv', hsv)
            cv2.imshow('mask', mask)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        triangle_detected = False
        square_detected = False

        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            if len(approx) == 3:
                triangle_detected = True
            elif len(approx) == 4:
                square_detected = True

        if triangle_detected:
            gandalf.allowed_people_dict[gandalf.current_person] = True
            gandalf.robot.ALTextToSpeech.say("Perfect, enjoy your stay.")
            gandalf.trigger('move_to_side')
        elif square_detected:
            gandalf.allowed_people_dict[gandalf.current_person] = False
            gandalf.robot.ALTextToSpeech.say("I'm sorry, but I can't grant you access... Please go ahead.")
            gandalf.trigger('re_initialize')
        else:
            gandalf.allowed_people_dict[gandalf.current_person] = False
            gandalf.robot.ALTextToSpeech.say("I didn't recognize anything. We have to try again.")
            gandalf.trigger('validate_entry')

    else:
        gandalf.allowed_people_dict[gandalf.current_person] = False
        gandalf.robot.ALTextToSpeech.say("I dont think that this will work... Let's start again.")
        gandalf.trigger('validate_entry')
