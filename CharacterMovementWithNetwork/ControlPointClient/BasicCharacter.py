RED = 0
BLUE = 1

class BasicCharacter():
        
    def __init__(self, name, factionId):
        self.name = name
        self.factionId = factionId
        self.x = 0
        self.y = 0
        self.z = 0
        
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z