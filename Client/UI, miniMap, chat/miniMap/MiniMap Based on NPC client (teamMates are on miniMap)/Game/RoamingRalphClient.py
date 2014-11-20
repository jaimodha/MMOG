# Author: Ryan Myers
# Models: Jeff Styers, Reagan Heller


# Last Updated: 6/13/2005
#
# This tutorial provides an example of creating a character
# and having it walk around on uneven terrain, as well
# as implementing a fully rotatable camera.

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

from miniMap import *

from panda3d.ai import *
 
SPEED = 0.5
CHASE_DISTANCE = 15
 
# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)
 
# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)
 
# A simple function to make sure a value is in a given range
def restrain(i, mn, mx): 
    return i == min(max(i, mn), mx)

class Player():
 def __init__(self):
  self.id = 0
  self.username = ""
  self.character = Actor("models/ralph",{"run":"models/ralph-run","walk":"models/ralph-walk"})
        
class World(DirectObject):
 
    def __init__(self):
         
        self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        
        self.cManager = QueuedConnectionManager()
        self.cListener = QueuedConnectionListener(self.cManager, 0)
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager, 0)
        
        self.opponents = dict()
        self.logStat = -1
        self.id = 0
        self.username = ""
        
        host = "localhost"
        port = 9252
        self.connection = self.cManager.openTCPClientConnection(host, port, 10000)
        
        self.received = 1
        
        self.playersText = []
        
        if self.connection:
         self.cReader.addConnection(self.connection)
         taskMgr.add(self.updateRoutine, 'updateRoutine')
         taskMgr.add(self.login, 'login')
         taskMgr.doMethodLater(.1, self.heartbeat, 'heartbeat')
         
        # Replace with actual, dynamic list of players from the server
        self.players = dict()
         
        # Placeholder, replace with actual # of players later
        self.numberOfPlayers = 2
         
        # Stores the OnScreenText for each player in the players list
        # Populated and depopulated using listPlayers and delistPlayers
        self.playersText = []
         
        # Stores all the player objects currently logged in
        self.playerObjects = []
         
        base.win.setClearColor(Vec4(0,0,0,1))
 
        # Post the instructions
 
        #self.title = addTitle("Panda3D Tutorial: Roaming Ralph (Walking on Uneven Terrain)")
        #self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        #self.inst2 = addInstructions(0.90, "[Left Arrow]: Rotate Ralph Left")
        #self.inst3 = addInstructions(0.85, "[Right Arrow]: Rotate Ralph Right")
        #self.inst4 = addInstructions(0.80, "[Up Arrow]: Run Ralph Forward")
        #self.inst6 = addInstructions(0.70, "[A]: Rotate Camera Left")
        #self.inst7 = addInstructions(0.65, "[S]: Rotate Camera Right")
        #self.inst8 = addInstructions(0.60, "[Q]: Display List Of Connected Players")
         
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
         
         
         
         
         
        # Create the main character, Ralph
 
        ralphStartPos = self.environ.find("**/start_point").getPos()
        self.ralph = Actor("models/ralph",
                                 {"run":"models/ralph-run",
                                  "walk":"models/ralph-walk"})
        self.ralph.reparentTo(render)
        self.ralph.setScale(.2)
        self.ralph.setPos(ralphStartPos)
        ralphStartPos.setY(ralphStartPos.getY()-10)
        self.ralph.setPos(ralphStartPos.getX(),ralphStartPos.getY(),ralphStartPos.getZ())
        self.initx = ralphStartPos.getX()
         
        # Add our Ralph to list to Ralphs
        self.playerObjects.append(self.ralph)
         
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.003, 0.003, 0.003)
        self.pandaActor.reparentTo(render)
        # Loop its animation.
        #self.pandaActor.loop("walk")
        self.pandaActor.setPos(ralphStartPos.getX(),ralphStartPos.getY()-20,ralphStartPos.getZ())
         
        # Create a floater object.  We use the "floater" as a temporary
        # variable in a variety of calculations.
         
        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)
 
        # Accept the control keys for movement and rotation
 
        self.accept("escape", self.disconnect)
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
        self.accept("q", self.listPlayers)
        self.accept("q-up", self.delistPlayers)
 
        taskMgr.add(self.move,"moveTask")
         
        # Call whenever a ralph has logged in, use arg "out" for logouts
        self.displayLoginText()
 
        # Game state variables
        self.isMoving = False
 
        # Set up the camera
         
        base.disableMouse()
        base.camera.setPos(self.ralph.getX(),self.ralph.getY()+10,2)
         
        # We will detect the height of the terrain by creating a collision
        # ray and casting it downward toward the terrain.  One ray will
        # start above ralph's head, and the other will start above the camera.
        # A ray may hit the terrain, or it may hit a rock or a tree.  If it
        # hits the terrain, we can detect the height.  If it hits anything
        # else, we rule that the move is illegal.
 
        self.cTrav = CollisionTraverser()
 
        self.ralphGroundRay = CollisionRay()
        self.ralphGroundRay.setOrigin(0,0,1000)
        self.ralphGroundRay.setDirection(0,0,-1)
        self.ralphGroundCol = CollisionNode('ralphRay')
        self.ralphGroundCol.addSolid(self.ralphGroundRay)
        self.ralphGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.ralphGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.ralphGroundColNp = self.ralph.attachNewNode(self.ralphGroundCol)
        self.ralphGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.ralphGroundColNp, self.ralphGroundHandler)
         
        self.pandaActorGroundRay = CollisionRay()
        self.pandaActorGroundRay.setOrigin(0,0,1000)
        self.pandaActorGroundRay.setDirection(0,0,-1)
        self.pandaActorGroundCol = CollisionNode('pandaActorRay')
        self.pandaActorGroundCol.addSolid(self.pandaActorGroundRay)
        self.pandaActorGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.pandaActorGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.pandaActorGroundColNp = self.pandaActor.attachNewNode(self.pandaActorGroundCol)
        self.pandaActorGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.pandaActorGroundColNp, self.pandaActorGroundHandler)
         
 
        self.camGroundRay = CollisionRay()
        self.camGroundRay.setOrigin(0,0,1000)
        self.camGroundRay.setDirection(0,0,-1)
        self.camGroundCol = CollisionNode('camRay')
        self.camGroundCol.addSolid(self.camGroundRay)
        self.camGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.camGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.camGroundColNp = base.camera.attachNewNode(self.camGroundCol)
        self.camGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.camGroundColNp, self.camGroundHandler)
 
        # Uncomment this line to see the collision rays
        #self.ralphGroundColNp.show()
        #self.camGroundColNp.show()
        
        self.miniMap = miniMap(self.ralph)
        self.miniMap.setNpc('tower_1', 'models/hexahedron.png', 0.05, 0.2, 0.3)
        self.miniMap.setNpc('tower_2', 'models/hexahedron.png', 0.05, -0.4, -0.5)
        
        # Uncomment this line to show a visual representation of the 
        # collisions occuring
        #self.cTrav.showCollisions(render)
         
        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
 
        self.setAI()
     
    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value
     
 
    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):
        
        self.miniMap.updateHeroPos(self.ralph.getX(), self.ralph.getY())
        self.miniMap.updateHeroHpr(self.ralph.getH())
        
        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.
 
        base.camera.lookAt(self.ralph)
        if (self.keyMap["cam-left"]!=0):
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if (self.keyMap["cam-right"]!=0):
            base.camera.setX(base.camera, +20 * globalClock.getDt())
 
        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.
 
        startpos = self.ralph.getPos()
 
        # If a move-key is pressed, move ralph in the specified direction.
 
        if (self.keyMap["left"]!=0):
            self.ralph.setH(self.ralph.getH() + 300 * globalClock.getDt())
        if (self.keyMap["right"]!=0):
            self.ralph.setH(self.ralph.getH() - 300 * globalClock.getDt())
        if (self.keyMap["forward"]!=0):
            self.ralph.setY(self.ralph, -25 * globalClock.getDt())
 
        # Makes the panda look at ralph when not using AI
        #self.pandaActor.lookAt(self.ralph)
        #self.pandaActor.setH(self.pandaActor.getH() + 180)
         
        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.
 
        if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0):
            if self.isMoving is False:
                self.ralph.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.ralph.stop()
                self.ralph.pose("walk",5)
                self.isMoving = False
                print "stop"
                self.requestStop()
         
        
 
 
        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.
 
        camvec = self.ralph.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0
 
        # Now check for collisions.
 
        self.cTrav.traverse(render)
 
        # Adjust ralph's Z coordinate.  If ralph's ray hit terrain,
        # update his Z. If it hit anything else, or didn't hit anything, put
        # him back where he was last frame.
 
        entries = []
        for i in range(self.ralphGroundHandler.getNumEntries()):
            entry = self.ralphGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
        if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
            self.ralph.setZ(entries[0].getSurfacePoint(render).getZ())
        else:
            self.ralph.setPos(startpos)
             
        entries2 = []
        for i in range(self.pandaActorGroundHandler.getNumEntries()):
            entry = self.pandaActorGroundHandler.getEntry(i)
            entries2.append(entry)
        entries2.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
        if (len(entries2)>0) and (entries2[0].getIntoNode().getName() == "terrain"):
            self.pandaActor.setZ(entries2[0].getSurfacePoint(render).getZ())
        else:
            self.pandaActor.setPos(startpos)   
 
        # Keep the camera at one foot above the terrain,
        # or two feet above ralph, whichever is greater.
         
        entries = []
        for i in range(self.camGroundHandler.getNumEntries()):
            entry = self.camGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
                                     x.getSurfacePoint(render).getZ()))
        if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
            base.camera.setZ(entries[0].getSurfacePoint(render).getZ()+1.0)
        if (base.camera.getZ() < self.ralph.getZ() + 2.0):
            base.camera.setZ(self.ralph.getZ() + 2.0)
             
        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.
         
        self.floater.setPos(self.ralph.getPos())
        self.floater.setZ(self.ralph.getZ() + 2.0)
        base.camera.lookAt(self.floater)
        
        if self.isMoving:
         self.moveRalph()
        
        return task.cont
     
    def displayLoginText(self, s="in"):
        self.loginText = addInstructions(-0.95, "A Ralph has logged " + s)
        myTask = taskMgr.doMethodLater(3, self.removeLoginText, 'removeLoginTextTask')
    
    def moveRalph(self):
     pkg = PyDatagram()
     pkg.addUint16(114)
     pkg.addFloat32(self.ralph.getX())
     pkg.addFloat32(self.ralph.getY())
     pkg.addFloat32(self.ralph.getZ())
     pkg.addFloat32(self.ralph.getH())
     self.cWriter.send(pkg,self.connection)
     
    def disconnect(self):
		pkg = PyDatagram()
		pkg.addUint16(119)
		self.cWriter.send(pkg,self.connection)
		sys.exit()
                
    def requestStop(self):
     pkg = PyDatagram()
     pkg.addUint16(115)
     self.cWriter.send(pkg,self.connection)
    
    def stopPlayer(self, data):
     id = data.getInt32()
     if id != self.id:
      self.opponents[id].character.stop()
      self.opponents[id].character.pose("walk",5)
     
    def movePlayer(self, data):
		id = data.getInt32()
		x = data.getFloat32()
		y = data.getFloat32()
		z = data.getFloat32()
                rotation = data.getFloat32()
                if id == self.id:
                 self.ralph.setPos(x, y, z)
                 self.ralph.setH(rotation)
                else:
                 self.opponents[id].character.setPos(x,y,z)
                 self.opponents[id].character.setH(rotation)
                 self.opponents[id].character.loop("run", restart = 0)
                 self.miniMap.updateTeamMatePos(id, x, y)
     
    def check(self):
               while self.cReader.dataAvailable():
                       print "data here"
                       datagram = NetDatagram()
                       # Retrieve the contents of the datagram.
                       if self.cReader.getData(datagram):
                               data = PyDatagramIterator(datagram)
                               responseCode = data.getUint16()
                               print responseCode
                               if responseCode == 201:
                                       self.getPlayer(data)
                               elif responseCode == 202:
                                       self.register(data)
                               elif responseCode == 203:
                                       self.getOpponent(data)
                               elif responseCode == 214:
                                       self.movePlayer(data)
                               elif responseCode == 215:
                                       self.stopPlayer(data)
                               elif responseCode == 219:
                                       self.dropPlayer(data)
                               else:
                                       print "nothing found"
    
    def heartbeat(self, task):
		pkg = PyDatagram()
		pkg.addUint16(113)
		self.cWriter.send(pkg,self.connection)
		return task.again
    
    def updateRoutine(self,task):
		self.check()
		return task.again;
    def login(self, task):
		self.option = 0
		self.option = str(raw_input("1-Login\n2-Register\n"))
		if self.option == "1":
			un = str(raw_input("Username: "))
			pw = str(raw_input("Password: "))
			request = self.loginRequest(un, pw)
			self.cWriter.send(request,self.connection)
			taskMgr.remove('login')
		elif self.option == "2":
			un = str(raw_input("Username: "))
			pw = str(raw_input("Password: "))
			request = self.registerRequest(un, pw)
			self.cWriter.send(request,self.connection)
			taskMgr.remove('login')
                         
    def loginRequest(self, username, password):
		pkg = PyDatagram()
		pkg.addUint16(101)
		pkg.addString(username)
		pkg.addString(password)
		return pkg
         
    def register(self, data):
		self.logStat = data.getUint16()
		if self.logStat == 0:
			print "Account Made"
			taskMgr.add(self.login, 'login')
		else:
			print "Username Taken"
			taskMgr.add(self.login, 'login')
         
    def registerRequest(self, username, password):
		pkg = PyDatagram()
		pkg.addUint16(102)
		pkg.addString(username)
		pkg.addString(password)
		return pkg
		
    def getPlayer(self, data):
		self.logStat = data.getUint16()
		if self.logStat == 0:
			self.id = data.getInt32()
			self.username = data.getString()
			x = data.getFloat32()
			y = data.getFloat32()
			z = data.getFloat32()
                        rotation = data.getFloat32()
                        if x == 0 and y == 0 and z == 0:
                         ralphStartPos = self.environ.find("**/start_point").getPos()
                         self.ralph.setPos(ralphStartPos.getX(),ralphStartPos.getY(),ralphStartPos.getZ())
			else:
                         self.ralph.setPos( x, y, z )
                         self.ralph.setH( rotation )
		else:
			print "login failed"
			taskMgr.add(self.login, 'login')
                        
    def getOpponent(self, data):
        opponent = Player()
        opponent.id = data.getInt32()
        opponent.username = data.getString()
        x = data.getFloat32()
        y = data.getFloat32()
        z = data.getFloat32()
        rotation = data.getFloat32()
        opponent.character.reparentTo(render)
        opponent.character.setScale(.2)
        opponent.character.setPos(x, y, z)
        opponent.character.setH(rotation)
        self.opponents[opponent.id] = opponent
        self.displayLoginText()
        self.miniMap.setTeamMate(opponent.id, 0.025, x, y)
                
    def dropPlayer(self, data):
        id = data.getInt32()
        self.opponents[id].character.removeNode()
        del self.opponents[id]
        self.displayLoginText(s="out")
        self.miniMap.delTeamMate(id)
                
    def removeLoginText(self, task):
        self.loginText.destroy()
        return task.done
     
    def listPlayers(self):
        i = 0.55
        for p in self.opponents:
            self.playersText.append( addInstructions(i, self.opponents[p].username) )
            i -= 0.05
     
    def delistPlayers(self):
        for x in self.playersText:
            x.destroy()
             
    def findClosestRalph(self):
        px = self.pandaActor.getX()
        py = self.pandaActor.getY()
        pz = self.pandaActor.getZ()
        
        closestPlayer = self.ralph
        rx = self.ralph.getX()
        ry = self.ralph.getY()
        rz = self.ralph.getZ()
        minDist = math.sqrt( (rx-px)*(rx-px) + (ry-py)*(ry-py) + (rz-pz)*(rz-pz) )
 
        for x in self.opponents:
            rx = self.opponents[x].character.getX()
            ry = self.opponents[x].character.getY()
            rz = self.opponents[x].character.getZ()
             
            dist = math.sqrt( (rx-px)*(rx-px) + (ry-py)*(ry-py) + (rz-pz)*(rz-pz) )
            if (dist < minDist):
                minDist = dist
                closestPlayer = self.opponents[x].character
         
        return closestPlayer, minDist
 
    # Panda chasing Ralph
    def setAI(self):        
        #Creating AI World
        self.AIworld = AIWorld(render)
  
        self.AIchar = AICharacter("panda",self.pandaActor, 100, 0.05, 5)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
  
        closestRalph = self.findClosestRalph()
        self.AIbehaviors.pursue(closestRalph[0])
        self.pandaActor.loop("walk")
  
        #AI World update        
        taskMgr.add(self.AIUpdate,"AIUpdate")
  
    #to update the AIWorld    
    def AIUpdate(self,task):
        self.AIworld.update()
         
        closestRalph = self.findClosestRalph()
        if ( self.numberOfPlayers <= 1 or not restrain(closestRalph[1], -CHASE_DISTANCE, CHASE_DISTANCE) or closestRalph[1] < 3):
            self.AIbehaviors.pauseAi("pursue")
        else: self.AIbehaviors.pursue(closestRalph[0])
         
        return task.cont
 
 
w = World()
run()