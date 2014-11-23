from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *

import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math

MAP_AX = 127 #minimum X
MAP_BX = 171 #minimum X + maximum X

MAP_AY = 70 #minimum Y
MAP_BY = 117 #minimum Y + maximum Y

MAP_SCALE = 0.35
HERO_SCALE = 0.045

class miniMap(object):
    
    def __init__(self, mainActor):
        
        self.teamMateImage = 'models/hexahedron_blue.png'
        self.heroImage = 'models/mainHero2.png'
        self.miniMapImage = 'models/miniMapImage.png'
        self.towerImage = 'models/tower_neitral.png'
        
        self.map = OnscreenImage(image = self.miniMapImage, pos=(-1, 0, 0.6), 
                              scale=(MAP_SCALE, MAP_SCALE, MAP_SCALE))
        
        self.map.setTransparency(1)

        self.hero = OnscreenImage(image=self.heroImage, pos=(mainActor.getX()/171, 0, mainActor.getY()/117), 
                                    scale=(HERO_SCALE, HERO_SCALE, HERO_SCALE), 
                                    hpr=(0, 0, mainActor.getH()))
        self.hero.reparentTo(self.map)
        self.hero.setTransparency(1)
        
        self.npc = {}
        
        self.tower = {}
        
        self.team = {}
    
    def resizeScreen(self, x, y):
        if x != 800 and y != 600:
            self.map.setPos(-1.5, 0, 0.6)
        else:
            self.map.setPos(-1, 0, 0.7)   
            
        return self.map
                
    def setMap(self, mapScale, x, y):
        self.map = OnscreenImage(image = self.miniMapImage, pos=(x, 0, y), 
                              scale=(mapScale, mapScale, mapScale))
        return self.map
        
    def setHero(self, heroScale, x, y, h):
        self.hero = OnscreenImage(image=self.heroImage, pos=(x, 0, y), 
                                   scale=(heroScale, heroScale, heroScale), 
                                   hpr=(0, 0, h))
        return self.hero
    
    def setNpc(self, npcName, npcImage, npcScale, x, y):
        self.Nps = OnscreenImage(image=npcImage, pos=(x, 0, y), 
                                 scale=(npcScale, npcScale, npcScale))
        self.Nps.reparentTo(self.map)
        self.Nps.setTransparency(1)
        self.npc[npcName] = self.Nps

        return self.npc
        
    def delNpc(self, npcName):
        del self.npc[npcName]
    
    def setTower(self, towerName, towerScale, x, y):
        self.tower_ = OnscreenImage(image=self.towerImage, pos=(x, 0, y), 
                                 scale=(towerScale, towerScale, towerScale))
        self.tower_.reparentTo(self.map)
        self.tower_.setTransparency(1)
        self.tower[towerName] = self.tower_

        return self.tower
    
    def changeTowerColor(self, towerName, towerImage):
        self.tower[towerName].setImage(towerImage)
        
    def delTower(self, towerName):
        del self.tower[towerName]
        
    def setTeamMate(self, mateName, mateScale, getX, getY):
        ay = ((MAP_AY+(getY))*100)/MAP_BY
        y = -1+(ay*2)/100
        ax = ((MAP_AX+(getX))*100)/MAP_BX
        x = -1+(ax*2)/100
        self.teamMate = OnscreenImage(image=self.teamMateImage, 
                                      pos=(x, 0, y), 
                                      scale=(mateScale, mateScale, mateScale))
        self.teamMate.reparentTo(self.map)
        self.teamMate.setTransparency(1)
        self.team[mateName] = self.teamMate
        
        return self.team
    
    def updateTeamMatePos(self, mateName, getX, getY):
        ay = ((MAP_AY+(getY))*100)/MAP_BY
        y = -1+(ay*2)/100
        ax = ((MAP_AX+(getX))*100)/MAP_BX
        x = -1+(ax*2)/100
        self.team[mateName].setPos(x, 0, y) 
     
    def updateTeamMateHpr(self, mateName, getH):
        h = -getH
        self.team[mateName].setHpr(0, 0, h) 
        
    def delTeamMate(self, mateName):
        del self.team[mateName]
        
    def updateHeroPos(self, getX, getY):
        ay = ((MAP_AY+(getY))*100)/MAP_BY
        y = -1+(ay*2)/100
        ax = ((MAP_AX+(getX))*100)/MAP_BX
        x = -1+(ax*2)/100
        self.hero.setPos(x, 0, y) 
        
    def updateHeroHpr(self, getH):
        h = -getH
        self.hero.setHpr(0, 0, h)  
            