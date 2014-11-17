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



class characterSelection(DirectObject):
    TEXT_COLOR = (1,1,1,1)
    FONT_TYPE_01 = 0
    TEXT_SHADOW_COLOR = (0,0,0,0.5)
    characterSelectionInput = ""
    output = ""
    frame = DirectFrame()
    
    #character selection varaiables
    createCharacter = DirectButton()
    deleteCharacter = DirectButton()
    selectCharacter = OnscreenText()
    selectCharacterTextbox = DirectEntry()
    selectCharacterInput=''
    referenceForSelection = OnscreenText()
    myScrolledList = DirectScrolledList()
    submitBtn = DirectButton()
    cancelBtn = DirectButton()
    
    #character deletion varaiables
    selectCharactertodelete = OnscreenText()
    deleteBtn = DirectButton()
    delCancelBtn = DirectButton()
    CharacterToDeleteTextbox = DirectEntry()
    referenceForDeletion = OnscreenText()
    CharacterToDeleteInput = ' '
    
    #character creation varaiables
    v=[0]
    v1=[0]
    nameOfChar = OnscreenText()
    nameOfCharTextbox = DirectEntry()
    factionSelection = OnscreenText()
    nameOfCharInput =''
    
    def __init__(self):
        print 'Loading character selection...'
        self.cManager = ConnectionManager()
        self.startConnection()
        frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                            frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                            pos=(-0.5, 0, 0.5))
        self.createSelectionWindow()
    
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
        self.buttons = [
        DirectRadioButton(text = ' Sword ', variable=self.v, value=[0], scale=0.07, pos=(-0.4,0,0.32), command=self.setText),
        DirectRadioButton(text = ' Axe ', variable=self.v, value=[1], scale=0.07, pos=(0.2,0,0.32), command=self.setText)
        ]
 
        for button in self.buttons:
            button.setOthers(self.buttons)
        
        self.nameOfChar = OnscreenText(text = "Name The Character :", pos = (-0.2, -0.75), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.nameOfChar.reparentTo(self.frame)    
        self.nameOfCharTextbox = DirectEntry(text = "" ,scale=.07,pos=(0.25,0, -.75),command=self.setnameOfChar,initialText="name of character", numLines = 1,focus=0,focusInCommand=self.clearnameOfChar, focusOutCommand=self.getnameOfChar)
        self.nameOfCharTextbox.reparentTo(self.frame)   
        
        self.factionSelection = OnscreenText(text = "Faction Selection :", pos = (-0.15, -0.95), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.factionSelection.reparentTo(self.frame)
        
        self.factionBtns = [
        DirectRadioButton(text = ' Blue ', variable=self.v1, value=[0], scale=0.07, pos=(-0.05,0,-0.05), command=self.setfaction),
        DirectRadioButton(text = ' Red ', variable=self.v1, value=[1], scale=0.07, pos=(0.3,0,-0.05), command=self.setfaction)
        ]
         
        for button1 in self.factionBtns:
            button1.setOthers(self.factionBtns)
        self.okForCreateBtn = DirectButton(text = ("Ok", "Ok", "Ok", "disabled"), scale=.08, command=self.clickedOkForCreateBtn, pos=(-0.05, 0.0, -1.25))
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
        print "you have pressed the ok button for creating a character"
     
    def clickedCancelForCreateBtn(self):
        print "you have press the cancel button from the create character frame"
        self.destroyCreateCharWindow()
        self.createSelectionWindow()    
    
    def setText(status=None):
        bk_text = "CurrentValue "
        
    def setfaction(status=None):
        bk_text = "CurrentValue "    
        
    #character deletion        
    def createDeleteCharWindow(self):
        self.frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                                frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                                pos=(-0.5, 0, 0.9))
        
        self.selectCharactertodelete = OnscreenText(text = "Select Character :", pos = (-0.02, -0.35), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.selectCharactertodelete.reparentTo(self.frame)
        self.selectCharacterToDeleteTextbox = DirectEntry(text = "" ,scale=.07,pos=(0.45,0, -.35),command=self.setselectCharacterToDelete,initialText="name of character", numLines = 1,focus=0,focusInCommand=self.clearselectCharacterToDelete, focusOutCommand=self.getselectCharacterToDelete)
        self.selectCharacterToDeleteTextbox.reparentTo(self.frame)
        self.referenceForDeletion = OnscreenText(text = "Reference to Character List:", pos = (-0.15, -0.75), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.referenceForDeletion.reparentTo(self.frame)
        self.deleteScrolledList = DirectScrolledList(
        decButton_pos= (0.35, 0, 0.53),
        decButton_text = "Dec",
        decButton_text_scale = 0.04,
        decButton_borderWidth = (0.005, 0.005),
 
        incButton_pos= (0.35, 0, -0.02),
        incButton_text = "Inc",
        incButton_text_scale = 0.04,
        incButton_borderWidth = (0.005, 0.005),
        
        
        pos = (0.7, 0, -0.99),
        numItemsVisible = 4,
        forceHeight = .11,
        itemFrame_frameSize = (-0.6, 0.6, -0.37, 0.11),
        itemFrame_pos = (0.35, 0, 0.4))
        
        for playerchar in ['xxxbluesword', 'xxxblueaxe', 'xxxredsword', 'xxxredsword01','xxx_red_sword04']:
            l = DirectLabel(text = playerchar, text_scale=0.1)
            self.deleteScrolledList.addItem(l)
            
        self.deleteScrolledList.reparentTo(self.frame)
        self.deleteBtn = DirectButton(text = ("Delete", "Delete", "Delete", "disabled"), scale=.08, command=self.clickedDelete, pos=(-0.2, 0.0, -1.25))
        
        self.delCancelBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "disabled"), scale=.08, command=self.clickedDelCancel, pos=(0.3, 0.0, -1.25))
        self.deleteBtn.reparentTo(self.frame)
        self.delCancelBtn.reparentTo(self.frame)
        
    def destroyDeleteCharWindow(self):
        self.frame.destroy()
        self.selectCharactertodelete.destroy()
        self.deleteBtn.destroy()
        self.delCancelBtn.destroy()
        self.selectCharacterToDeleteTextbox.destroy()
        self.referenceForDeletion.destroy()
        
    def clearselectCharacterToDelete(self):
        self.selectCharacterToDeleteTextbox.enterText('')
        
    def getselectCharacterToDelete(self):
        self.selectCharacterToDeleteInput = self.nameOfCharTextbox.get()
    
    def setselectCharacterToDelete(self, textEntered):
        print "name Of Char: ",textEntered
        self.selectCharacterToDelete = textEntered
        
    def clickedDelete(self):
        print "You pressed delete a character"
        
    def clickedDelCancel(self):
        print "to go back to slection menu"
        self.destroyDeleteCharWindow()
        self.createSelectionWindow()
            
    
    #character Selection
    def createSelectionWindow(self):
        self.frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                                frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                                pos=(-0.5, 0, 0.9))
                
        self.createCharacter = DirectButton(text = ("Create Character","Create Character","Create Character","disabled"), scale=.08, command = self.clickedCreateChar, pos=(-0.14,0.0,-0.25))
        self.deleteCharacter = DirectButton(text = ("Delete Character","Delete Character","Delete Character","disabled"), scale=.08, command = self.clickedDeleteChar, pos=(-0.14,0.0,-0.40))
        self.createCharacter.reparentTo(self.frame)
        self.deleteCharacter.reparentTo(self.frame)
        self.selectCharacter = OnscreenText(text = "Select Character :", pos = (-0.12, -0.55), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.selectCharacter.reparentTo(self.frame)
        
        self.myScrolledList = DirectScrolledList(
        decButton_pos= (0.35, 0, 0.53),
        decButton_text = "Dec",
        decButton_text_scale = 0.04,
        decButton_borderWidth = (0.005, 0.005),
 
        incButton_pos= (0.35, 0, -0.02),
        incButton_text = "Inc",
        incButton_text_scale = 0.04,
        incButton_borderWidth = (0.005, 0.005),
 
        
        pos = (0.05, 0, -0.3),
        numItemsVisible = 4,
        forceHeight = .11,
        itemFrame_frameSize = (-0.6, 0.6, -0.37, 0.11),
        itemFrame_pos = (0.35, 0, 0.4),
        )
        
        self.selectCharacterTextbox = DirectEntry(text = "" ,scale=.07,pos=(0.28,0, -.55),command=self.setselectCharacterTextbox,initialText="name of character", numLines = 1,focus=0,focusInCommand=self.clearselectCharacterTextbox, focusOutCommand=self.getselectCharacterTextbox)
        self.selectCharacterTextbox.reparentTo(self.frame)
        self.referenceForSeletion = OnscreenText(text = "Reference to Character List:\n that already exists", pos = (-0.30, -0.75), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.referenceForSeletion.reparentTo(self.frame)
      
        for playerchar in ['xxxbluesword', 'xxxblueaxe', 'xxxredsword', 'xxxredsword01','xxx_red_sword04']:
            l = DirectLabel(text = playerchar, text_scale=0.1)
            self.myScrolledList.addItem(l) 
        
        self.submitBtn = DirectButton(text = ("Start", "Start", "Start", "disabled"), scale=.08, command=self.clickedSubmit, pos=(-0.2, 0.0, -1.45))
        
        self.cancelBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "disabled"), scale=.08, command=self.clickedCancel, pos=(0.3, 0.0, -1.45))
        self.submitBtn.reparentTo(self.frame)
        self.cancelBtn.reparentTo(self.frame)
        
    def destroySelectionWindow(self):
        self.frame.destroy()
        self.selectCharacter.destroy()
        self.createCharacter.destroy()
        self.deleteCharacter.destroy()
        self.submitBtn.destroy()        
        self.cancelBtn.destroy()
    
    def clearselectCharacterTextbox(self):
        self.selectCharacterTextbox.enterText('')
        
    def getselectCharacterTextbox(self):
        self.selectCharacterTextbox = self.selectCharacterTextbox.get()
    
    def setselectCharacterTextbox(self, textEntered):
        print "name Of Char: ",textEntered
        self.selectCharacterTextbox = textEntered
        
    def clickedCreateChar(self):
        print "You pressed create a new character"
        self.destroySelectionWindow()
        self.createCreateCharWindow()  
    
    def clickedDeleteChar(self):
        print "You pressed delete a character"
        self.destroySelectionWindow()
        self.createDeleteCharWindow()  
        
    def clickedSubmit(self):
        print "you pressed start button"
  
    def clickedCancel(self):
        print "You pressed Cancel"
        

c = characterSelection()
run()
