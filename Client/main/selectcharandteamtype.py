import __builtin__

""" Python Imports """
from hashlib import md5
from sys import exit
from time import strftime
import random, sys

""" Panda3D Imports """
from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import Texture
from panda3d.core import WindowProperties
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.interval.IntervalGlobal import Sequence


from common.Constants import Constants
from net.ConnectionManager import ConnectionManager



class selectcharandteamtype(DirectObject):
    TEXT_COLOR = (1,1,1,1)
    FONT_TYPE_01 = 0
    TEXT_SHADOW_COLOR = (0,0,0,0.5)
    characterSelectionInput = ""
    output = ""
    frame = DirectFrame()
    
    
    
    
    
    #character creation varaiables
    v=[0]
    v1=[0]
    nameOfChar = OnscreenText()
    nameOfCharTextbox = DirectEntry()
    factionSelection = OnscreenText()
    nameOfCharInput =''
    charactertype = OnscreenText()
    
    def __init__(self):
        print 'Loading character selection...'
        self.cManager = ConnectionManager()
        self.startConnection()
        frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                            frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                            pos=(-0.5, 0, 0.5))
        self.createCreateCharWindow()
        
        
    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True
    
    #character Creation        
    def createCreateCharWindow(self):
        self.frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                                frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                                pos=(-0.5, 0, 0.9))
        self.charactertype = OnscreenText(text = "Character type :", pos = (-0.60, 0.32), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.factionSelection.reparentTo(self.frame)
        self.buttons = [
        DirectRadioButton(text = ' Axe ', variable=self.v, value=[0], scale=0.07, pos=(-0.05,0,0.32), command=self.setText),
        DirectRadioButton(text = ' Sword ', variable=self.v, value=[1], scale=0.07, pos=(0.3,0,0.32), command=self.setText)
        ]
 
        for button in self.buttons:
            button.setOthers(self.buttons)
        
        
        self.factionSelection = OnscreenText(text = "Faction Selection :", pos = (-0.15, -0.95), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.factionSelection.reparentTo(self.frame)
        
        self.factionBtns = [
        DirectRadioButton(text = ' Blue ', variable=self.v1, value=[0], scale=0.07, pos=(-0.05,0,-0.05), command=self.setfaction),
        DirectRadioButton(text = ' Red ', variable=self.v1, value=[1], scale=0.07, pos=(0.3,0,-0.05), command=self.setfaction)
        ]
         
        for button1 in self.factionBtns:
            button1.setOthers(self.factionBtns)
        self.okForCreateBtn = DirectButton(text = ("Start", "Start", "Start", "disabled"), scale=.08, command=self.clickedOkForCreateBtn, pos=(-0.05, 0.0, -1.25))
        self.cancelForCreateBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "disabled"), scale=.08, command=self.clickedCancelForCreateBtn, pos=(0.4, 0.0, -1.25))
        self.okForCreateBtn.reparentTo(self.frame)
        self.cancelForCreateBtn.reparentTo(self.frame)
        
    def destroyCreateCharWindow(self):
        self.frame.destroy()
        self.nameOfChar.destroy()
        self.nameOfCharTextbox.destroy()
        self.factionSelection.destroy()
        self.okForCreateBtn.destroy()
        self.cancelForCreateBtn.destroy()
                                
    def clearnameOfChar(self):
        self.nameOfCharTextbox.enterText('')
        
    def getnameOfChar(self):
        self.nameOfCharInput = self.nameOfCharTextbox.get()
    
    def setnameOfChar(self, textEntered):
        print "name Of Char: ",textEntered
        self.nameOfChar = textEntered
        
    def clickedOkForCreateBtn(self):
        self.nameOfCharInput = self.nameOfCharTextbox.get().strip()
        print "you have pressed the ok button for creating a character"
        print "you have Created a char of type",self.chartitle,";Faction : ",self.factiontitle
        self.cManager.sendRequest(Constants.CMSG_CREATE_CHARACTER, (self.chartitle, self.factiontitle));
     
    def clickedCancelForCreateBtn(self):
        print "you have press the cancel button from the create character frame"
        self.destroyCreateCharWindow()
            
    
    def setText(self):
        self.chartitle = ""
        if self.v[0]:
            self.chartitle="sword"
        else:
            self.chartitle="axe"
        
        
    def setfaction(self):
        self.factiontitle = ""
        if self.v1[0]:
            self.factiontitle="red"
        else:
            self.factiontitle="blue"    
        
        
        
c = selectcharandteamtype()
run()
