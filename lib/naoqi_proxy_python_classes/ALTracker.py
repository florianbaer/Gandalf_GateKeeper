#!/usr/bin/env python
# Class autogenerated from .\altrackerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running





class ALTracker(object):
    def __init__(self, session):
        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("ALTracker")

    def addEffector(self, pEffector):
        """DEPRECATED. Use setEffector instead. Add an end-effector to move for tracking.

        :param str pEffector: Name of effector. Could be: "Arms", "LArm" or "RArm".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.addEffector(pEffector)

    def addTarget(self, pTarget, pParams):
        """DEPRECATED. Use registerTarget() instead. Add a predefined target. Subscribe to corresponding extractor if Tracker is running..

        :param str pTarget: a predefined target to track.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        :param AL::ALValue pParams: a target parameters. (RedBall : set diameter of ball.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.addTarget(pTarget, pParams)

    def getActiveTarget(self):
        """Return active target name.

        :returns str: Tracked target name.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getActiveTarget()

    def getAvailableModes(self):
        """Get the list of predefined mode.

        :returns std::vector<std::string>: List of predefined mode.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getAvailableModes()

    def getEffector(self):
        """Get active effector.

        :returns str: Active effector name. Could be: "Arms", "LArm", "RArm" or "None".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getEffector()

    def getExtractorPeriod(self, pTarget):
        """Get the period of corresponding target name extractor.

        :param str pTarget: a predefined target name.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        :returns int: a period in milliseconds
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getExtractorPeriod(pTarget)

    def getManagedTargets(self):
        """DEPRECATED. Use getRegisteredTargets() instead. Return a list of managed targets names.

        :returns std::vector<std::string>: Managed targets names.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getManagedTargets()

    def getMaximumAcceleration(self):
        """Get the maximum acceleration for tracking.

        :returns float: The maximum acceleration in rad.s-2 .
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getMaximumAcceleration()

    def getMaximumDistanceDetection(self):
        """get the maximum distance for target detection in meter.

        :returns float: The maximum distance for target detection in meter.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getMaximumDistanceDetection()

    def getMaximumVelocity(self):
        """Get the maximum velocity for tracking.

        :returns float: The maximum velocity in rad.s-1 .
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getMaximumVelocity()

    def getMode(self):
        """Get the tracker current mode.

        :returns str: The current tracker mode.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getMode()

    def getMoveConfig(self):
        """Get the config for move modes.

        :returns AL::ALValue: ALMotion GaitConfig
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getMoveConfig()

    def getRegisteredTargets(self):
        """Return a list of registered targets names.

        :returns std::vector<std::string>: Registered targets names.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getRegisteredTargets()

    def getRelativePosition(self):
        """Get the robot position relative to target in Move mode.

        :returns AL::ALValue: The final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz].
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getRelativePosition()

    def getRobotPosition(self):
        """Only work with LandMarks target name. Returns the [x, y, z, wx, wy, wz] position of the robot in coordinate system setted with setMap API. This is done assuming an average target size, so it might not be very accurate.

        :returns std::vector<float>: Vector of 6 floats corresponding to the robot position 6D.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getRobotPosition()

    def getSearchFractionMaxSpeed(self):
        """Get search process fraction max speed.

        :returns float: a fraction max speed.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getSearchFractionMaxSpeed()

    def getSupportedTargets(self):
        """Return a list of supported targets names.

        :returns std::vector<std::string>: Supported targets names.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getSupportedTargets()

    def getTargetCoordinates(self):
        """Only work with LandMarks target name. Get objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]

        :returns AL::ALValue: objects coordinates.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getTargetCoordinates()

    def getTargetNames(self):
        """DEPRECATED. Use getSupportedTargets() instead. Return a list of targets names.

        :returns std::vector<std::string>: Valid targets names.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getTargetNames()

    def getTargetPosition(self, pFrame):
        """Returns the [x, y, z] position of the target in FRAME_TORSO. This is done assuming an average target size, so it might not be very accurate.

        :param int pFrame: target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
        :returns std::vector<float>: Vector of 3 floats corresponding to the target position 3D.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getTargetPosition(pFrame)

    def getTargetPosition2(self):
        """DEPRECATED. Use pointAt with frame instead. Returns the [x, y, z] position of the target in FRAME_TORSO. This is done assuming an average target size, so it might not be very accurate.

        :returns std::vector<float>: Vector of 3 floats corresponding to the target position 3D.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getTargetPosition()

    def getTimeOut(self):
        """get the timeout parameter for target lost.

        :returns int: time in milliseconds.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.getTimeOut()

    def initialize(self):
        """Initialize tracker parameters with default values.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.initialize()

    def isActive(self):
        """Return true if Tracker is running.

        :returns bool: True if Tracker is running.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.isActive()

    def isNewTargetDetected(self):
        """Return true if a new target was detected.

        :returns bool: True if a new target was detected since the last getTargetPosition().
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.isNewTargetDetected()

    def isSearchEnabled(self):
        """Return true if the target search process is enabled.

        :returns bool: If true the target search process is enabled.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.isSearchEnabled()

    def isTargetLost(self):
        """Return true if the target was lost.

        :returns bool: True if the target was lost.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.isTargetLost()

    def lookAt(self, pPosition, pFrame, pFractionMaxSpeed, pUseWholeBody):
        """Look at the target position with head.

        :param std::vector<float> pPosition: position 3D [x, y, z] x position must be striclty positif.
        :param int pFrame: target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
        :param float pFractionMaxSpeed: The fraction of maximum speed to use. Must be between 0 and 1.
        :param bool pUseWholeBody: If true, use whole body constraints.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.lookAt(pPosition, pFrame, pFractionMaxSpeed, pUseWholeBody)

    def lookAt2(self, pPosition, pFractionMaxSpeed, pUseWholeBody):
        """DEPRECATED. Use lookAt with frame instead. Look at the target position with head.

        :param std::vector<float> pPosition: position 3D [x, y, z] to look in FRAME_TORSO. x position must be striclty positif.
        :param float pFractionMaxSpeed: The fraction of maximum speed to use. Must be between 0 and 1.
        :param bool pUseWholeBody: If true, use whole body constraints.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.lookAt(pPosition, pFractionMaxSpeed, pUseWholeBody)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.ping()

    def pointAt(self, pEffector, pPosition, pFrame, pFractionMaxSpeed):
        """Point at the target position with arms.

        :param str pEffector: effector name. Could be "Arms", "LArm", "RArm".
        :param std::vector<float> pPosition: position 3D [x, y, z] to point in FRAME_TORSO. x position must be striclty positif.
        :param int pFrame: target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
        :param float pFractionMaxSpeed: The fraction of maximum speed to use. Must be between 0 and 1.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.pointAt(pEffector, pPosition, pFrame, pFractionMaxSpeed)

    def pointAt2(self, pEffector, pPosition, pFractionMaxSpeed):
        """DEPRECATED. Use pointAt with frame instead. Point at the target position with arms.

        :param str pEffector: effector name. Could be "Arms", "LArm", "RArm".
        :param std::vector<float> pPosition: position 3D [x, y, z] to point in FRAME_TORSO. x position must be striclty positif.
        :param float pFractionMaxSpeed: The fraction of maximum speed to use. Must be between 0 and 1.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.pointAt(pEffector, pPosition, pFractionMaxSpeed)

    def registerTarget(self, pTarget, pParams):
        """Register a predefined target. Subscribe to corresponding extractor if Tracker is running..

        :param str pTarget: a predefined target to track.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        :param AL::ALValue pParams: a target parameters. (RedBall : set diameter of ball.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.registerTarget(pTarget, pParams)

    def removeAllTargets(self):
        """DEPRECATED. Use unregisterAllTargets() instead. Remove all managed targets except active target and stop corresponding extractor.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.removeAllTargets()

    def removeEffector(self, pEffector):
        """DEPRECATED. Use setEffector("None") instead. Remove an end-effector from tracking.

        :param str pEffector: Name of effector. Could be: "Arms", "LArm" or "RArm".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.removeEffector(pEffector)

    def removeTarget(self, pTarget):
        """DEPRECATED. Use unregisterTarget() instead. Remove target name and stop corresponding extractor.

        :param str pTarget: a predefined target to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.removeTarget(pTarget)

    def removeTargets(self, pTarget):
        """DEPRECATED. Use unregisterTargets() instead. Remove a list of target names and stop corresponding extractor.

        :param std::vector<std::string> pTarget: a predefined target list to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.removeTargets(pTarget)

    def setEffector(self, pEffector):
        """Set an end-effector to move for tracking.

        :param str pEffector: Name of effector. Could be: "Arms", "LArm", "RArm" or "None".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setEffector(pEffector)

    def setExtractorPeriod(self, pTarget, pPeriod):
        """Set a period for the corresponding target name extractor.

        :param str pTarget: a predefined target name.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        :param int pPeriod: a period in milliseconds
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setExtractorPeriod(pTarget, pPeriod)

    def setMaximumAcceleration(self, pAcceleration):
        """Set the maximum acceleration for tracking.

        :param float pAcceleration: The maximum acceleration in rad.s-2 .
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setMaximumAcceleration(pAcceleration)

    def setMaximumDistanceDetection(self, pMaxDistance):
        """set the maximum target detection distance in meter.

        :param float pMaxDistance: The maximum distance for target detection in meter.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setMaximumDistanceDetection(pMaxDistance)

    def setMaximumVelocity(self, pVelocity):
        """Set the maximum velocity for tracking.

        :param float pVelocity: The maximum velocity in rad.s-1 .
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setMaximumVelocity(pVelocity)

    def setMode(self, pMode):
        """Set the tracker in the predefined mode.Could be "Head", "WholeBody" or "Move".

        :param str pMode: a predefined mode.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setMode(pMode)

    def setMoveConfig(self, config):
        """set a config for move modes.

        :param AL::ALValue config: ALMotion GaitConfig
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setMoveConfig(config)

    def setRelativePosition(self, target):
        """Set the robot position relative to target in Move mode.

        :param AL::ALValue target: Set the final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz].
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setRelativePosition(target)

    def setSearchFractionMaxSpeed(self, pFractionMaxSpeed):
        """Set search process fraction max speed.

        :param float pFractionMaxSpeed: a fraction max speed.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setSearchFractionMaxSpeed(pFractionMaxSpeed)

    def setTargetCoordinates(self, pCoord):
        """Only work with LandMarks target name. Set objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]

        :param AL::ALValue pCoord: objects coordinates.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setTargetCoordinates(pCoord)

    def setTimeOut(self, pTimeMs):
        """set the timeout parameter for target lost.

        :param int pTimeMs: time in milliseconds.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.setTimeOut(pTimeMs)

    def stopTracker(self):
        """Stop the tracker.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.stopTracker()

    def toggleSearch(self, pSearch):
        """Enables/disables the target search process. Target search process occurs only when the target is lost.

        :param bool pSearch: If true and if the target is lost, the robot moves the head in order to find the target. If false and if the target is lost the robot does not move.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.toggleSearch(pSearch)

    def track(self, pTarget):
        """Set the predefided target to track and start the tracking process if not started.

        :param str pTarget: a predefined target to track.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.track(pTarget)

    def trackEvent(self, pEventName):
        """Track event and start the tracking process if not started.

        :param str pEventName: a event name to track.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.trackEvent(pEventName)

    def unregisterAllTargets(self):
        """Unregister all targets except active target and stop corresponding extractor.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.unregisterAllTargets()

    def unregisterTarget(self, pTarget):
        """Unregister target name and stop corresponding extractor.

        :param str pTarget: a predefined target to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.unregisterTarget(pTarget)

    def unregisterTargets(self, pTarget):
        """Unregister a list of target names and stop corresponding extractor.

        :param std::vector<std::string> pTarget: a predefined target list to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.unregisterTargets(pTarget)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALTracker")
        return self.proxy.version()
