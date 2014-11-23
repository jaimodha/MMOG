from direct.showbase.ShowBase import ShowBase
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode,NodePath,Camera,TextNode

from panda3d.core import ConnectionWriter
from panda3d.core import NetDatagram
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader

import random, sys, os, math

# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)
 
# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)
 

class Player():
	
	def __init__(self):
		id = 0
		username = ""
		x = 0
		y = 0
		z = 0
		rotation = 0
		
class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		
		self.cManager = QueuedConnectionManager()
		self.cListener = QueuedConnectionListener(self.cManager, 0)
		self.cReader = QueuedConnectionReader(self.cManager, 0)
		self.cWriter = ConnectionWriter(self.cManager, 0)
		
		self.player = Player()
		self.opponents = dict()
		self.logStat = -1
		
		host = "localhost"
		port = 9252
		self.connection = self.cManager.openTCPClientConnection(host, port, 10000)
		
		self.received = 1
		
		self.playersText = []
		
		if self.connection:
			self.cReader.addConnection(self.connection)                	
			taskMgr.add(self.updateRoutine, 'updateRoutine')
			taskMgr.add(self.login, 'login')
			#taskMgr.doMethodLater(3, self.updateRoutine, 'updateRoutine')
			taskMgr.doMethodLater(.1, self.heartbeat, 'heartbeat')
		
		self.accept("q", self.listPlayers)
		self.accept("q-up", self.delistPlayers)
		self.accept("escape", self.disconnect)
		self.accept("arrow_up", self.move)
		
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
		
	def registerRequest(self, username, password):
		pkg = PyDatagram()
		pkg.addUint16(102)
		pkg.addString(username)
		pkg.addString(password)
		return pkg
			
	def disconnect(self):
		pkg = PyDatagram()
		pkg.addUint16(119)
		self.cWriter.send(pkg,self.connection)
		sys.exit()
	
	def move(self):
		self.player.x += 1
		pkg = PyDatagram()
		pkg.addUint16(114)
		pkg.addFloat32(self.player.x)
		pkg.addFloat32(self.player.y)
		pkg.addFloat32(self.player.z)
		pkg.addFloat32(self.player.rotation)
		self.cWriter.send(pkg,self.connection)
		
	def movePlayer(self, data):
		id = data.getInt32()
		x = data.getFloat32()
		y = data.getFloat32()
		z = data.getFloat32()
		rotation = data.getFloat32()
		if self.player.id == id:
			self.player.x = x
			self.player.y = y
			self.player.z = z
			self.player.rotation = rotation
		else:
			self.opponents[id].x = x
			self.opponents[id].y = y
			self.opponents[id].z = z
			self.opponents[id].rotation = rotation
	
	def dropPlayer(self, data):
		id = data.getInt32()
		del self.opponents[id]
		
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
	
	def getPlayer(self, data):
		self.logStat = data.getUint16()
		if self.logStat == 0:
			self.player.id = data.getInt32()
			self.player.username = data.getString()
			self.player.x = data.getFloat32()
			self.player.y = data.getFloat32()
			self.player.z = data.getFloat32()
			self.player.rotation = data.getFloat32()
		else:
			print "login failed"
			taskMgr.add(self.login, 'login')
	
	def register(self, data):
		self.logStat = data.getUint16()
		if self.logStat == 0:
			print "Account Made"
			taskMgr.add(self.login, 'login')
		else:
			print "Username Taken"
			taskMgr.add(self.login, 'login')
	
	def listPlayers(self):
		i = 0.55
		for p in self.opponents:
			self.playersText.append( addInstructions(i, self.opponents[p].username + " " + "{:.2f}".format(self.opponents[p].x) + " " + "{:.2f}".format(self.opponents[p].y) + " " + "{:.2f}".format(self.opponents[p].z) + " " + "{:.2f}".format(self.opponents[p].rotation) ))
			i -= 0.05
	
	def delistPlayers(self):
		for x in self.playersText:
			x.destroy()
	
	def getOpponent(self, data):
		opponent = Player()
		opponent.id = data.getInt32()
		opponent.username = data.getString()
		opponent.x = data.getFloat32()
		opponent.y = data.getFloat32()
		opponent.z = data.getFloat32()
		opponent.rotation = data.getFloat32()
		self.opponents[opponent.id] = opponent

app = MyApp()
app.run() #enters the panda3D main loop