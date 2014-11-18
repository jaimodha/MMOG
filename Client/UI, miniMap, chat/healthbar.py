class HealthBar(NodePath): 
        def __init__(self, scale=1, value=1, r=1, g=0, b=0): 
                NodePath.__init__(self, 'healthbar') 

                self.scale = scale #right now the scale goes from 0 to 1: You can change the 
                #scale here
                self.setBillboardAxis()
                cmfg = CardMaker('fg') 
                cmfg.setFrame(- scale,  scale, -0.1 * scale, 0.1 * scale) 
                self.fg = self.attachNewNode(cmfg.generate()) 

              

                self.fg.setColor(r, g, b, 1) 
            
                self.fg.setPos(1.5,0,5.8)
            


                self.setValue(value) 

        def setValue(self, value):
                value = min(max(0, value), 1) 
                self.fg.setScale(value * self.scale, 0, self.scale) 
           
                self.fg.setX((value - 1) * self.scale * self.scale)