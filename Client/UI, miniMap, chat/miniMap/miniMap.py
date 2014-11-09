from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *

import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math


class miniMap(object):
    
    map = None
    hero = None
    team = {}
    npc = {}
    
    def __init__(self, mainActor):
        
        self.teamMateImage = 'teamMateImage.png'
        self.heroImage = 'heroImage.png'
        self.miniMapImage = 'miniMapImage.bmp'
        
        self.map = OnscreenImage(image = self.miniMapImage, pos=(1, 0, 0.6), 
                              scale=(0.3, 0.3, 0.3))

        self.hero = OnscreenImage(image=self.heroImage, pos=(mainActor.getX()/200, 0, mainActor.getY()/100), 
                                    scale=(0.025, 0.025, 0.025), 
                                    hpr=(0, 0, mainActor.getH()))
        self.hero.reparentTo(self.map)
        self.hero.setTransparency(1)
    
        if not self.team:
            print 'team is empty'
        else:
            self.team = team
            for i in team:
                i.reparentTo(self.map)
                i.setTransparency(1)
        
        if not self.npc:
            print 'npc is empty'
        else:
            self.npc = npc
            for i in npc:
                i.reparentTo(self.map)
                i.setTransparency(1)
                
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
        self.npc = OnscreenImage(image=npcImage, pos=(x, 0, y), 
                                   scale=(npcScale, npcScale, npcScale))
        npc[npcName] = self.npc
        
    def delNpc(self, npcName):
        del npc[npcName]
        
    def setTeamMate(self, mateName, mateScale, x, y):
        self.teamMate = OnscreenImage(image=self.teamMateImage, pos=(x, 0, y), 
                                   scale=(mateScale, mateScale, mateScale))
        team[mateName] = self.teamMate
        
    def delTeamMate(self, mateName):
        del team[mateName]
        
    def updateHeroPos(self, getX, getY):
        ay = ((70+(getY))*100)/120
        y = -1+(ay*2)/100
        ax = ((127+(getX))*100)/172
        x = -1+(ax*2)/100
        self.hero.setPos(x, 0, y) 
        
    def updateHeroHpr(self, getH):
        h = -getH
        self.hero.setHpr(0, 0, h)
        
        
            