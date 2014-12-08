# Don't display a window
#from panda3d.core import loadPrcFileData
#loadPrcFileData ("", "window-type none")

from direct.directbase.DirectStart import *
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math

from ControlPoint import *

from common.Constants import Constants
from net.ConnectionManager import ConnectionManager
import __builtin__

SPEED = 0.5

class World(DirectObject):

    def __init__(self):
        __builtin__.main = self
        self.taskMgr = taskMgr
        self.base = base
        
        # Connect to the server
        self.cManager = ConnectionManager()
        self.startConnection()
    
        self.characters = dict()
        self.cpList = dict()

        base.win.setClearColor(Vec4(0,0,0,1))
        self.environ = loader.loadModel("models/world")
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.ralphStartPos = self.environ.find("**/start_point").getPos()
        
        # Create a floater object. We use the "floater" as a temporary
        # variable in a variety of calculations.
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)
        
        self.accept("escape", sys.exit)
        
        # Login as 'CPHandler'
        # Temporary workaround, can add a seperate request/response for client/NPC client logins later
        self.username = "CPHandler"
        type = 0
        factionId = 0
        self.cManager.sendRequest(Constants.CMSG_AUTH, [self.username, type, factionId])

        # Create two control points
        cp1 = ControlPoint(1, -107.575, 0.6066, 0.490075, 10, RED)
        cp2 = ControlPoint(2, -100.575, -35.6066, 0.090075, 10, BLUE)

        self.cpList[1] = cp1
        self.cpList[2] = cp2

        taskMgr.doMethodLater(0.1, self.refresh, "heartbeat")
        taskMgr.doMethodLater(1, self.CPHandler, 'CPHandler')
        
         # Set up the camera
        base.disableMouse()
        
        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
        
    def startConnection(self):
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False
        return True
        
    def refresh(self,task):
        self.cManager.sendRequest(Constants.REQ_HEARTBEAT)
        return task.again
        
    def move(self, task):
        return None
        
    def CPHandler(self, task):
        for cp in self.cpList.values():
            if cp.factionId == RED:
                if cp.checkContested(self.characters):
                    print("CP [", cp.id, "] is contested")
                elif cp.checkBluePresence(self.characters):
                    cp.timer -= 1
                    print(cp.id, cp.timer)

                    if cp.timer == 0:
                        print("CP [", cp.id, "] taken by Blue")
                        cp.factionId = BLUE
                else:
                    cp.timer = 30
                    
            elif cp.factionId == BLUE:
                if cp.checkContested(self.characters):
                    print("CP [", cp.id, "] contested")
                elif cp.checkRedPresence(self.characters):
                    cp.timer += 1
                    print(cp.id, cp.timer)

                    if cp.timer == 30:
                        print("CP [", cp.id, "] taken by Red")
                        cp.factionId = RED
                else:
                    cp.timer = 0
            
            # Send 'timer' to server, which send to all clients
            self.cManager.sendRequest(Constants.CMSG_CONTROL_POINT_STATE, [cp.id, cp.timer, cp.factionId])

        return task.again;

w = World()
run()

