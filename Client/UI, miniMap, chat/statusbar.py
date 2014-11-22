from direct.gui.DirectGui import DirectWaitBar
#should be able to change visibility
class StatusBar(DirectWaitBar):
    def __init__(self, barColor=(0,0,255,1), pos=(1.0,0,0.9)): 
        self.bar = DirectWaitBar(pos = pos, barColor = barColor, text="",
        value=70, range=100, frameSize=(-0.3,0.3,0,0.03), frameColor=(255,0,0,1))

    def setValue(self, value):
        self.bar['value'] = float(value)

    def setPos(position):
        self.bar['pos'] = (position)
    
    def setColor(color):
        self.bar['barColor'] = color
