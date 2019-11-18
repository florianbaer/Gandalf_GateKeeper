import time
import cv2
import numpy as np
from Project.excercises.camera import Camera
from Project.excercises.file_transfer import FileTransfer


def validation_card_reading(gandalf):
    remote_folder_path = "/home/nao/recordings/cameras/"
    file_name = "gatekeeper_" + str(time.time()) + ".jpg"
    local = "/Users/jabbathegut/Downloads/" + file_name
    camera = Camera(gandalf.robot)

    # configure text to speech
    gandalf.robot.ALTextToSpeech.setVolume(0.5)
    gandalf.robot.ALTextToSpeech.setLanguage("English")
    gandalf.robot.ALTextToSpeech.say("I'm going to have a look at your validation card.")
    gandalf.robot.ALTextToSpeech.say("Please hold your card in front of my eyes and keep it still.")

    time.sleep(2)

    gandalf.robot.ALTextToSpeech.say("Now I'm taking the picture.")

    # take a picture
    camera.take_picture(remote_folder_path, file_name)

    # copy file to local path
    remote = remote_folder_path + file_name
    file_transfer = FileTransfer(gandalf.robot)
    file_transfer.get(remote, local)
    file_transfer.close()

    # analyse card
    img = cv2.imread(remote_folder_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_color = np.array([136, 185, 171])
    upper_color = np.array([160, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours = cv2.findContours(mask, 1, 2)

    if len(contours) == 0:
        gandalf.robot.ALTextToSpeech.say("No Shape")
        gandalf.robot.ALTextToSpeech.say("I'm sorry, but I couldn't detect your card.")
    else:
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            # If shape is triangle return 0
            # If shape is circle return 1
            # If shape is not detected return 2
            if len(approx) == 3:
                gandalf.robot.ALTextToSpeech.say("Perfect, enjoy your stay.")
                break
            elif len(approx) > 10:
                gandalf.robot.ALTextToSpeech.say("I'm sorry, but I can't grant you access... Please go ahead.")
                break

