from panda3d.core import PandaNode,NodePath,TextNode
from panda3d.core import CardMaker

class HealthBar(NodePath): 
        def __init__(self, scale=1, value=1, r=1, g=0, b=0): 
                NodePath.__init__(self, 'healthbar') 

                self.scale = scale #right now the scale goes from 0 to 1: You can change the 
                #scale here

                cmfg = CardMaker('fg') 
                cmfg.setFrame(- scale,  scale, -0.1 * scale, 0.1 * scale)
                self.fg = self.attachNewNode(cmfg.generate()) 
                self.fg.setBillboardAxis()
                self.fg.setColor(r, g, b, 1)             
                self.fg.setPos(1.5,0,7.5)
                self.setValue(value) 

        def setValue(self, value):
                value = float(value) * 0.01
                self.fg.setX((1-value) * self.scale * self.scale)
                self.fg.setScale(value * self.scale, 0, self.scale) 
                
        def reparentTo(self, parent):
            self.fg.reparentTo(parent)