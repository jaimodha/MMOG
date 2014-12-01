
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TextNode
import direct.directbase.DirectStart
import random, sys, os, math
from common.Constants import Constants
import direct.directbase.DirectStart
from Queue import Queue
import __builtin__

class Chat(object):
	def __init__(self, manager):
		__builtin__.chat = self
		self.cManager = manager
		self.msgQ = Queue()
		#taskMgr.doMethodLater(2, self.refresh, 'Heartbeat')

		self.messageList = []
		#set different color depend on their username
		#--initiate chat message
		chat = { 'userName' : main.username,     #username
		         'message'    : '-------Login------' }
		self.cManager.sendRequest(Constants.CMSG_CHAT, chat)
		#---
		self.numMessage = -1
		self.currentCanvasHeight = 0
		#scroll frame
		self.chatFrame = DirectScrolledFrame(
		                                     pos=(-2*.5,0,.55*.5),
		                                     relief= DGG.GROOVE,
		                                     borderWidth=(.01,.01),
		                                     frameColor=(1,1,1,.25),
		                                     canvasSize = (-.33,.506,-2,2), 
		                                     frameSize = (-.33,.5,-1.15,-.7),
		                                     manageScrollBars=False,
		                                     autoHideScrollBars=True,
		                                     verticalScroll_resizeThumb=False,
		                                     verticalScroll_thumb_frameSize=(0,.01,-.01,0),
		                                     scrollBarWidth=0.04)
		#self.chatFrame.destroycomponent('horizontalScroll')
		self.verticalScroll = self.chatFrame.component('verticalScroll')
		self.verticalScroll['scrollSize'] = .5*0.005

		self.chatBox=self.chatFrame.getCanvas().attachNewNode('myCanvas')
		#input frame
		self.chatInput = DirectEntry(text = "" ,scale=.05,command=self.sendMessage,
		                            numLines = 2, width=16.5,
		                            frameColor=(1,1,1,0.35),focusInCommand=self.clearText,
		                            borderWidth=(.01,.01),
		                            text_fg=(1,1,0,1))
		self.chatInput.setPos(-1.33,0,-.93)
		self.msgQ = Queue()
		#taskMgr.add(self.refresh, 'Heartbeat')
		taskMgr.add(self.resizeScreen, 'resizeScreen')

	def refresh(self,task):
	    self.cManager.sendRequest(Constants.REQ_HEARTBEAT)
	    return task.again

	def clearText(self):
	    self.chatInput.enterText('')
	     
	#this being called from responseChat, it will add the message to the queue
	def putToChatQ(self,username, message):
	    self.msgQ.put({'userName' : username,'message' : message})
	    #print self.msgQ.qsize()
	    while not self.msgQ.empty():
	        event = self.msgQ.get()
	        self.addMessage(event['userName'],event['message'])
	        self.msgQ.task_done()

	#add message to the scrolled frame
	def addMessage(self,username,msg):
	    newMessage = DirectButton(parent = self.chatBox,
	                              scale = .055,
	                              pos = (0,0,self.currentCanvasHeight),
	                              relief = None,
	                              pad=(0,0),
	                              borderWidth=(0.01,0.01),
	                              text = username+'>> '+msg,            #text
	                              text_wordwrap = 15,
	                              text_align = TextNode.ALeft,          
	                              text_fg=(1,0,1,1),                 #change color here
	                              enableEdit = False,
	                              suppressMouse = False)
	    if username == main.username:
	        newMessage["text_fg"]=(1,1,0,1)
	    self.messageList.append(newMessage)
	    self.numMessage += 1
	    self.updateCanvasHeight()
	    # Scroll till the last line.
	    self.chatFrame['verticalScroll_value'] = 1
	    #create packet to send 

	#this medthod is called when the user press enter after they type something
	def sendMessage(self, textMessage):
	    chat = { 'userName' : main.username,     #username
	             'message'    : textMessage }
	    self.cManager.sendRequest(Constants.CMSG_CHAT, chat)
	    self.clearText()
	    #clear scrollframe context and attach the frame again
	    #self.chatBox.removeNode()
	    #self.chatBox=self.chatFrame.getCanvas().attachNewNode('myCanvas')
	    
	    #self.addMessage()
	    
	def updateCanvasHeight(self):
	    self.updateMessages()
	    self.chatFrame['canvasSize'] = (0,1.2,self.currentCanvasHeight,0)

	def updateMessages(self):
	    messageSpacing = -0.07

	    for i in range(0,self.numMessage+1):
	        self.messageList[i].setZ(messageSpacing)
	        l,r,b,t = self.messageList[i].getBounds()
	        messageSpacing += (b-t)*0.07

	    self.currentCanvasHeight = messageSpacing

	def resizeScreen(self, task):
		if base.win.getXSize()!= 800 and base.win.getYSize()!=600:
		    self.chatFrame.setPos(-2.725*.5,0,.55*.5)
		    self.chatInput.setPos(-1.695,0,-.93)
		else:
		    self.chatFrame.setPos(-2*.5,0,.55*.5)
		    self.chatInput.setPos(-1.33,0,-.93)

		return task.cont
