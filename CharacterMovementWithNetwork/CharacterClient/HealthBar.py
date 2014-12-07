from panda3d.core import PandaNode,NodePath,TextNode
from panda3d.core import CardMaker

class HealthBar(NodePath): 
        def __init__(self, scale=1, value=0, r=10, g=0, b=0): 
                NodePath.__init__(self, 'healthbar') 
                self.value = value
                self.scale = scale 
                self.range = 1.0
                self.buff = 0
                
                
                
                cmbg = CardMaker('bg') 
                cmbg.setFrame(- scale, scale, -0.1 * scale, 0.1 * scale)
                self.bg = self.attachNewNode(cmbg.generate())
 
                self.bg.setColor(0.2, 0.2, 0.2, 1)
                self.bg.setPos(0,0,7.1)
                
                
                cmfg = CardMaker('fg') 
                cmfg.setFrame(- scale,  scale, -0.1 * scale, 0.1 * scale)
                self.fg = self.bg.attachNewNode(cmfg.generate()) 
               
                self.fg.setColor(r, g, b, 1) 
                self.fg.setPos(0,-0.1,0)
                self.fg.setBillboardPointWorld()
                self.bg.setBillboardPointWorld()
                
                self.fg.clearShader()
                self.bg.clearShader()
       

                self.setValue(0)
              

        def setValue(self, value):
                self.value = self.buff*.01 + float(value)/self.range * 0.01 
                self.fg.setScale(self.value * self.scale, 0, self.scale) 
                self.fg.setX((self.value - 1) * self.scale * self.scale)

                
        def reparentTo(self, parent):
            self.bg.reparentTo(parent)
            self.fg.reparentTo(self.bg)
            
        
        def setRange(self, value):
            self.range *= float(value *.01)
        
        # assuming the buff is % of max health. Enter percents as integers
        def addBuff(self, buffPercent):
            self.buff = buffPercent 
            self.setValue(self.value)
          