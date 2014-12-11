from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *

import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math

MAP_AX = 270 #minimum X
MAP_BX = 270 #minimum X + maximum X

MAP_AY = 30 #minimum Y
MAP_BY = 30 #minimum Y + maximum Y

MAP_SCALEX = 0.65
MAP_SCALEY = 0.2

HERO_SCALE = 0.035

class miniMap(object):
    
    def __init__(self, mainActor):
        
        self.teamMateImage = 'models/hexahedron_blue.png'
        self.heroImage = 'models/mainHero2.png'
        self.miniMapImage = 'models/miniMap000.png'
        self.towerImage = 'models/tower_neitral.png'
        
        self.map = OnscreenImage(image = self.miniMapImage, pos=(-0.7, 0, 0.8), 
                              scale=(MAP_SCALEX, 0, MAP_SCALEY))
        
        self.map.setTransparency(1)
        #self.map.reparentTo(rander)

        self.hero = OnscreenImage(image=self.heroImage, pos=(mainActor.getX()/525, 0, mainActor.getY()/160), 
                                    scale=(HERO_SCALE, 1, HERO_SCALE), 
                                    hpr=(0, 0, mainActor.getH()))
        self.hero.reparentTo(self.map)
        self.hero.setTransparency(1)
        
        self.npc = {}
        
        self.tower = {}
        
        self.team = {}
    
    def resizeScreen(self, x, y):
        if x != 800 and y != 600:
		self.map.setPos(-1.4, 0, 0.8)
        else:
		self.map.setPos(-0.7, 0, 0.8)
                
    def setMap(self, mapScale, x, y):
        self.map = OnscreenImage(image = self.miniMapImage, pos=(x, 0, y), 
                              scale=(mapScale, mapScale, mapScale))
        return self.map
        
    def setHero(self, heroScale, x, y, h):
        self.hero = OnscreenImage(image=self.heroImage, pos=(x, 0, y), 
                                   scale=(heroScale, 1, heroScale), 
                                   hpr=(0, 0, h))
        return self.hero
    
    def updateHeroPos(self, getX, getY):
        if getX <= 0 and getY <= 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        elif getX > 0 and getY < 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)   
        elif getX < 0 and getY > 0:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        else:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)      
            
        self.hero.setPos(x, 0, y) 
        
    def updateHeroHpr(self, getH):
        h = -getH
        self.hero.setHpr(0, 0, h)  
    
    def setNpc(self, npcName, npcImage, npcScale, x, y):
        self.Nps = OnscreenImage(image=npcImage, pos=(x, 0, y), 
                                 scale=(npcScale*MAP_SCALEY, 1, npcScale*MAP_SCALEX))
        self.Nps.reparentTo(self.map)
        self.Nps.setTransparency(1)
        self.npc[npcName] = self.Nps

        return self.npc
        
    def delNpc(self, npcName):
        del self.npc[npcName]
    
    def setTower(self, towerName, towerScale, getX, getY):
	if getX <= 0 and getY <= 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        elif getX > 0 and getY < 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)   
        elif getX < 0 and getY > 0:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        else:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)

        self.tower_ = OnscreenImage(image=self.towerImage, pos=(x, 0, y), 
                                 scale=(towerScale*MAP_SCALEY, 1, towerScale*MAP_SCALEX))
        self.tower_.reparentTo(self.map)
        self.tower_.setTransparency(1)
        self.tower[towerName] = self.tower_

        return self.tower
    
    def changeTowerColor(self, towerName, towerImage):
        self.tower[towerName].setImage(towerImage)
        
    def delTower(self, towerName):
        del self.tower[towerName]
        
    def setTeamMate(self, mateName, mateScale, getX, getY):
        if getX <= 0 and getY <= 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        elif getX > 0 and getY < 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)   
        elif getX < 0 and getY > 0:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        else:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)
            
        self.teamMate = OnscreenImage(image=self.teamMateImage, 
                                      pos=(x, 0, y), 
                                      scale=(mateScale*MAP_SCALEY, 1, mateScale*MAP_SCALEX))
        self.teamMate.reparentTo(self.map)
        self.teamMate.setTransparency(1)
        self.team[mateName] = self.teamMate
        
        return self.team
    
    def updateTeamMatePos(self, mateName, getX, getY):
        if getX <= 0 and getY <= 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        elif getX > 0 and getY < 0:
            ay = (MAP_AY + (getY))/MAP_AY
            y = MAP_SCALEY-(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)   
        elif getX < 0 and getY > 0:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_AX + (getX))/MAP_AX
            x = MAP_SCALEX-(ax*MAP_SCALEX)
        else:
            ay = (MAP_BY - (getY))/MAP_BY
            y = -MAP_SCALEY+(ay*MAP_SCALEY)
            ax = (MAP_BX - (getX))/MAP_BX
            x = -MAP_SCALEX+(ax*MAP_SCALEX)
            
        self.team[mateName].setPos(x, 0, y) 
     
    def updateTeamMateHpr(self, mateName, getH):
        h = -getH
        self.team[mateName].setHpr(0, 0, h) 
        
    def delTeamMate(self, mateName):
        del self.team[mateName]
        
            
