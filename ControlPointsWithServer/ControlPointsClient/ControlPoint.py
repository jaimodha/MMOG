from Character import *
import math

class ControlPoint():

    def __init__(self, id, x, y, z, radius, factionId):
        # TODO: Make id autoincrement
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.factionId = factionId

        self.model = loader.loadModel("models/circle")
        self.model.setTransparency(True)
        self.model.reparentTo(render)
        self.model.setAlphaScale(0.5)
        self.model.setScale(3)
        self.model.setPos(x, y, z)


        if factionId == RED:
            self.timer = 0
            self.model.setColor(255,0,0)
        else:
            self.timer = 30
            self.model.setColor(0,0,255)
            
    def setTimer(self, timer):
        self.timer = timer
        
    def setFactionId(self, factionId):
        self.factionId = factionId

    ## this method takes in a character and checks if it exists within the given radius of the control point
    def withinCircle(self, character):
        dist = math.sqrt((character.getX() - self.x)**2 + (character.getY() - self.y)**2)
        return dist <= self.radius

    ## check for red characters in the control point
    def checkRedPresence(self, characters):
        for x in characters.values():
            if self.withinCircle(x.actor) and x.factionId == RED:
                return True
        return False

    ## check for blue characters in the control point
    def checkBluePresence(self, characters):
        for x in characters.values():
            if self.withinCircle(x.actor) and x.factionId == BLUE:
                return True
        return False

    ## checks to see if red and blue players are within the control point
    def checkContested(self, characters):
            return self.checkRedPresence(characters) and self.checkBluePresence(characters)
