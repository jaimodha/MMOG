from panda3d.core import PandaNode,NodePath,TextNode
from panda3d.core import CardMaker

class HealthBar(NodePath): 
        def __init__(self, scale=1, value=0, r=1, g=0, b=0): 
                NodePath.__init__(self, 'healthbar') 
                self.value = value
                self.scale = scale 
                self.range = 1.0
                self.buff = 0
                cmfg = CardMaker('fg') 
                cmfg.setFrame(- scale,  scale, -0.1 * scale, 0.1 * scale)
                self.fg = self.attachNewNode(cmfg.generate()) 
                self.fg.setBillboardAxis()
                self.fg.setColor(r, g, b, 1)             
                self.fg.setPos(1.5,0,5.8)
                self.setValue(self.value) 
                
                
              

        def setValue(self, value):
                self.value = self.buff*.01 + float(value)/self.range * 0.01 
                self.fg.setX((1-self.value) * self.scale * self.scale)
                self.fg.setScale(self.value * self.scale, 0, self.scale) 
                
        def reparentTo(self, parent):
            self.fg.reparentTo(parent)
        
        def setRange(self, value):
            self.range *= float(value *.01)
        
        # assuming the buff is % of max health. Enter percents as integers
        def addBuff(self, buffPercent):
            self.buff = buffPercent 
            self.setValue(self.value)
          