#!/usr/bin/env python
# Class autogenerated from .\albodytemperatureproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running





class ALBodyTemperature(object):
    def __init__(self, session):
        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("ALBodyTemperature")

    def areNotificationsEnabled(self):
        """Return true if notifications are active.

        :returns bool: Return True if notifications are active.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALBodyTemperature")
        return self.proxy.areNotificationsEnabled()

    def getTemperatureDiagnosis(self):
        """The actual state of the temperature diagnosis.

        :returns AL::ALValue: Return the current temperature diagnosis.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALBodyTemperature")
        return self.proxy.getTemperatureDiagnosis()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALBodyTemperature")
        return self.proxy.ping()

    def setEnableNotifications(self, enable):
        """Enables / Disables temperature notifications.

        :param bool enable: If True enable temperature notifications. If False disable temperature notifications.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALBodyTemperature")
        return self.proxy.setEnableNotifications(enable)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALBodyTemperature")
        return self.proxy.version()
