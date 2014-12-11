'''
Created on Nov 14, 2014

@author: Akshay
'''
#from npc import ControlPoint
from direct.actor.Actor import Actor
from panda3d.ai import *
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from direct.interval.LerpInterval import LerpPosInterval
from direct.interval.LerpInterval import *
#from libpanda import Point3
from panda3d.core import Point3
from direct.interval.ActorInterval import ActorInterval
import math
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d.core import ConnectionWriter
from panda3d.core import NetDatagram
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader
from direct.interval.FunctionInterval import Wait
from direct.interval.IntervalGlobal import Sequence
from common.Constants import Constants
from HealthBar import HealthBar
from panda3d.core import PandaNode,NodePath,TextNode


class Npc():

    def __init__(self,controlPointId,id, anchorx, anchory, anchorz,render,team):
        self.id = id
        self.anchorx = anchorx
        self.anchory = anchory
        self.anchorz = anchorz
        self.controlPointId = controlPointId
        self.target = None
        self.isMoving = False
        self.health = 200
        self.isCurrentUser = False
        self.damage = 8
        self.attackTimer = 0
        self._is_dead = False
        self._team = team
        
        self.render = render
        '''Initializing NPC actors'''
        self.npc = Actor("models/priest",
                                {"walk": "models/priest-walk", "attack":"models/priest-attack", "hurt":"models/priest-hit", "die":"models/priest-die"})
        if self._team==0:
            self.npcTex = loader.loadTexture("models/tex/guard_red.png")
        else:
            self.npcTex = loader.loadTexture("models/tex/guard_blue.png")
        self.npc.setTexture(self.npcTex)
        self.npc.setScale(0.5, 0.5, 0.5)
        self.npc.clearColor()
        self.npc.clearColorScale()
        self.npc.setColor(255, 0, 0, 0)
        self.npc.setColorScale(255, 0, 0, 0)
        self.npc.reparentTo(self.render)
        self.npc.setPos(anchorx,anchory,anchorz)
        
        self.AIchar = AICharacter("npc",self.npc, 100, 0.05, 5)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        
        self.hb = HealthBar(1.5, value=self.health)
        #self._floater = NodePath(PandaNode("char_info"))
        #self._floater.reparentTo(self.npc)
        self.hb.setPos(0, 0, 11.9)
        self.hb.reparentTo(self.npc)
        #self.hb.reparentTo(self.npc)
        
    def renderBlue(self):
        if not self._is_dead:
            self.AIbehaviors.removeAi("pursue")
            self.npc.detachNode()
        self.npc = Actor("models/priest",
                                {"walk": "models/priest-walk", "attack":"models/priest-attack", "hurt":"models/priest-hit", "die":"models/priest-die"})
        
        self.npcTex = loader.loadTexture("models/tex/guard_blue.png")
        self.npc.setTexture(self.npcTex)
        self.npc.setScale(0.5, 0.5, 0.5)
        self.npc.clearColor()
        self.npc.clearColorScale()
        self.npc.setColor(255, 0, 0, 0)
        self.npc.setColorScale(255, 0, 0, 0)
        self.npc.reparentTo(self.render)
        self.npc.setPos(self.anchorx,self.anchory,self.anchorz)
        
        self.AIchar = AICharacter("npc",self.npc, 100, 0.05, 5)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        
        self.hb = HealthBar(1.5, value=self.health)
        self.hb.setPos(0, 0, 8.1)
        self.hb.reparentTo(self.npc)
        #self.hb.reparentTo(self.npc)
        
    def renderRed(self):
        if not self._is_dead:
            self.AIbehaviors.removeAi("pursue")
            self.npc.detachNode()
        self.npc = Actor("models/priest",
                                {"walk": "models/priest-walk", "attack":"models/priest-attack", "hurt":"models/priest-hit", "die":"models/priest-die"})
        
        self.npcTex = loader.loadTexture("models/tex/guard_red.png")
        self.npc.setTexture(self.npcTex)
        self.npc.setScale(0.5, 0.5, 0.5)
        self.npc.clearColor()
        self.npc.clearColorScale()
        self.npc.setColor(255, 0, 0, 0)
        self.npc.setColorScale(255, 0, 0, 0)
        self.npc.reparentTo(self.render)
        self.npc.setPos(self.anchorx,self.anchory,self.anchorz)
        
        self.AIchar = AICharacter("npc",self.npc, 100, 0.05, 5)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        
        self.hb = HealthBar(1.5, value=self.health)
        self.hb.setPos(0, 0, 8.1)
        self.hb.reparentTo(self.npc)
        
    def switchTeam(self):
        if self._team==0:
            self._team=1
            self.renderBlue()
        else:
            self._team=0
            self.renderRed()
            
        self.target = None
        self.isMoving = False
        self.health = 200
        self.isCurrentUser = False
        self.damage = 8
        self.attackTimer = 0
        self._is_dead = False
            
        
    def set_health(self, health):
        self.health = health
        
    def take_damage(self, health_change):
        health = self.health
        if health <= health_change and not self._is_dead:
            self.killNpc()
        else:
            health = health-health_change
            self.set_health(health)
            self.hb.setValue(self.health)
            self.npc.play("hurt")
            
    def killNpc(self):
        self.set_health(0)
        self.hb.setValue(0)
        self.AIbehaviors.removeAi("pursue")
        hurt_interval = self.npc.actorInterval("hurt")
        death_interval = self.npc.actorInterval("die")
        seq = Sequence(hurt_interval, death_interval)
        seq.start()
        self.npc.pose("die",45)
        self._is_dead = True
        self.npc.detachNode()
        if self.isCurrentUser:
            main.freeDeadNpc(self.id)
            #main.cManager.sendRequest(Constants.CMSG_NPCDEATH, [self.id])
            print Constants.CMSG_NPCDEATH,
            print " + ",
            print self.id
            
            
    def chaseTarget(self, target, status = False):
        if(not self.isMoving):
            self.target = target
            self.AIbehaviors.remove_ai("all")
            self.AIbehaviors.pursue(self.target)
            self.npc.loop("walk")
            self.isMoving = True
            self.isCurrentUser = status
            
    def stopChase(self):
        
        #self.AIbehaviors.pauseAi("pursue")
        if not self._is_dead:
            self.AIbehaviors.removeAi("pursue")
            p1 = LerpHprInterval(self.npc, 4, Point3(180,0,0))
            p2 = LerpPosInterval(self.npc, 4, Point3(self.anchorx, self.anchory, self.anchorz))
            animInterval = self.npc.actorInterval("walk", loop = 1, duration=4)
            p2.start()
            p1.start()
            animInterval.start()
            self.isMoving = False
            self.target = None
            self.isCurrentUser = False
        
    def givNPCDistance(self,charachter):
        x = self.npc.getX()
        y = self.npc.getY()
        z = self.npc.getZ()
        minDist = math.sqrt( (charachter.getX()-x)*(charachter.getX()-x) + (charachter.getY()-y)*(charachter.getY()-y) + (charachter.getZ()-z)*(charachter.getZ()-z) )
        return minDist
    
    def checkNpcIsAlive(self):
        if(self.health>0):
            return True
        else:
            return False
                         
    def shouldAttack(self,currentTime,cManager):
        if not self._is_dead:
            if self.isMoving:
                if self.attackTimer>0:
                    self.attackTimer = self.attackTimer-currentTime
                    #print self.attackTimer
                if self.AIbehaviors.behaviorStatus("pursue")=="done":
                    #self.npc.stop("walk")
                    #print self.npc.getAnimControl("walk")
                    if self.attackTimer<=0:
                            if self.npc.getAnimControl("walk").isPlaying():
                                self.npc.stop("walk")
                            if not self.npc.getAnimControl("attack").isPlaying():
                                #self.npc.loop("attack")
                                self.npc.play("attack")
                                self.attackTimer = 2
                                #myInterval = self.npc.actorInterval("attack")
                                #seq = Sequence(myInterval)
                                #seq.append(Wait(3))
                                #seq.start()
                            if self.isCurrentUser:
                                cManager.sendRequest(Constants.CMSG_NPCATTACK, [self.id, self.damage])
                
                if self.AIbehaviors.behaviorStatus("pursue")=="active":
                    if self.npc.getAnimControl("attack").isPlaying():
                        self.npc.stop("attack")
                    if not self.npc.getAnimControl("walk").isPlaying():
                        self.npc.loop("walk") 