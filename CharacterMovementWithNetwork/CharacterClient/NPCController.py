'''
Created on Nov 14, 2014

@author: Akshay
'''

import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import math
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math

from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import ConnectionWriter
from panda3d.core import NetDatagram
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader
from direct.interval.LerpInterval import LerpPosInterval
from direct.interval.LerpInterval import *

from panda3d.ai import *
from libpanda import Point3
#from ControlPoint import ControlPoint
from Npc import Npc
#from RoamingRalphClient import *



class NPCController():

    def __init__(self,render):
        self.threshold = 15
        self.render = render

        '''self.cp1anchorx = 210
        self.cp1anchory = 115
        self.cp1anchorz = 0.0
        
        self.cp2anchorx = 140
        self.cp2anchory = 1
        self.cp2anchorz = 0.0
        
        self.cp3anchorx = 0.0
        self.cp3anchory = 0
        self.cp3anchorz = 0.0
        
        self.cp4anchorx = -150
        self.cp4anchory = 1
        self.cp4anchorz = 0.0
        
        self.cp5anchorx = -210
        self.cp5anchory = 115
        self.cp5anchorz = 0.0'''
        
        self.cp1anchorx = 208.306
        self.cp1anchory = 75.0934
        self.cp1anchorz = -1
        
        self.cp2anchorx = 141.016
        self.cp2anchory = 0.440607
        self.cp2anchorz = -1
        
        self.cp3anchorx = -0.766843
        self.cp3anchory = 9.40588
        self.cp3anchorz = -1
        
        self.cp4anchorx = -210.771
        self.cp4anchory = 113.753
        self.cp4anchorz = -1
        
        self.cp5anchorx = -149.953
        self.cp5anchory = 0.674369
        self.cp5anchorz = -1
        
        cp1team = 0
        cp2team = 0
        cp3team = 0
        cp4team = 1
        cp5team = 1
        
        
        self.npc10 = Npc(1,1,self.cp1anchorx+1, self.cp1anchory+1, self.cp1anchorz,render, cp1team)
        self.npc11 = Npc(1,2,self.cp1anchorx+2, self.cp1anchory+2, self.cp1anchorz,render, cp1team)
        self.npc12 = Npc(1,3,self.cp1anchorx-2, self.cp1anchory+2, self.cp1anchorz,render, cp1team)
        self.npc13 = Npc(1,4,self.cp1anchorx-2, self.cp1anchory-2, self.cp1anchorz,render, cp1team)
        self.npc14 = Npc(1,5,self.cp1anchorx+2, self.cp1anchory-2, self.cp1anchorz,render, cp1team)
        
        self.npc20 = Npc(2,6,self.cp2anchorx+1, self.cp2anchory+1, self.cp2anchorz,render, cp2team)
        self.npc21 = Npc(2,7,self.cp2anchorx+2, self.cp2anchory+2, self.cp2anchorz,render, cp2team)
        self.npc22 = Npc(2,8,self.cp2anchorx-2, self.cp2anchory+2, self.cp2anchorz,render, cp2team)
        self.npc23 = Npc(2,9,self.cp2anchorx-2, self.cp2anchory-2, self.cp2anchorz,render, cp2team)
        self.npc24 = Npc(2,10,self.cp2anchorx+2, self.cp2anchory-2, self.cp2anchorz,render, cp2team)
        
        self.npc30 = Npc(3,11,self.cp3anchorx+1, self.cp3anchory+1, self.cp3anchorz,render, cp3team)
        self.npc31 = Npc(3,12,self.cp3anchorx+2, self.cp3anchory+2, self.cp3anchorz,render, cp3team)
        self.npc32 = Npc(3,13,self.cp3anchorx-2, self.cp3anchory+2, self.cp3anchorz,render, cp3team)
        self.npc33 = Npc(3,14,self.cp3anchorx-2, self.cp3anchory-2, self.cp3anchorz,render, cp3team)
        self.npc34 = Npc(3,15,self.cp3anchorx+2, self.cp3anchory-2, self.cp3anchorz,render, cp3team)
        
        self.npc40 = Npc(4,16,self.cp4anchorx, self.cp4anchory, self.cp4anchorz,render, cp4team)
        self.npc41 = Npc(4,17,self.cp4anchorx+2, self.cp4anchory+2, self.cp4anchorz,render, cp4team)
        self.npc42 = Npc(4,18,self.cp4anchorx-2, self.cp4anchory+2, self.cp4anchorz,render, cp4team)
        self.npc43 = Npc(4,19,self.cp4anchorx-2, self.cp4anchory-2, self.cp4anchorz,render, cp4team)
        self.npc44 = Npc(4,20,self.cp4anchorx+2, self.cp4anchory-2, self.cp4anchorz,render, cp4team)
        
        self.npc50 = Npc(5,21,self.cp5anchorx+1, self.cp5anchory+1, self.cp5anchorz,render, cp5team)
        self.npc51 = Npc(5,22,self.cp5anchorx+2, self.cp5anchory+2, self.cp5anchorz,render, cp5team)
        self.npc52 = Npc(5,23,self.cp5anchorx-2, self.cp5anchory+2, self.cp5anchorz,render, cp5team)
        self.npc53 = Npc(5,24,self.cp5anchorx-2, self.cp5anchory-2, self.cp5anchorz,render, cp5team)
        self.npc54 = Npc(5,25,self.cp5anchorx+2, self.cp5anchory-2, self.cp5anchorz,render, cp5team)
        
        
        self.controlPoint1List = [self.npc10,self.npc11,self.npc12,self.npc13,self.npc14]
        self.controlPoint2List = [self.npc20,self.npc21,self.npc22,self.npc23,self.npc24]
        self.controlPoint3List = [self.npc30,self.npc31,self.npc32,self.npc33,self.npc34]
        self.controlPoint4List = [self.npc40,self.npc41,self.npc42,self.npc43,self.npc44]
        self.controlPoint5List = [self.npc50,self.npc51,self.npc52,self.npc53,self.npc54]
        
        self.controlPointList = [self.controlPoint1List,self.controlPoint2List,self.controlPoint3List,self.controlPoint4List,self.controlPoint5List]
        
        self.AIworld = AIWorld(self.render)
        self.setAI()
        
        
    def setAI(self):        
        #Creating AI World
        #self.AIworld = AIWorld(render)
        for cp in self.controlPointList:
            for npc in cp:
                self.AIworld.addAiChar(npc.AIchar)
                
    def npcTakeDamage(self, health_change,npcId):
        for cp in self.controlPointList:
            for npc in cp:
                if(npc.id == npcId):
                    npc.take_damage(health_change)
                    break
        
                
    def givDistance(self,charachter, id):
        if(id == 1):
            anchorx = self.cp1anchorx 
            anchory = self.cp1anchory
            anchorz = self.cp1anchorz
        elif(id == 2):
            anchorx = self.cp2anchorx
            anchory = self.cp2anchory
            anchorz = self.cp2anchorz
        elif(id == 3):
            anchorx = self.cp3anchorx
            anchory = self.cp3anchory
            anchorz = self.cp3anchorz
        elif(id == 4):
            anchorx = self.cp4anchorx
            anchory = self.cp4anchory
            anchorz = self.cp4anchorz
        elif(id == 5):
            anchorx = self.cp5anchorx
            anchory = self.cp5anchory
            anchorz = self.cp5anchorz
        minDist = math.sqrt( (charachter.getX()-anchorx)*(charachter.getX()-anchorx) + (charachter.getY()-anchory)*(charachter.getY()-anchory) + (charachter.getZ()-anchorz)*(charachter.getZ()-anchorz) )
        return minDist
        
    def isIn(self,charachter,id):
        dist = self.givDistance(charachter,id)
        if(dist<self.threshold):
            return True
        else:
            return False
        
    def cpNpcAlive(self, id):
        count = 0
        for cp in self.controlPointList:
            for npc in cp:
                if(npc.controlPointId==id):
                    if(npc.checkNpcIsAlive()):
                        count +=1
                    else:
                        continue
        
        return count
    
    def allCPNpcStatus(self):
        npcAliveList = []
        for cp in self.controlPointList:
            npcAliveList.append(self.cpNpcAlive(cp[0].controlPointId))
            
        return npcAliveList
            
    '''def getNpc(self,id):
        for cp in self.controlPointList:
            for npc in cp:
                if npc.id == id:
                    return npc'''
    def switchControl(self,cpId):
        for cp in self.controlPointList:
            if(cp[0].controlPointId==cpId):
                for npc in cp:
                    npc.switchTeam()
        
        
    def allBusy(self, cpList): 
        if(cpList[0].isMoving and cpList[1].isMoving and cpList[2].isMoving and cpList[3].isMoving and cpList[4].isMoving):
            return True
        else:
            return False
            
    def nextNotBusy(self, cpList):     
        for npc in cpList:
            if(not npc.isMoving):
                return npc
            
    def checkForAttack(self,currentTime,cManager):
        for cp in self.controlPointList:
            for npc in cp:
                npc.shouldAttack(currentTime,cManager)
                
    def AIUpdate(self,enemyPlayer,currentTime,cManager):
        self.AIworld.update()
        self.checkForAttack(currentTime,cManager)
        npcList = enemyPlayer.npcList
        
        ### LOGIC FOR CHASING 
        for cp in self.controlPointList:
            #cp = self.controlPointList[0]
            #closestRalph = self.findClosestRalph(enemyPlayer.player._character, opponents, cp[0].controlPointId)
            if(not (enemyPlayer.isChased)):
                if(self.isIn(enemyPlayer.player._character,cp[0].controlPointId)):
                    if(not self.allBusy(cp)):
                        availableNpc = self.nextNotBusy(cp)
                        if not enemyPlayer.player._team==availableNpc._team:
                            availableNpc.chaseTarget(enemyPlayer.player._character, True)
                            availableNpc.isMoving = True
                            enemyPlayer.isChased = True
                            npcList = availableNpc.id
                        
        for cp in self.controlPointList:
            if(enemyPlayer.isChased):
                if(not self.isIn(enemyPlayer.player._character,cp[0].controlPointId)):
                    for npc in cp:
                        if(npc.target == enemyPlayer.player._character):
                            #if not npc._is_dead:
                                npc.stopChase()
                                #enemyPlayer.isChased[i] = False
                                #npcList[i] = 0
                                #i = i+1
                                if npc.id == npcList:
                                    enemyPlayer.isChased = False
                                    npcList = 0
        
        return npcList
                   
    def move(self,npcid, target):
        #print " Move Reached"
        for cp in self.controlPointList:
            for npc in cp:
                if(npc.id == npcid):
                    npc.chaseTarget(target)
                    #print " Move Reached 2"
                    break
                
    def stop(self,npcid):
        #print "Reached 1"
        for cp in self.controlPointList:
            for npc in cp:
                if(npc.id == npcid):
                    npc.stopChase()
                    #print "Reached 2"
                    break
                
    def npcStatus(self,npcid):
        for cp in self.controlPointList:
            for npc in cp:
                if(npc.id == npcid):
                    #print npc.isMoving
                    return npc.isMoving
                
    def getNpc(self,npcId):
        for cp in self.controlPointList:
            for npc in cp:
                if(npc.id == npcId):
                    #print npc.isMoving
                    return npc.npc
                        
                    
        
        