from BasicCharacter import *
import math

class BasicControlPoint():

    def __init__(self, id, x, y, z, radius, factionId):
        # TODO: Make id autoincrement
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.factionId = factionId
        
        if factionId == RED:
            self.timer = 0
        else:
            self.timer = 30
            
    def setTimer(self, timer):
        self.timer = timer
        
    def setFactionId(self, factionId):
        self.factionId = factionId

    ## this method takes in a character and checks if it exists within the given radius of the control point
    def withinCircle(self, character):
        dist = math.sqrt((character.x - self.x)**2 + (character.y - self.y)**2)
        return dist <= self.radius

    ## check for red characters in the control point
    def checkRedPresence(self, characters):
        for x in characters.values():
            if self.withinCircle(x) and x.factionId  == RED:
                return True
        return False

    ## check for blue characters in the control point
    def checkBluePresence(self, characters):
        for x in characters.values():
            if self.withinCircle(x) and x.factionId  == BLUE:
                return True
        return False

    ## checks to see if red and blue players are within the control point
    def checkContested(self, characters):
            return self.checkRedPresence(characters) and self.checkBluePresence(characters)
