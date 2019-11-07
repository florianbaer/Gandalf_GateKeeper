import time


class Dialog:

    def __init__(self, robot):
        self.__al_tts = robot.ALTextToSpeech
        self.__al_audio = robot.ALAudioDevice
        self.__al_dialog = robot.session.service("ALDialog")
        self.__my_id = 1337
        self.__al_dialog.openSession(self.__my_id)
        self.__al_tts.setLanguage("English")

    def say(self, text_to_say):
        self.__al_tts.say(text_to_say)

    def say_slowly(self, text_to_say):
        original_speed = self.__al_tts.getParameter("speed")
        self.__al_tts.setParameter("speed", 50)
        self.__al_tts.say(text_to_say)
        self.__al_tts.setParameter("speed", original_speed)
        pass

    def shout(self, text_to_say):
        original_volume = self.__al_audio.getOutputVolume()
        self.__al_audio.setOutputVolume(min(original_volume + 20, 100))
        original_pitch = self.__al_tts.getParameter("pitch")
        pitch = 80
        self.__al_tts.setParameter("pitch", pitch)
        self.__al_tts.say(text_to_say)
        self.__al_tts.setParameter("pitch", original_pitch)
        self.__al_audio.setOutputVolume(original_volume)
        pass

    def add_simple_reaction(self, user_input, robot_output):
        topic_name = "hello_topic"
        topic_content = ('topic: ~' + topic_name + '()\n'
            'language: enu\n'
            'u:(' + user_input + ') ' + robot_output + '\n')
        print(topic_content)
        self.__al_dialog.loadTopicContent(topic_content)
        return topic_name

    def load_yes_no_question(self, question, reaction_yes, reaction_no):
        topic_name = "testpipapo"
        topic_content = ('topic: ~'+ topic_name +' ()\n'
                        'language: enu\n'
                        'proposal: ' + question + '\n'
                        '   u1: (no) '+ reaction_no + '\n'
                        '   u1: (yes) ' + reaction_yes
                         )
        self.__al_dialog.loadTopicContent(topic_content)
        return topic_name

    def ask_yes_no_question(self, topic):
        self.__al_dialog.activateTopic(topic)
        self.__al_dialog.subscribe('myself')
        self.__al_dialog.setFocus(topic)
        self.__al_dialog.forceOutput()  # start proposal sentence
        time.sleep(5)
        do_agree = self.__al_dialog.getUserData("agree", self.__my_id)
        self.__al_dialog.deactivateTopic(topic)
        return do_agree

    def start_topic(self, topic_name):
        self.__al_dialog.activateTopic(topic_name)
        self.__al_dialog.setFocus(topic_name)
        pass

    def stop_topic(self, topic_name):
        self.__al_dialog.deactivateTopic(topic_name)
        self.__al_dialog.unloadTopic(topic_name)
        pass

    def close_session(self):
        # to be implemented
        pass
