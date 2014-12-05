from direct.showbase.ShowBase import ShowBase
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

from panda3d.core import ConnectionWriter
from panda3d.core import NetDatagram
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader

import random
import msvcrt as m

class MyApp(ShowBase):
	uname = None
	def __init__(self):
		ShowBase.__init__(self)
		
		self.cManager = QueuedConnectionManager()
		self.cListener = QueuedConnectionListener(self.cManager, 0)
		self.cReader = QueuedConnectionReader(self.cManager, 0)
		self.cWriter = ConnectionWriter(self.cManager, 0)
               
		
		host = "localhost";
    	        port = 6002;
		self.connection = self.cManager.openTCPClientConnection(host, port, 10000)
		
		self.received = 1
		
		if self.connection:
                	self.cReader.addConnection(self.connection)                	
			#taskMgr.add(self.updateRoutine, 'updateRoutine')
                       
                        # LOGIN Request Starts        
                        self.uname = raw_input('Enter username :')
                        self.password= raw_input('Enter password :')
			MyApp.uname = self.uname
                        #taskMgr.add(self.communicate101,'Login')
			if(self.received):
				print "->Client request:"
			# Send a request to the server
		
			myPyDatagram101 = PyDatagram()
			prot = 101
			myPyDatagram101.addUint16(prot)
			myPyDatagram101.addString(self.uname)
			myPyDatagram101.addString(self.password)
			self.cWriter.send(myPyDatagram101,self.connection)	
			self.received = 0
                        taskMgr.add(self.receiveResponse101,'Login')
                       
        def sendRequest101(self):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram101 = PyDatagram()
		prot = 101
		myPyDatagram101.addUint16(prot)
		myPyDatagram101.addString(self.uname)
		myPyDatagram101.addString(self.password)
		self.cWriter.send(myPyDatagram101,self.connection)	
		self.received = 0
        
	def receiveResponse101(self,task):
		
		while self.cReader.dataAvailable():
			datagram = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram):
				self.myIterator = PyDatagramIterator(datagram)
                                print "<-Server response:"
				print self.myIterator.getUint16()
				self.msg = self.myIterator.getUint32()
				self.l = self.myIterator.getUint32()
                                if self.msg is not None:
				    if self.l is not 0:
					for x in range(0,self.l):
						print self.myIterator.getString()
						print self.myIterator.getUint32()
						print self.myIterator.getUint32()
							
				    print self.msg, " received"
                                    #raw_input("Press Enter to continue...")
				    
                                    self.received = 0
				    taskMgr.remove('Login')
				   
				    #1-Character creatopm
				    #taskMgr.add(self.sendRequest104, 'CharacterCreation')
				    
				    #2-heartbeat of playgame after login
				    MyApp.sendRequest113(self)
		return task.again               	
		   	            
                # LOGIN Request End        
                              
			      
		# CHARACTER CREATION Starts
	
        def sendRequest104(self,task):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram = PyDatagram()
		prot = 104
		cname = raw_input('Character Name :')
		faction_id_104 = raw_input('press 0 for Red Or 1 for Blue ? :')
   		classType_104 = raw_input('press 0 for Axe Or 1 for Sword ? :')
		myPyDatagram.addUint16(prot)
		myPyDatagram.addString(cname)
		myPyDatagram.addUint32(faction_id_104)
		myPyDatagram.addUint32(classType_104)		
		self.cWriter.send(myPyDatagram,self.connection)	
					
		print "104 sent"
		self.received = 0
                taskMgr.add(self.receiveResponse104,"characterresponse")
        
	def receiveResponse104(self,task):
		
		while self.cReader.dataAvailable():
			datagram = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram):
				self.myIterator1 = PyDatagramIterator(datagram)
				print '------'
                                print self.myIterator1.getUint16()
                                self.msg = self.myIterator1.getUint32()
                                if self.msg is not None:
				    print "<-Server response:"
				    print self.msg, " received"
                                    raw_input("Press Enter to continue...")
                                    self.received = 0
				    taskMgr.remove('CharacterCreation')
				    taskMgr.add(self.sendRequest106, 'move')
				
	        return task.again
				
				
					
		#CHARACTER CREATION Ends
        
	
	# Move Starts    	
        def sendRequest106(self,task):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram106 = PyDatagram()
		prot = 106
		xpos = raw_input('X Position :')
		ypos = raw_input('Y Position :')
    		zpos = raw_input('Z Position :')
    		hpos = raw_input('Heading (0 to 360):')
		ismoving = raw_input('Moving ? -- 0 for NO , 1 for YES :')
		myPyDatagram106.addUint16(prot)
		myPyDatagram106.addUint32(xpos)
		myPyDatagram106.addUint32(ypos)
		myPyDatagram106.addUint32(zpos)
		myPyDatagram106.addUint32(hpos)
		myPyDatagram106.addUint32(ismoving)
		self.cWriter.send(myPyDatagram106,self.connection)	
					
		self.received = 0
                taskMgr.add(self.receiveResponse106,"characterresponse")
        
	def receiveResponse106(self,task):	
		while self.cReader.dataAvailable():
			datagram6 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram6):
				
				myIterator = PyDatagramIterator(datagram6)
                                print myIterator.getUint16()
				
                                msg = myIterator.getString()
                                
                                if msg is not None:
				    print "<-Server response:"
				    print msg
				    print myIterator.getUint32()
				    print myIterator.getUint32()
				    print myIterator.getUint32()
				    print myIterator.getUint32()
				    print myIterator.getUint32()
                                    raw_input("Press Enter to continue...")
                                    self.received = 1
				    # Attack
				    #raw_input("Press Enter to continue...") 
				    taskMgr.add(self.sendRequest108, 'health')
		return task.again				    
		#Move Ends
        
	#Change Health Starts
        def sendRequest108(self,task):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram108 = PyDatagram()
		prot = 108
		change_Health = raw_input('Change in health (-100 to 100):')
		myPyDatagram108.addUint16(prot)
		myPyDatagram108.addUint32(change_Health)
		self.cWriter.send(myPyDatagram108,self.connection)	
					
		self.received = 0
                taskMgr.add(self.receiveResponse108,"healthresponse")
        
	def receiveResponse108(self,task):
		
		while self.cReader.dataAvailable():
			datagram8 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram8):
				myIterator = PyDatagramIterator(datagram8)
                                print myIterator.getUint16()
                                msg = myIterator.getString()
                               
                                if msg is not None:
				    print "<-Server response:"
				    print msg
				    print myIterator.getUint32()
                                    self.received = 1
				    # CP State
				    raw_input("Press Enter to continue...") 
				    taskMgr.add(self.sendRequest107, 'attack')
		#Change Health Ends
	        return task.again
	
	# Attack Starts
        def sendRequest107(self,task):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram107 = PyDatagram()
		prot = 107
		attackId = raw_input('Attack Id (0 or 1):')
		myPyDatagram107.addUint16(prot)
		myPyDatagram107.addUint32(attackId)
		self.cWriter.send(myPyDatagram107,self.connection)	
					
		#print " sent"
		self.received = 0
                taskMgr.add(self.receiveResponse108,"attackresponse")
        
	def receiveResponse107(self,task):
		
		
		while self.cReader.dataAvailable():
			datagram7 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram7):
				myIterator = PyDatagramIterator(datagram7)
                                print myIterator.getUint16()
                                msg = myIterator.getString()
                                
                                if msg is not None:
				    print "<-Server response:"	
                                    print msg
				    print myIterator.getUint32()
				    raw_input("Press Enter to continue...")
                                    self.received = 1
                                     # Change Health
				    taskMgr.add(self.sendRequest112, 'CP Capture')
		return task.again				    
		#Attack Ends
	
				
	
	
	
	#CP Capture Starts
        def sendRequest112(self,task):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram112 = PyDatagram()
		prot = 112
		CP_id = raw_input('Control Point ID (1 to 5): ')
		faction_id = raw_input('press 0 for Red Or 1 for Blue ? :')
		myPyDatagram112.addUint16(prot)
		myPyDatagram112.addUint32(CP_id)
		myPyDatagram112.addUint32(faction_id)
		self.cWriter.send(myPyDatagram112,self.connection)	
					
		#print " sent"
		self.received = 0
                taskMgr.add(self.receiveResponse112,"CPCaptureRes")
        
	def receiveResponse112(self,task):
		
		while self.cReader.dataAvailable():
			datagram12 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram12):
				myIterator = PyDatagramIterator(datagram12)
                                print myIterator.getUint16()
                                msg = myIterator.getUint32()
                                
                                if msg is not None:
				    print "<-Server response:"
                                    print msg
				    print myIterator.getUint32()
				    raw_input("Press Enter to continue...")
                                    self.received = 1
                                     #HeartBeat
				    #raw_input("Press Enter to continue...") 
				    #taskMgr.add(self.communicate105, 'chat')
						    
		#CP Capture Ends
		
		
	# CHAT Starts
	def communicate105(self,task):
		#print "communicate"
		self.sendRequest105()
		self.receiveResponse105(task)		
                return task.again;
        		
        def sendRequest105(self):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram105 = PyDatagram()
		prot = 105
		chat = raw_input('Insert Chat Message :')
		myPyDatagram105.addUint16(prot)
		myPyDatagram105.addString(chat)
		self.cWriter.send(myPyDatagram105,self.connection)	
					
		print " sent"
		self.received = 0
                
        
	def receiveResponse105(self,task):
		print "<-Server response:"
		while self.cReader.dataAvailable():
			datagram5 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram5):
				myIterator = PyDatagramIterator(datagram5)
                                print myIterator.getUint16()
                                msg = myIterator.getUint16()
                                print msg, " received"
                                if msg is not None:
                                    raw_input("Press Enter to continue...")
                                    self.received = 1
                                     # Move
				    raw_input("Press Enter to continue...") 
				    taskMgr.add(self.communicate111, 'CP state')
						    
		#CHAT Ends
	
	
	#CP State Starts
	def communicate111(self,task):
		#print "communicate"
		self.sendRequest111()
		self.receiveResponse111(task)		
                return task.again;
        		
	def sendRequest111(self):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram111 = PyDatagram()
		prot = 111
		CP_id = raw_input('Control Point ID (1 to 5): ')
		CP_state = raw_input('Control Point state (1 red, 2 blue, 3 purple): ')
		myPyDatagram111.addUint16(prot)
		myPyDatagram111.addUint16(CP_id)
		myPyDatagram111.addUint16(CP_state)
		self.cWriter.send(myPyDatagram111,self.connection)	
					
		print " sent"
		self.received = 0
                
        
	def receiveResponse111(self,task):
		print "<-Server response:"
		while self.cReader.dataAvailable():
			datagram11 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram11):
				myIterator = PyDatagramIterator(datagram11)
                                print myIterator.getUint16()
                                msg = myIterator.getUint16()
                                print msg, " received"
                                if msg is not None:
                                    raw_input("Press Enter to continue...")
                                    self.received = 1
                                     # CP Capture
				    raw_input("Press Enter to continue...") 
				    taskMgr.add(self.communicate102, 'Logout')
		#CP State Ends
	
	
	# LOGOUT Starts
	def communicate102(self,task):
		#print "communicate"
		self.sendRequest102()
		self.receiveResponse102(task)		
                return task.again;
        		
        def sendRequest102(self):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram102 = PyDatagram()
		prot = 102
		myPyDatagram102.addUint16(prot)
		self.cWriter.send(myPyDatagram102,self.connection)	
					
		print " sent"
		self.received = 0
          
	def receiveResponse102(self,task):
		print "<-Server response:"
		while self.cReader.dataAvailable():
			datagram2 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram2):
				myIterator = PyDatagramIterator(datagram2)
                                print myIterator.getUint16()
                                msg = myIterator.getUint16()
                                print msg, " received"
                                if msg is not None:
                                    raw_input("Press Enter to continue...")
                                    self.received = 1
                                     # Register
				    raw_input("Press Enter to continue...")
				    taskMgr.add(self.communicate301, 'Heartbeat')
						    
		#LOGOUT Ends
		
		
		#HeartBeat Starts
	def communicate301(self):
		#print "communicate"
		self.sendRequest301()
		self.receiveResponse301()		
                #return task.again;
        		
        def sendRequest301(self,task):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram301 = PyDatagram()
		prot = 301
		myPyDatagram301.addUint16(prot)
		self.cWriter.send(myPyDatagram301,self.connection)	
		self.received = 0
                return task.again
        
	def receiveResponse301(self):
		
		while self.cReader.dataAvailable():
			datagram301 = NetDatagram()
			# Retrieve the contents of the datagram.
			if self.cReader.getData(datagram301):
				myIterator = PyDatagramIterator(datagram301)
                                p =  myIterator.getUint16()
                                if p == 213:
					un = myIterator.getString()
					cname = myIterator.getString()
					ctype = myIterator.getUint32()
					cteam = myIterator.getUint32()	
					if un ==  MyApp.uname:
						abc = 'abc'
					else:	
						print cname+' just joined a game......!! hurray'
				
					#print msg, " received"
					
					self.received = 1
                                		    
		#HeartBeat Ends
		
	#heartbeat
	def sendRequest113(self):
		if(self.received):
			print "->Client request:"
			# Send a request to the server
		
		myPyDatagram113 = PyDatagram()
		prot = 113
		myPyDatagram113.addUint16(prot)
		print MyApp.uname+'-------'
		if MyApp.uname == 'chintan':
			myPyDatagram113.addUint32(18)
		elif MyApp.uname == 'paras':
			myPyDatagram113.addUint32(35)
		else:
			myPyDatagram113.addUint32(3)
		self.cWriter.send(myPyDatagram113,self.connection)	
		self.received = 0
		#taskMgr.add(self.updateRoutine,'update113')
		#taskMgr.doMethodLater(1,self.sendRequest301,'HeatBeat')
		MyApp.retrieve113(self)
		
	def retrieve113(self):
		taskMgr.add(self.updateRoutine,'update113')
		taskMgr.doMethodLater(1,self.sendRequest301,'HeatBeat')
	
		
	def updateRoutine(self,task):
		self.receiveResponse301()
		return task.again;

	
       
app = MyApp()
app.run() #enters the panda3D main loop


