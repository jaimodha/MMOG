from direct.gui.DirectGui import DirectWaitBar
#should be able to change visibility
class ControlPointBar(DirectWaitBar):
    def __init__(self, barColor=(255,0,0,1), pos=(base.a2dRight, 0, base.a2dTop)): 
        self.bar = DirectWaitBar(pos = pos, barColor = barColor, text="",sdfkjWDHFGP'NWELKB; 
        value=70, range=30, frameSize=(-0.3,0.3,0,0.03), frameColor=(0,0,255,1))

    def setValue(self, value):
        self.bar['value'] = float(value)

    def hide(self):
        self.bar.hide()
    
    def show(self):
        self.bar.show()
    
    def setPos(pos):
        self.bar['pos'] = pos
        
    
class ResourceBar(DirectWaitBar):
    def __init__(self, barColor=(200,180,0,1), pos=(0,0,0.9)): 
        self.bar = DirectWaitBar(pos = pos, barColor = barColor, text="",
        value=70, range=30, frameSize=(-0.3,0.3,0,0.03), frameColor=(0,0,0,1))

    def setValue(self, value):
        self.bar['value'] = float(value)

    def hide(self):
        self.bar.hide()
    
    def show(self):
        self.bar.show()
        