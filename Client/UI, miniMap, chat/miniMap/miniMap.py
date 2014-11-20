from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *

import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math


class miniMap(object):
    
    def __init__(self, mainActor):
        
        self.teamMateImage = 'models/teamMate.png'
        self.heroImage = 'models/mainHero.png'
        self.miniMapImage = 'models/miniMapImage.png'
        
        self.map = OnscreenImage(image = self.miniMapImage, pos=(-1, 0, 0.6), 
                              scale=(0.3, 0.3, 0.3))
        
        self.map.setTransparency(1)

        self.hero = OnscreenImage(image=self.heroImage, pos=(mainActor.getX()/200, 0, mainActor.getY()/100), 
                                    scale=(0.045, 0.045, 0.045), 
                                    hpr=(0, 0, mainActor.getH()))
        self.hero.reparentTo(self.map)
        self.hero.setTransparency(1)
        
        self.npc = {}
        
        self.team = {}
                
    def setMap(self, mapScale, x, y):
        map = OnscreenImage(image = self.miniMapImage, pos=(x, 0, y), 
                              scale=(mapScale, mapScale, mapScale))
        return map
        
    def setHero(self, heroScale, x, y, h):
        hero = OnscreenImage(image=self.heroImage, pos=(x, 0, y), 
                                   scale=(heroScale, heroScale, heroScale), 
                                   hpr=(0, 0, h))
        return hero
    
    def setNpc(self, npcName, npcImage, npcScale, x, y):
        self.Nps = OnscreenImage(image=npcImage, pos=(x, 0, y), 
                                 scale=(npcScale, npcScale, npcScale))
        self.Nps.reparentTo(self.map)
        self.Nps.setTransparency(1)
        self.npc[npcName] = self.Nps

        return self.npc
        
    def delNpc(self, npcName):
        del self.npc[npcName]
        
    def setTeamMate(self, mateName, mateScale, getX, getY):
        ay = ((70+(getY))*100)/120
        y = -1+(ay*2)/100
        ax = ((127+(getX))*100)/172
        x = -1+(ax*2)/100
        self.teamMate = OnscreenImage(image=self.teamMateImage, 
                                      pos=(x, 0, y), 
                                      scale=(mateScale, mateScale, mateScale))
        self.teamMate.reparentTo(self.map)
        self.teamMate.setTransparency(1)
        self.team[mateName] = self.teamMate
        
        return self.team
        
    def delTeamMate(self, mateName):
        del self.team[mateName]
        
    def updateHeroPos(self, getX, getY):
        ay = ((70+(getY))*100)/120
        y = -1+(ay*2)/100
        ax = ((127+(getX))*100)/172
        x = -1+(ax*2)/100
        self.hero.setPos(x, 0, y) 
        
    def updateHeroHpr(self, getH):
        h = -getH
        self.hero.setHpr(0, 0, h)
        
    def updateTeamMatePos(self, mateName, getX, getY):
        ay = ((70+(getY))*100)/120
        y = -1+(ay*2)/100
        ax = ((127+(getX))*100)/172
        x = -1+(ax*2)/100
        self.team[mateName].setPos(x, 0, y) 
     
    def updateTeamMateHpr(self, mateName, getH):
        h = -getH
        self.team[mateName].setHpr(0, 0, h)   
    
    def changeTowerColor(self, npcName, toverImage):
        self.npc[npcName].setImage(toverImage)
            