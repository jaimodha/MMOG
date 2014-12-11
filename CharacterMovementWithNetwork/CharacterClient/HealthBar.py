from panda3d.core import PandaNode,NodePath,TextNode
from panda3d.core import CardMaker, DecalEffect

class HealthBar(NodePath): 
        def __init__(self, scale=1, value=0, r=0, g=10, b=0): 
                NodePath.__init__(self, 'healthbar') 
                
                self.value = value
                self.scale = scale 
                self.range = 1.0
                self.buff = 0
                self.x = 0
                self.y = 0
                self.z = 5
                              
                cmbg = CardMaker('bg') 
                cmbg.setFrame(- scale, scale, -0.1 * scale, 0.1 * scale)
                self.bg = self.attachNewNode(cmbg.generate())
 
                self.bg.setColor(0.8, 0.2, 0.4, 1)
                self.bg.setPos(self.x, self.y, self.z)  
                
                
                cmfg = CardMaker('fg') 
                cmfg.setFrame(- scale, scale, -0.1 * scale, 0.1 * scale)
                self.fg = self.bg.attachNewNode(cmfg.generate()) 
               
                self.fg.setColor(r, g, b, 1) 
                self.fg.setPos(0,0,0)
                self.fg.setBillboardPointWorld()
                self.bg.setBillboardPointWorld()
                
                self.fg.clearShader()
                self.bg.clearShader() 
                
                self.fg.setScale(self.scale, 0, self.scale)
                self.bg.setScale(self.scale, 0, self.scale)
                self.bg.setEffect(DecalEffect.make())
                               
                self.setValue(0)
                

        def setValue(self, value):
                self.value = min((self.buff*.01 + float(value)/self.range * 0.01), 1)
                self.fg.setScale(self.value, 0, 1)
                self.fg.setX((self.value - 1) * self.scale)
                
          

                
        def reparentTo(self, parent):
            self.bg.reparentTo(parent)
            self.fg.reparentTo(self.bg)
            
        
        def setRange(self, value):
            self.range *= float(value *.01)
        
        # assuming the buff is % of max health. Enter percents as integers
        def addBuff(self, buffPercent):
            self.buff = buffPercent 
            self.setValue(self.value)
            
        def setPos(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
          