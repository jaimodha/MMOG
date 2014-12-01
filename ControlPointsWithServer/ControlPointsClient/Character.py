RED = 0
BLUE = 1

class Character():
        
    def __init__(self, name, actor, factionId):
        self.name = name
        self.actor = actor
        self.factionId = factionId
        
    def __str__(self):
        if self.factionId == RED:
            return "I'm a red ralph"
        elif self.factionId == BLUE:
            return "I'm a blue ralph"
        else:
            return "What am I?"
