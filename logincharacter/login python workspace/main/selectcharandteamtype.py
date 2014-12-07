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
from panda3d.core import TransparencyAttrib

#from main.login2 import login
#from main.Register import Register
from common.Constants import Constants
from net.ConnectionManager import *



class selectcharandteamtype:
    TEXT_COLOR = (1,1,1,1)
    FONT_TYPE_01 = 0
    TEXT_SHADOW_COLOR = (0,0,0,0.5)
    characterSelectionInput = ""
    output = ""
    #frame = DirectFrame()
    
    username01 = "harsh01"
    
    #character selection varaiables
    data1=2
    #name1 = OnscreenText()
    #name2 = OnscreenText()
    #name3 = OnscreenText()
    name11 = "harsh0111"
    name22 = "xtremekiller"
    name33 = "killermaster"
    #submitBtn = DirectButton()
    #cancelBtn = DirectButton()
    #createbtn = DirectButton()
    greyimage = "grey.png"
    swordimage = "sword.png"
    axeimage = "Axe.png"
    username = OnscreenText()
    src = ""
    #character creation varaiables
    v=[0]
    v1=[0]
    va1 = [0]
    va2 = [0]
    va3 = [0]
    nameOfChar = OnscreenText()
    #nameOfCharTextbox = DirectEntry()
    factionSelection = OnscreenText()
    nameOfCharInput =''
    #charactertype = OnscreenText()
    chartitle = ""
    factiontitle=""
    chardata =""
    def __init__(self):
        __builtin__.main=self
        print 'Loading character selection...'
        self.some =""
        #self.cManager = ConnectionManager()
        #self.startConnection()
        frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                            frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                            pos=(-0.5, 0, 0.5))
        
        self.dict = {1:'sword blueswordcutter blue'} 
        
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
        
        
            
        
        print "print somethg:",self.some
        self.swordImage=OnscreenImage(image = Constants.IMG_SWORD, pos = (0.3, 0, 0.62),scale = 0.15)
        self.swordImage.setTransparency(TransparencyAttrib.MAlpha)
        self.axeImage=OnscreenImage(image = Constants.IMG_AXE, pos = (-0.05, 0, 0.62),scale = 0.15)
        self.axeImage.setTransparency(TransparencyAttrib.MAlpha)
        
        self.username = OnscreenText(text = self.username01, pos = (-1,.5), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.username.reparentTo(self.frame)
        
        self.charactertype = OnscreenText(text = "Character type :", pos = (-0.60, 0.32), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.factionSelection.reparentTo(self.frame)
        self.buttons = [
        DirectRadioButton(text = '', variable=self.v, value=[0], scale=0.07, pos=(-0.05,0,0.32), command=self.setText),
        DirectRadioButton(text = '', variable=self.v, value=[1], scale=0.07, pos=(0.35,0,0.32), command=self.setText)
        ]
 
        for button in self.buttons:
            button.setOthers(self.buttons)
        
        self.nameOfChar = OnscreenText(text = "Name The Character :", pos = (-0.2, -0.75), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.nameOfChar.reparentTo(self.frame)    
        self.nameOfCharTextbox = DirectEntry(text = "" ,scale=.07,pos=(0.3,0, -.75),command=self.setnameOfChar,initialText="name of character", numLines = 1,focus=0,focusInCommand=self.clearnameOfChar, focusOutCommand=self.getnameOfChar)
        self.nameOfCharTextbox.reparentTo(self.frame)   
        
        self.factionSelection = OnscreenText(text = "Faction Selection :", pos = (-0.15, -1.0), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.factionSelection.reparentTo(self.frame)
        self.blueImage=OnscreenImage(image = Constants.IMG_BLUE, pos = (-0.05, 0, -0.02),scale = 0.08)
        self.blueImage.setTransparency(TransparencyAttrib.MAlpha) 
        self.redImage=OnscreenImage(image = Constants.IMG_RED, pos = (0.26, 0, -0.02),scale = 0.08)
        self.redImage.setTransparency(TransparencyAttrib.MAlpha)
        self.factionBtns = [
        DirectRadioButton(text = '', variable=self.v1, value=[0], scale=0.07, pos=(-0.01,0,-0.2), command=self.setfaction),
        DirectRadioButton(text = '', variable=self.v1, value=[1], scale=0.07, pos=(0.3,0,-0.2), command=self.setfaction)
        ]
         
        for button1 in self.factionBtns:
            button1.setOthers(self.factionBtns)
        self.okForCreateBtn = DirectButton(text = ("Create", "Create", "Create", "disabled"), scale=.09, command=self.clickedOkForCreateBtn, pos=(0.2, 0.0, -1.3))
        self.cancelForCreateBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "disabled"), scale=.09, command=self.clickedCancelForCreateBtn, pos=(0.6, 0.0, -1.3))
        self.okForCreateBtn.reparentTo(self.frame)
        self.cancelForCreateBtn.reparentTo(self.frame)
        
    def destroyCreateCharWindow(self):
        self.nameOfChar.destroy()
        self.swordImage.destroy()
        self.axeImage.destroy()
        self.blueImage.destroy()
        self.redImage.destroy()
        self.nameOfChar.destroy()
        self.nameOfCharTextbox.destroy()
        self.factionSelection.destroy()
        self.okForCreateBtn.destroy()
        self.cancelForCreateBtn.destroy()
        self.factionSelection.destroy()
        self.frame.destroy()
        #self.factionBtns.destroy()
        #self.button.destory()
                                
    def mainresp(self,chartype,charname,charfact):
        print "printed these",chartype,charname,charfact
        chardata="".join((chartype," ",charname," ",charfact))
        if(self.lengthdic<=3):
            self.dict[self.lengthdic+1] = chardata  
        else:
            print "u can have only 3 character"
        self.createSelectionWindow()
        
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
        print "you have Created a char of type",self.chartitle,";Faction : ",self.factiontitle,";name of character",self.nameOfCharInput,"; with username : ",self.username01
        self.cManager = ConnectionManager()
        self.startConnection()
        self.cManager.sendRequest(Constants.CMSG_CREATE_CHARACTER, (self.chartitle, self.nameOfCharInput,self.factiontitle));
        print "print somethg:",self.some
        
     
    def clickedCancelForCreateBtn(self):
        print "you have press the cancel button from the create character frame"
        self.destroyCreateCharWindow()
        self.createSelectionWindow()
        #go back to login    
    
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
        
    #character Selection
    def createSelectionWindow(self):
        self.frame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                                frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                                pos=(-0.5, 0, 0.9))
        self.lengthdic = len(self.dict)
        print self.lengthdic
        if(self.lengthdic>3):
            del self.dict[4]
            self.lengthdic = len(self.dict)
            print "updated lenght : ",self.lengthdic 
            
        if(self.lengthdic==1):
            self.src = self.dict[1]
            print "dic 1",self.src
            self.dicts1 = self.src.split()
            if(self.dicts1[0] =="axe"):
                self.fristimageforchartype = Constants.IMG_AXE
            else:
                self.fristimageforchartype = Constants.IMG_SWORD
            #set the name of the character
            self.name11 = self.dicts1[1]
            #set the color of the faction
            if(self.dicts1[2] =="blue"):
                self.fristimagefactiontype = Constants.IMG_BLUE
            else:
                self.fristimagefactiontype = Constants.IMG_RED
            
            
            
        if(self.lengthdic==2):
            self.src = self.dict[1]
            print "dic 1",self.src
            self.dicts1 = self.src.split()
            if(self.dicts1[0] =="axe"):
                self.fristimageforchartype = Constants.IMG_AXE
            else:
                self.fristimageforchartype = Constants.IMG_SWORD
            
            self.src2 = self.dict[2]
            print "dic 2",self.src2
            self.dicts2 = self.src2.split()
            if(self.dicts2[0] =="axe"):
                self.secondimageforchartype = Constants.IMG_AXE
            else:
                self.secondimageforchartype = Constants.IMG_SWORD
            
            self.name11 = self.dicts1[1]
            self.name22 = self.dicts2[1]
            
            #set the color of the faction
            if(self.dicts1[2] =="blue"):
                self.fristimagefactiontype = Constants.IMG_BLUE
            else:
                self.fristimagefactiontype = Constants.IMG_RED
    
            if(self.dicts2[2] =="blue"):
                self.secondimagefactiontype = Constants.IMG_BLUE
            else:
                self.secondimagefactiontype = Constants.IMG_RED
                
        if(self.lengthdic<=3 and self.lengthdic>2):
            self.src = self.dict[1]
            print "dic 1",self.src
            self.dicts1 = self.src.split()
            
            if(self.dicts1[0] =="axe"):
                self.fristimageforchartype = Constants.IMG_AXE
            else:
                self.fristimageforchartype = Constants.IMG_SWORD
            
            self.src2 = self.dict[2]
            print "dic 2",self.src2
            self.dicts2 = self.src2.split()
            if(self.dicts2[0] =="axe"):
                self.secondimageforchartype = Constants.IMG_AXE
            else:
                self.secondimageforchartype = Constants.IMG_SWORD
            
                
            self.src3 = self.dict[3]    
            print "dic 3",self.src3
            self.dicts3 = self.src3.split()
            if(self.dicts3[0] =="axe"):
                self.thridimageforchartype = Constants.IMG_AXE
            else:
                self.thridimageforchartype = Constants.IMG_SWORD
            self.name11 = self.dicts1[1]
            self.name22 = self.dicts2[1]
            self.name33 = self.dicts3[1]
            
            #set the color of the faction
            if(self.dicts1[2] =="blue"):
                self.fristimagefactiontype = Constants.IMG_BLUE
            else:
                self.fristimagefactiontype = Constants.IMG_RED
    
            if(self.dicts2[2] =="blue"):
                self.secondimagefactiontype = Constants.IMG_BLUE
            else:
                self.secondimagefactiontype = Constants.IMG_RED
            
            if(self.dicts3[2] =="blue"):
                self.thridimagefactiontype = Constants.IMG_BLUE
            else:
                self.thridimagefactiontype = Constants.IMG_RED    
            
        print self.dicts1[0]
            
        if(self.lengthdic==1):
            self.greyImage1=OnscreenImage(image = Constants.IMG_GREY , pos = (0.8, 0, 0.62),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = Constants.IMG_GREY, pos = (-0.0, 0, 0.62),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = self.fristimageforchartype, pos = (-0.8, 0, 0.62),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
            
            self.name1 = OnscreenText(text = self.name11, pos = (-0.85, 0.2), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.factionImage1=OnscreenImage(image = self.fristimagefactiontype, pos = (-0.85, 0, 0.0),scale = 0.08)
            self.factionImage1.setTransparency(TransparencyAttrib.MAlpha) 
        
            #change method and variable names
            self.mainRadioBtns1 = [
                DirectRadioButton(text = '', variable=self.va1, value=[0], scale=0.07, pos=(-0.8,0,-0.25), command=self.setcharselection1)
                ]
            for mainbutton1 in self.mainRadioBtns1:
                mainbutton1.setOthers(self.mainRadioBtns1)
            
        elif(self.lengthdic==2):
            self.greyImage1=OnscreenImage(image = Constants.IMG_GREY, pos = (0.8, 0, 0.62),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = self.secondimageforchartype, pos = (-0.0, 0, 0.62),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = self.fristimageforchartype, pos = (-0.8, 0, 0.62),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
            
            self.name1 = OnscreenText(text = self.name11, pos = (-0.85, 0.2), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.name2 = OnscreenText(text = self.name22, pos = (0.0, 0.2), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            
            self.factionImage1=OnscreenImage(image = self.fristimagefactiontype, pos = (-0.85, 0, 0.0),scale = 0.08)
            self.factionImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.factionImage2=OnscreenImage(image = self.secondimagefactiontype, pos = (-0.05, 0, 0.0),scale = 0.08)
            self.factionImage2.setTransparency(TransparencyAttrib.MAlpha)
            #change method and variable names
            self.mainRadioBtns2 = [
                DirectRadioButton(text = '', variable=self.va2, value=[0], scale=0.07, pos=(-0.8,0,-0.25), command=self.setcharselection2),
                DirectRadioButton(text = '', variable=self.va2, value=[1], scale=0.07, pos=(0,0,-0.25), command=self.setcharselection2)
                ]
            for mainbutton2 in self.mainRadioBtns2:
                mainbutton2.setOthers(self.mainRadioBtns2)
            
        elif(self.lengthdic>=3):
            self.greyImage1=OnscreenImage(image = self.thridimageforchartype, pos = (0.8, 0, 0.62),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = self.secondimageforchartype, pos = (-0.0, 0, 0.62),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = self.fristimageforchartype, pos = (-0.8, 0, 0.62),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
            
            self.name1 = OnscreenText(text = self.name11, pos = (-0.85, 0.2), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.name2 = OnscreenText(text = self.name22, pos = (0.0, 0.2), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.name3 = OnscreenText(text = self.name33, pos = (0.8, 0.2), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.factionImage1=OnscreenImage(image = self.fristimagefactiontype, pos = (-0.85, 0, 0.0),scale = 0.08)
            self.factionImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.factionImage2=OnscreenImage(image = self.secondimagefactiontype, pos = (-0.05, 0, 0.0),scale = 0.08)
            self.factionImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.factionImage3=OnscreenImage(image = self.thridimagefactiontype, pos = (0.75, 0, 0.0),scale = 0.08)
            self.factionImage3.setTransparency(TransparencyAttrib.MAlpha)
            #change method and variable names
            self.mainRadioBtns3 = [
                DirectRadioButton(text = '', variable=self.va3, value=[2], scale=0.07, pos=(-0.8,0,-0.25), command=self.setcharselection3),
                DirectRadioButton(text = '', variable=self.va3, value=[1], scale=0.07, pos=(0,0,-0.25), command=self.setcharselection3),
                DirectRadioButton(text = '', variable=self.va3, value=[0], scale=0.07, pos=(0.8,0,-0.25), command=self.setcharselection3)
                ]
            for mainbutton3 in self.mainRadioBtns3:
                mainbutton3.setOthers(self.mainRadioBtns3)
        else:
            self.greyImage1=OnscreenImage(image = Constants.IMG_GREY, pos = (0.6, 0, 0.62),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = Constants.IMG_GREY, pos = (-0.0, 0, 0.62),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = Constants.IMG_GREY, pos = (-0.6, 0, 0.62),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
        
        self.submitBtn = DirectButton(text = ("Play", "Play", "Play", "Play"), scale=.1, command=self.clickedSubmit, pos=(0.0, 0.0, -1.45))
        if(self.lengthdic >= 3):
            print "u have maximum characters"
            #self.createbtn = DirectButton(text = ("Create", "Create", "Create", "Create"), scale=.1, command=self.clickedCreate, pos=(0.4, 0.0, -1.45),state=DGG.DISABLED)
        else:
            self.createbtn = DirectButton(text = ("Create", "Create", "Create", "Create"), scale=.1, command=self.clickedCreate, pos=(0.4, 0.0, -1.45))
            self.createbtn.reparentTo(self.frame)
        self.cancelBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "Cancel"), scale=.1, command=self.clickedCancel, pos=(0.8, 0.0, -1.45))
        
        self.submitBtn.reparentTo(self.frame)
        
        self.cancelBtn.reparentTo(self.frame)
        
    def destroySelectionWindow(self):
        self.frame.destroy()
        self.greyImage1.destroy()
        self.greyImage2.destroy()
        self.greyImage3.destroy()
        self.name1.destroy()
        #self.name2.destroy()
        #self.name3.destroy()
        self.submitBtn.destroy()        
        self.cancelBtn.destroy()
        self.createbtn.destroy()
        
    def setcharselection1(self):
        self.finalchar = self.dicts1[0]
        self.finalname = self.dicts1[1]
        self.finaltype = self.dicts1[2]
        print ""
    def setcharselection2(self):
        if self.va2[0]:
            self.finalchar = self.dicts2[0]
            self.finalname = self.dicts2[1]
            self.finaltype = self.dicts2[2]
        else:
            self.finalchar = self.dicts1[0]
            self.finalname = self.dicts1[1]
            self.finaltype = self.dicts1[2]
        print ""
    def setcharselection3(self):
        if self.va3==[2]:
            self.finalchar = self.dicts1[0]
            self.finalname = self.dicts1[1]
            self.finaltype = self.dicts1[2]
        elif self.va3==[1]:
            self.finalchar = self.dicts2[0]
            self.finalname = self.dicts2[1]
            self.finaltype = self.dicts2[2]
        else:
            self.finalchar = self.dicts3[0]
            self.finalname = self.dicts3[1]
            self.finaltype = self.dicts3[2]
        print ""
    
    def clearselectCharacterTextbox(self):
        self.selectCharacterTextbox.enterText('')
        
    def getselectCharacterTextbox(self):
        self.selectCharacterTextbox = self.selectCharacterTextbox.get()
    
    def setselectCharacterTextbox(self, textEntered):
        print "name Of Char: ",textEntered
        self.selectCharacterTextbox = textEntered
        
    def clickedSubmit(self):
        print "you pressed play button and the game will start with character type : ",self.finalchar,"; character name :",self.finalname,"; and Faction :",self.finaltype
        #game starts from its base faction you have selected
    
    def clickedCreate(self):
        print "you pressed create button"
        self.destroySelectionWindow()
        self.createCreateCharWindow()
        
  
    def clickedCancel(self):
        print "You pressed Cancel"   
        self.l = login()
        self.l.createLogin()
        
