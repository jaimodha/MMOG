from direct.gui.DirectGui import DirectWaitBar
#should be able to change visibility

class ControlPointBar(DirectWaitBar):
    def __init__(self, barColor=(255,0,0,1), pos=(1.0,0,0.9)): 
        self.bar = DirectWaitBar(pos = pos, barColor = barColor, text="",
        value=70, range=100, frameSize=(-0.3,0.3,0,0.03), frameColor=(0,0,255,1))
        

    def setValue(self, value):
        self.bar['value'] = float(value)
        self.setPos((0,0,0))

    def hide(self):
        self.bar.hide()
    
    # to make inherited setPos available for this object
    def show(self):
        self.bar.show()
    
    # to make inherited setPos available for this object
    def setPos(self, pos):
        self.bar.setPos(pos)
       
        
    
class ResourceBar(ControlPointBar):
    def __init__(self, barColor=(200,180,0,1), pos=(0,0,0.9)): 
        self.bar = DirectWaitBar(pos = pos, barColor = barColor, text="",
        value=70, range=100, frameSize=(-0.3,0.3,0,0.03), frameColor=(0,0,0,1))

  