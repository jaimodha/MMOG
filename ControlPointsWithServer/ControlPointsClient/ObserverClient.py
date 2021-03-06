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

from statusbar import *
from ControlPoint import *

from common.Constants import Constants
from net.ConnectionManager import ConnectionManager
import __builtin__

SPEED = 0.5

# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)

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

        self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        base.win.setClearColor(Vec4(0,0,0,1))

        # Post the instructions

        self.title = addTitle("Panda3D Tutorial: Roaming Ralph (Walking on Uneven Terrain)")
        self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        self.inst2 = addInstructions(0.90, "[Left Arrow]: Rotate Ralph Left")
        self.inst3 = addInstructions(0.85, "[Right Arrow]: Rotate Ralph Right")
        self.inst4 = addInstructions(0.80, "[Up Arrow]: Run Ralph Forward")
        self.inst6 = addInstructions(0.70, "[A]: Rotate Camera Left")
        self.inst7 = addInstructions(0.65, "[S]: Rotate Camera Right")

        # Set up the environment
        #
        # This environment model contains collision meshes.  If you look
        # in the egg file, you will see the following:
        #
        #    <Collide> { Polyset keep descend }
        #
        # This tag causes the following mesh to be converted to a collision
        # mesh -- a mesh which is optimized for collision, not rendering.
        # It also keeps the original mesh, so there are now two copies ---
        # one optimized for rendering, one for collisions.

        self.environ = loader.loadModel("models/world")
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.ralphStartPos = self.environ.find("**/start_point").getPos()

        # Create a floater object.  We use the "floater" as a temporary
        # variable in a variety of calculations.

        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

        # Accept the control keys for movement and rotation

        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left",1])
        self.accept("arrow_right", self.setKey, ["right",1])
        self.accept("arrow_up", self.setKey, ["forward",1])
        self.accept("a", self.setKey, ["cam-left",1])
        self.accept("s", self.setKey, ["cam-right",1])
        self.accept("arrow_left-up", self.setKey, ["left",0])
        self.accept("arrow_right-up", self.setKey, ["right",0])
        self.accept("arrow_up-up", self.setKey, ["forward",0])
        self.accept("a-up", self.setKey, ["cam-left",0])
        self.accept("s-up", self.setKey, ["cam-right",0])
        
        # Placeholder Login
        self.name = str(raw_input("Name: "))
        factionId = int(input("Faction ID: "))
        self.cManager.sendRequest(Constants.CMSG_AUTH, [self.name, factionId])

        # Create two control points
        cp1 = ControlPoint(1, -107.575, 0.6066, 0.490075, 10, RED)
        cp2 = ControlPoint(2, -100.575, -35.6066, 0.090075, 10, BLUE)

        self.cpList[1] = cp1
        self.cpList[2] = cp2
        
        # Create the control point Bar UI
        self.cp_bar = ControlPointBar()
        self.resource_bar = ResourceBar()

        taskMgr.doMethodLater(0.1, self.refresh, "heartbeat")
        taskMgr.doMethodLater(1, self.CPHandler, "CPHandler")
        taskMgr.doMethodLater(0.1, self.CPBarHandler, 'CPBarHandler')

        # Game state variables
        self.isMoving = False

        # Set up the camera
        base.disableMouse()
        #base.camera.setPos(self.character.actor.getX(),self.character.actor.getY()+10,2)

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

    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value


    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):

        # Set the control point circle's height to Ralph's
        #for cp in self.cpList:
         #   cp.model.setZ(self.character.actor.getZ() + 0.1)

        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.

        base.camera.lookAt(self.character.actor)
        if (self.keyMap["cam-left"]!=0):
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if (self.keyMap["cam-right"]!=0):
            base.camera.setX(base.camera, +20 * globalClock.getDt())

        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.

        startpos = self.character.actor.getPos()

        # If a move-key is pressed, move ralph in the specified direction.

        if (self.keyMap["left"]!=0):
            self.character.actor.setH(self.character.actor.getH() + 300 * globalClock.getDt())
        if (self.keyMap["right"]!=0):
            self.character.actor.setH(self.character.actor.getH() - 300 * globalClock.getDt())
        if (self.keyMap["forward"]!=0):
            self.character.actor.setY(self.character.actor, -25 * globalClock.getDt())

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.

        if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0):
            if self.isMoving is False:
                self.character.actor.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.character.actor.stop()
                self.character.actor.pose("walk",5)
                self.isMoving = False
        self.cManager.sendRequest(Constants.CMSG_MOVE, [self.character.actor.getX(), self.character.actor.getY(), self.character.actor.getZ(), self.character.actor.getH()])

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.

        camvec = self.character.actor.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0

        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.

        self.floater.setPos(self.character.actor.getPos())
        self.floater.setZ(self.character.actor.getZ() + 2.0)
        base.camera.lookAt(self.floater)

        return task.cont
    
    
    # Used for checking whether to show the control point capture bar
    def inWhichControlPoint(self):
        for cp in self.cpList.values():
            if cp.withinCircle(self.character.actor):
                return cp
        return None
    
    def CPBarHandler(self, task):
        # This is where you check to see if you are in a control point 
        # to render the bar or not
        
        currentCP = self.inWhichControlPoint()

        if currentCP is not None:
            self.cp_bar.show()
            self.cp_bar.setValue(currentCP.timer)
        else:
            self.cp_bar.hide()
        
        return task.again
        
    def CPHandler(self, task):
        # Change colors of control points to match their faction
        for cp in self.cpList.values():
            if cp.timer == 0:
                cp.model.setColor(0,0,255)
            if cp.timer == 30:
                cp.model.setColor(255,0,0)

        return task.again;

w = World()
run()

