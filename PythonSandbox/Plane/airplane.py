class Airplane:
    def __init__(self, planeID, numPassengers, flightPriority, flightTime):
        self.planeID = planeID
        self.numPassengers = numPassengers
        self.flightPriority= flightPriority
        self.flightTime = flightTime
    def getPriority(self):
        return self.flightPriority
    def getTime(self):
        return self.flightTime
    def getPlaneID(self):
        return self.planeID