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

from direct.interval.IntervalGlobal import Wait
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Parallel
from direct.interval.ActorInterval import ActorInterval
from panda3d.core import Point3

from Character import Character
from Swordsman import Swordsman
from Axeman import Axeman
from Chat import Chat
from miniMap import *
import operator

from main.login import login
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager
import __builtin__


class World(DirectObject):
    def __init__(self):
        
        __builtin__.main = self
        self.cManager = ConnectionManager()
        self.startConnection()
        self.taskMgr = taskMgr
        self.base = base
        
        self.keyMap = {"left":0, "right":0, "forward":0, "backward":0, "cam-left":0, "cam-right":0}
        
        self.characters = dict()
        
        base.win.setClearColor(Vec4(0,0,0,1))
        
        #self.environ = loader.loadModel("models/world")
        self.environ = loader.loadModel("models/land") 
        self.swordLeft = loader.loadModel("models/Sword_Left")
        self.swordRight = loader.loadModel("models/Sword_Right")  
        self.shieldLeft = loader.loadModel("models/Shield_Left")  
        self.shieldRight = loader.loadModel("models/Shield_Right")  
        self.money = loader.loadModel("models/Money")        
        
        self.environ.reparentTo(render)
        self.swordLeft.reparentTo(render)
        self.swordRight.reparentTo(render)
        self.shieldLeft.reparentTo(render)
        self.shieldRight.reparentTo(render)
        self.money.reparentTo(render)
        
        self.environ.setPos(0,0,0)
        self.environ.setH(90)
        self.swordLeft.setH(90)
        self.swordRight.setH(90)
        self.shieldLeft.setH(90)
        self.shieldRight.setH(90)
        self.money.setH(90)
        
        ## swordsmanStartPos = self.environ.find("**/start_point").getPos()
        ## self.player = Swordsman("Swordsman", 0)
        ## self.player._character.reparentTo(render)
        ## self.player._character.setScale(.1)
        ## self.player._character.setPos(swordsmanStartPos)
        ## swordsmanStartPos.setY(swordsmanStartPos.getY()-10)
        ## self.player._character.setPos(swordsmanStartPos.getX(),swordsmanStartPos.getY(),swordsmanStartPos.getZ())
        ## self.initx = swordsmanStartPos.getX()
        
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)
        
        ## self.characters["Axeman"] = Axeman("Axeman", 1)
        ## self.characters["Axeman"]._character.reparentTo(render)
        ## self.characters["Axeman"]._character.setScale(.1)
        ## self.characters["Axeman"]._character.setPos(swordsmanStartPos)
        ## swordsmanStartPos.setY(swordsmanStartPos.getY()-10)
        ## self.characters["Axeman"]._character.setPos(swordsmanStartPos.getX(),swordsmanStartPos.getY() - 10,swordsmanStartPos.getZ())
        ## self.characters["Axeman"]._character.loop("idle")

        self.accept("a", self.setKey, ["left",1])
        self.accept("s", self.setKey, ["backward",1])
        self.accept("w", self.setKey, ["forward",1])
        self.accept("d", self.setKey, ["right",1])
        self.accept("a-up", self.setKey, ["left",0])
        self.accept("s-up", self.setKey, ["backward",0])
        self.accept("w-up", self.setKey, ["forward",0])
        self.accept("d-up", self.setKey, ["right",0])
        self.accept("arrow_left", self.setKey, ["cam-left",1])
        self.accept("arrow_right", self.setKey, ["cam-right",1])
        self.accept("arrow_left-up", self.setKey, ["cam-left",0])
        self.accept("arrow_right-up", self.setKey, ["cam-right",0])
        ## self.accept("mouse1", self.attack, [3])
        ## self.accept("mouse3", self.attack, [4])
        
        ## self.username = str(raw_input("Username: "))
        ## type = input("Type: ")
        ## faction = input("Faction: ")
        ## self.cManager.sendRequest(Constants.CMSG_AUTH, [self.username, type, faction])
        self.login = login()
        
        #taskMgr.add(self.move,"moveTask")
        taskMgr.doMethodLater(.10, self.refresh, "heartbeat")
        
        base.disableMouse()
        #base.camera.setPos(self.player._character.getX(),self.player._character.getY()+10,2)
        
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))

        directionalLight2 = DirectionalLight("directionalLight2")
        directionalLight2.setDirection(Vec3(5, 5, 5))
        directionalLight2.setColor(Vec4(1, 1, 1, 1))
        directionalLight2.setSpecularColor(Vec4(1, 1, 1, 1))

        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(directionalLight2))

        
        
    def startConnection(self):
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False
        return True
        
    def refresh(self,task):
        self.cManager.sendRequest(Constants.REQ_HEARTBEAT)
        return task.again
        
    def setKey(self, key, value):
        self.keyMap[key] = value
        
    def move(self, task):

        main.miniMap.updateHeroPos(self.player._character.getX(), self.player._character.getY())
        main.miniMap.updateHeroHpr(self.player._character.getH())
        main.miniMap.resizeScreen(base.win.getXSize(), base.win.getYSize())

        base.camera.lookAt(self.player._character)
        if (self.keyMap["cam-left"]!=0):
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if (self.keyMap["cam-right"]!=0):
            base.camera.setX(base.camera, +20 * globalClock.getDt())
        
        self.player.move(self.keyMap["forward"], self.keyMap["backward"], self.keyMap["left"], self.keyMap["right"], globalClock.getDt())
            
        if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0) or (self.keyMap["backward"]!=0):
            if self.player._is_moving is False:
                self.player._character.loop("run")
                self.player._is_moving = True
            self.cManager.sendRequest(Constants.CMSG_MOVE, [self.player._character.getX(), self.player._character.getY(), self.player._character.getZ(), self.player._character.getH(), 1])
            #self.characters["Axeman"].moveActor(self.player._character.getX(), self.player._character.getY() - 10, self.player._character.getZ(), self.player._character.getH(), True, globalClock.getDt())
        else:
            if self.player._is_moving:
                #self.player.character.stop()
                self.player._character.loop("idle")
                self.player._is_moving = False
                self.cManager.sendRequest(Constants.CMSG_MOVE, [self.player._character.getX(), self.player._character.getY(), self.player._character.getZ(), self.player._character.getH(), 0])
                #self.characters["Axeman"].moveActor(self.player._character.getX(), self.player._character.getY() - 10, self.player._character.getZ(), self.player._character.getH(), False, globalClock.getDt())
                
        ## camvec = self.player.character.getPos() - base.camera.getPos()
        ## camvec.setZ(0)
        ## camdist = camvec.length()
        ## camvec.normalize()
        ## if (camdist > 10.0):
            ## base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            ## camdist = 10.0
        ## if (camdist < 5.0):
            ## base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            ## camdist = 5.0
        
        base.camera.setPos(self.player._character.getX(),self.player._character.getY()+70,40)
        
        self.floater.setPos(self.player._character.getPos())
        self.floater.setZ(self.player._character.getZ() + 2.0)
        base.camera.lookAt(self.floater)
        
        return task.cont

    
    def attack(self, attack_id):
        self.player._is_attacking = True
        self.cManager.sendRequest(Constants.CMSG_ATTACK, attack_id)
        targets = self.find_target()
        #print targets
        damage=0
        AOE = False
        if attack_id==3:
            damage = self.player.basic_attack()
        elif attack_id==4:
            damage = self.player.special_attack()
            if isinstance(self.player, Axeman):
                AOE=True
        #if targets != None:
        if targets and not AOE:
            self.cManager.sendRequest(Constants.CMSG_HEALTH, [targets[0], damage])
        elif targets and isinstance(self.player, Axeman) and AOE:
            for i in range(len(targets)):
                self.cManager.sendRequest(Constants.CMSG_HEALTH, [targets[i], damage])

    def find_target(self):
        """
        if h==Constants.NORTH:
            pass
        """

        #current player pos and fixed fov
        fov = self.player.FOV
        px = self.player._character.getX()
        py = self.player._character.getY()
        h = self.player._character.getH()
        p_team = self.player.get_team()

        num_of_targets=0
        if isinstance(self.player, Swordsman):
            num_of_targets=1
        elif isinstance(self.player, Axeman):
            num_of_targets=3

        rx=3
        ry=0
        if h==90:
            rx=3
            ry=0
        elif h==135:
            theta = math.pi/4
            rx = (rx*math.cos(theta)) - (ry*math.sin(theta))
            ry = (rx*math.sin(theta)) + (ry*math.cos(theta))
        elif h==180:
            rx=0
            ry=3
        elif h==225:
            theta = (3*math.pi)/4
            rx = (rx*math.cos(theta)) - (ry*math.sin(theta))
            ry = (rx*math.sin(theta)) + (ry*math.cos(theta))
        elif h==270:
            rx=-3
            ry=0
        elif h==315:
            theta = (5*math.pi)/4
            rx = (rx*math.cos(theta)) - (ry*math.sin(theta))
            ry = (rx*math.sin(theta)) + (ry*math.cos(theta))
        elif h==0:
            rx=0
            ry=-3
        elif h==405:
            theta = (7*math.pi)/4
            rx = (rx*math.cos(theta)) - (ry*math.sin(theta))
            ry = (rx*math.sin(theta)) + (ry*math.cos(theta))

        #player view direction based on heading
        cx=rx
        cy=ry

        #find length
        cl = math.sqrt( math.pow(cx, 2) + math.pow(cy, 2) )

        #normalized facing vector
        ncx = cx/cl
        ncy = cy/cl

        targets = []
        candidates={}
        for name, other in self.characters.iteritems():
            tx = other._character.getX()
            ty = other._character.getY()
            
            #direction from player to other player
            vx = tx-px
            vy = ty-py

            vl = math.sqrt( math.pow(vx, 2) + math.pow(vy, 2) )

            if vl==0:
                return None

            #normalize
            nvx = vx/vl
            nvy = vy/vl

            #dot product
            dp = self.dot(ncx, ncy, nvx, nvy)

            angle = math.degrees(math.acos(dp))

            d = self.distance(tx, ty, px, py)

            if angle<(fov/2) and d<self.player.ATK_RANGE:
                if (p_team != other.get_team()) and (not other._is_dead):
                    candidates[name]=d

            if candidates:
                if num_of_targets==1:
                    targets.append(min(candidates, key=candidates.get))
                elif num_of_targets==3:
                    #sorted_candidates=sorted(candidates.items(), key=operator.itemgetter(1))
                    for i in range(0,3):
                        if candidates:
                            min_target=min(candidates, key=candidates.get)
                            del candidates[min_target]
                            targets.append(min_target)

        return targets

    def distance(self, ux, uy, vx, vy):
        dx = math.fabs(ux-vx)
        dy = math.fabs(uy-vy)
        d = math.sqrt( math.pow(dx, 2) + math.pow(dy, 2) )
        return d

    def dot(self, ux, uy, vx, vy):
        return (ux*vx)+(uy*vy)
    
w = World()
run()
