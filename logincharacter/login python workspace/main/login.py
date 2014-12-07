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

from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import Vec3,Vec4,BitMask32
from panda3d.core import TransparencyAttrib
from direct.gui.DirectGui import *
from panda3d.core import TextNode
from direct.task import Task

""" Custom Imports """
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager

class login:
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
    charFrame = DirectFrame()
    frame = DirectFrame()
    def __init__(self):
        __builtin__.main=self
        #self.loginEntry = []
        self.createLogin();
        self.dict = {} 
        try:
            self.cManager = ConnectionManager()
            self.startConnection()
        except Exception:
            self.error = True
        
    def createLogin(self):
        base.win.setClearColor(Vec4(0,0,0,1))
        self.imageObject = OnscreenImage(parent = render2d, image = 'images/mainPage.png', pos = (0,0,0), scale = (1.444, 1, 1.444))
        self.imageObject.setTransparency(TransparencyAttrib.MAlpha)
        self.createMainFrame()
        self.createText()
        self.createTextEntry()
        self.createButtons()
    def startConnection(self):
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True
    def createMainFrame(self):
        """Create the main base frame."""
        self.registerFrame = DirectFrame( frameSize = (-0.512, 0.512, -0.362, 0.362),
                                       frameColor = (0.53, 0.42, 0.18, 0.70),
                                       pos = (0, 0, -0.28) )

        self.mainBox = DirectFrame( frameSize = (-0.5, 0.5, -0.35, 0.35),
                                    frameColor = (0, 0, 0, 0.25),
                                    pos = (0, 0, 0) )
        self.mainBox.reparentTo(self.registerFrame)

        self.blackFrame = DirectFrame( frameSize = (-2, 2, -2, 2),
                                       frameColor = (0, 0, 0, 0.3),
                                       pos = (0, 0, 0),
                                       state = DGG.NORMAL )
        self.blackFrame.reparentTo(self.registerFrame, 1)
        self.blackFrame.hide()
    def createText(self):
        """Create some label for login text entry field"""
        self.headerLabel = DirectLabel(text='LOG IN',
                                       text_align=TextNode.ACenter,
                                       frameSize=(-0.2, 0.2, 0.2, 0.2),
                                       text_fg=(1,1,1,1),
                                       text_scale=0.07,
                                       frameColor=(0, 0, 0, 0),
                                       pos=(0, 0, 0.23))
        self.headerLabel.reparentTo(self.registerFrame)
        self.usernameLabel = DirectLabel(text='Username',
                                        text_align = TextNode.ARight,
                                         text_fg=(1,1,1,1),
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.19, 0, 0.067))
        self.usernameLabel.reparentTo(self.registerFrame)

        self.passwordLabel = DirectLabel(text='Password',
                                        text_align = TextNode.ARight,
                                         text_fg=(1,1,1,1),
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.19, 0, -0.070))
        self.passwordLabel.reparentTo(self.registerFrame)
    
    def createTextEntry(self):
        """Create entry boxes for credentials."""
        self.usernameEntry = DirectEntry(self.registerFrame,scale=0.055,
                                              pos=(-0.14, 0, 0.055),
                                              command=self.startSubmit,
                                              focus=1,
                                              focusInCommand=self.focus("username"),
                                              #focusInExtraArgs=[0],
                                              initialText="jeff",
                                              rolloverSound = None)
        self.usernameEntry.reparentTo(self.registerFrame)
        #self.loginEntry.append(self.usernameEntry)
        
        self.passwordEntry = DirectEntry(self.registerFrame,
                                              scale=0.055,
                                              pos=(-0.14, 0, -0.08),
                                              command=self.startSubmit,
                                              obscured=1,
                                              focusInCommand=self.focus("password"),
                                              #focusInExtraArgs=[1],
                                              rolloverSound = None)
        self.passwordEntry.reparentTo(self.registerFrame)
        #self.loginEntry.append(self.passwordEntry)
    def clearPassword(self):
        self.passwordEntry.enterText('')
    def startSubmit(self, message):
        self.submitLogin()

    def createButtons(self):
        """Create some buttons."""
        self.validateLoginFrame = DirectFrame( frameSize = (-0.131, 0.131, -0.056, 0.056),
                                               frameColor = (0.33, 0.42, 0.18, 0.95), # color of the login button
                                               pos = (-0.2, 0, -0.22) )
        self.validateLoginFrame.reparentTo(self.mainBox)

        self.validateLogin = DirectButton (text='Log In',
                                                 text_fg=(1, 1, 1, 1),
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.05,
                                                 frameSize=(-0.125, 0.125, -0.05, 0.05),
                                                 frameColor=(0, 0, 0, 0.2),
                                                 relief=DGG.FLAT,
                                                 pos=(0, 0, 0),
                                                 command=self.submitLogin,
                                                 clickSound = None,
                                                 rolloverSound = None)
        self.validateLogin.reparentTo(self.validateLoginFrame)

        self.registerButtonFrame = DirectFrame( frameSize = (-0.131, 0.131, -0.056, 0.056),
                                                frameColor = (1, 0, 1, 1), # color of the register button
                                                pos = (0.2, 0, -0.22) )
        self.registerButtonFrame.reparentTo(self.mainBox)

        self.registerButton = DirectButton(text='Register',
                                                 text_fg=(1, 1, 1, 1),
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.05,
                                                 frameSize=(-0.125, 0.125, -0.05, 0.05),
                                                 frameColor=(0, 0, 0, 0.2),
                                                 relief=DGG.FLAT,
                                                 pos=(0, 0, 0),
                                                 command=self.register,
                                                 clickSound = None,
                                                 rolloverSound = None)
        self.registerButton.reparentTo(self.registerButtonFrame)
    def focus(self, text):
        print text
    
    
        
    
    def submitLogin(self):
        print "Login"
        print "username: "+self.usernameEntry.get()
        print "password: "+self.passwordEntry.get()
        
        self.usernameInput = self.usernameEntry.get().strip()
        self.passwordInput = self.passwordEntry.get().strip()
        self.clearPassword()
        self.error = False
        try:
            #self.cManager = ConnectionManager()
            #self.startConnection()
            self.error = False
        except Exception:
            self.error = True
        if self.error is False:
            if(self.usernameInput is not "" and self.passwordInput is not ""):
                #c = characterSelection()
                self.dict = {}
                print "You pressed Submit", self.usernameInput, " ; ",self.passwordInput
                self.cManager.sendRequest(Constants.CMSG_AUTH, (self.usernameInput, self.passwordInput));
                self.mainUsername = self.usernameInput
                """ THiS IS WHERE IT STARTS TO GET WEIRD """
                #self.createSelectionWindow()
            else:
                print "Please enter in a username and password"
        else:
            print "Cannot connect to server."
    #def resume(self):
        #self.registerFrame.show()
    def register(self):
        """Switch to the registration screen."""
        
        self.registerFrame.hide()
        #R = Register(self.registerFrame)
        base.win.setClearColor(Vec4(0,0,0,1))
        self.imageObject = OnscreenImage(parent = render2d, image = 'images/mainPage.png', pos = (0,0,0), scale = (1.444, 1, 1.444))
        self.imageObject.setTransparency(TransparencyAttrib.MAlpha)
        self.createRMainFrame()
        self.createRText()
        self.createRTextEntry()
        self.createRButtons()
        self.error = False
        print "Register"
    def createRMainFrame(self):
        """Create the main base frame."""
        # frameColor is defined as (R,G,B,A)
        self.registerFrame = DirectFrame( frameSize = (-0.612, 0.612, -0.462, 0.462),
                                       frameColor = (0.53, 0.42, 0.18, 0.70),
                                       pos = (0, 0, -0.37) )

        self.mainBox = DirectFrame( frameSize = (-0.6, 0.6, -0.45, 0.45),
                                    frameColor = (0, 0, 0, 0.25),
                                    pos = (0, 0, 0) )
        self.mainBox.reparentTo(self.registerFrame)

        self.blackFrame = DirectFrame( frameSize = (-2, 2, -2, 2),
                                       frameColor = (0, 0, 0, 0.3),
                                       pos = (0, 0, 0),
                                       state = DGG.NORMAL )
        self.blackFrame.reparentTo(self.registerFrame, 1)
        self.blackFrame.hide()

    def createRText(self):
        """Create some label for login text entry field"""
        self.headerLabel = DirectLabel(text='REGISTER',
                                       text_align=TextNode.ACenter,
                                       frameSize=(-0.2, 0.2, 0.2, 0.2),
                                       text_fg=(1,1,1,1),
                                       text_scale=0.07,
                                       frameColor=(0, 0, 0, 0),
                                       pos=(0, 0, 0.28))
        self.headerLabel.reparentTo(self.registerFrame)
        self.usernameLabel = DirectLabel(text='Username',
                                        text_align = TextNode.ARight,
                                         text_fg=(1,1,1,1),
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.19, 0, 0.12))
        self.usernameLabel.reparentTo(self.registerFrame)

        self.passwordLabel = DirectLabel(text='Password',
                                        text_align = TextNode.ARight,
                                         text_fg=(1,1,1,1),
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.19, 0, -0.023))
        self.passwordLabel.reparentTo(self.registerFrame)

        self.rePasswordLabel = DirectLabel(text='Re-Password',
                                        text_align = TextNode.ARight,
                                         text_fg=(1,1,1,1),
                                         text_scale=0.06,
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.19, 0, -0.16))
        self.rePasswordLabel.reparentTo(self.registerFrame)

    def createRTextEntry(self):
        """Create entry boxes for credentials."""
        self.usernameEntry = DirectEntry(self.registerFrame,scale=0.055,
                                              pos=(-0.14, 0, 0.12),
                                              command=self.submitRRegister,
                                              focus=1,
                                              #focusInCommand=self.setFocus,
                                              focusInExtraArgs=[0],
                                              rolloverSound = None)
        self.usernameEntry.reparentTo(self.registerFrame)

        self.passwordEntry = DirectEntry(self.registerFrame,
                                              scale=0.055,
                                              pos=(-0.14, 0, -0.025),
                                              command=self.submitRRegister,
                                              obscured=1,
                                              #focusInCommand=self.setFocus,
                                              focusInExtraArgs=[1],
                                              rolloverSound = None)
        self.passwordEntry.reparentTo(self.registerFrame)

        self.rePasswordEntry = DirectEntry(self.registerFrame,
                                              scale=0.055,
                                              pos=(-0.14, 0, -0.165),
                                              command=self.submitRRegister,
                                              obscured=1,
                                              #focusInCommand=self.setFocus,
                                              focusInExtraArgs=[2],
                                              rolloverSound = None)
        self.rePasswordEntry.reparentTo(self.registerFrame)

    def createRButtons(self):
        """Create some buttons."""
        self.validateRegFrame = DirectFrame( frameSize = (-0.131, 0.131, -0.056, 0.056),
                                               frameColor = (0.33, 0.42, 0.18, 0.95), 
                                               pos = (-0.2, 0, -0.30) )
        self.validateRegFrame.reparentTo(self.mainBox)

        self.validateReg = DirectButton (text='Register',
                                                 text_fg=(1, 1, 1, 1),
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.05,
                                                 frameSize=(-0.125, 0.125, -0.05, 0.05),
                                                 frameColor=(0, 0, 0, 0.2),
                                                 relief=DGG.FLAT,
                                                 pos=(0, 0, 0),
                                                 command=self.submitRRegister,
                                                 clickSound = None,
                                                 rolloverSound = None)
        self.validateReg.reparentTo(self.validateRegFrame)

        self.registerButtonFrame = DirectFrame( frameSize = (-0.131, 0.131, -0.056, 0.056),
                                                frameColor = (0.33, 0.42, 0.18, 0.95), 
                                                pos = (0.2, 0, -0.30) )
        self.registerButtonFrame.reparentTo(self.mainBox)

        self.registerButton = DirectButton(text='Cancel',
                                                 text_fg=(1, 1, 1, 1),
                                                 text_pos=(0, -0.015),
                                                 text_scale=0.05,
                                                 frameSize=(-0.125, 0.125, -0.05, 0.05),
                                                 frameColor=(0, 0, 0, 0.2),
                                                 relief=DGG.FLAT,
                                                 pos=(0, 0, 0),
                                                 command=self.cancel,
                                                 clickSound = None,
                                                 rolloverSound = None)
        self.registerButton.reparentTo(self.registerButtonFrame)

    def submitRRegister(self):
        print "username: "+self.usernameEntry.get()
        print "password: "+self.passwordEntry.get()
        print "re-password: "+self.rePasswordEntry.get()
        self.registerUsername = self.usernameEntry.get().strip()
        self.registerPassword = self.passwordEntry.get().strip()
        self.registerCPassword = self.rePasswordEntry.get().strip()
        self.passwordEntry.enterText("")
        self.rePasswordEntry.enterText("")
        try:
            self.cManager = ConnectionManager()
            self.startConnection()
            print ""
        except Exception:
            self.error = True
        
        if self.error is False:
            if self.registerPassword == self.registerCPassword and self.registerPassword.strip() != "" and self.registerUsername.strip() != "":
                print "Success (",self.registerUsername, ", ",self.registerPassword,", ",self.registerCPassword,")"
                self.cManager.sendRequest(Constants.CMSG_REGISTER, (self.registerUsername, self.registerPassword))
                self.cancel()
            else:
                taskMgr.add(self.errorMessage, "destroyIncorrectUsername")
                self.message()
                print "Failed (",self.registerUsername, ", ",self.registerPassword,", ",self.registerCPassword,")"
        else:
            print "Cannot Connect to the Server"
    def errorMessage(self, task):
        if task.time < 5.0:
            return task.cont
        else:  
            self.failed.destroy()
            return task.done
        
    def message(self):
        self.failed = DirectLabel(text='Password needs to match',
                                       text_align=TextNode.ACenter,
                                       frameSize=(-0.2, 0.2, 0.2, 0.2),
                                       text_fg=(1,1,1,1),
                                       text_scale=0.07,
                                       frameColor=(255, 0, 0, 1),
                                       pos=(0, 0, 0.20))
        self.failed.reparentTo(self.registerFrame)
    def cancel(self):
        print "cancel"
        self.registerFrame.hide()
        self.createLogin()
        #self.l = login.resume()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #character Creation        
    def createCreateCharWindow(self):
        self.charFrame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                                frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                                pos=(-0.5, 0, 0.9))
        
        
            
        
        #print "print somethg:",self.some
        self.swordImage=OnscreenImage(image = Constants.IMG_SWORD, pos = (0.85, 0, -.3),scale = 0.15)
        self.swordImage.setTransparency(TransparencyAttrib.MAlpha)
        self.swordImage.reparentTo(self.charFrame)
        self.axeImage=OnscreenImage(image = Constants.IMG_AXE, pos = (0.45, 0, -0.3),scale = 0.15)
        self.axeImage.setTransparency(TransparencyAttrib.MAlpha)
        self.axeImage.reparentTo(self.charFrame)
        self.username = OnscreenText(text = self.username01, pos = (-1,.5), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.username.reparentTo(self.charFrame)
        
        self.charactertype = OnscreenText(text = "Character type :", pos = (-.1, -.55), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.charactertype.reparentTo(self.charFrame)
        self.buttons = [
        DirectRadioButton(text = '', variable=self.v, value=[0], scale=0.07, pos=(0.5,0,-.55), command=self.setText),
        DirectRadioButton(text = '', variable=self.v, value=[1], scale=0.07, pos=(0.9,0,-.55), command=self.setText)
        ]
        
        for button in self.buttons:
            button.setOthers(self.buttons)
            button.reparentTo(self.charFrame)
        self.nameOfChar = OnscreenText(text = "Name The Character :", pos = (-0.2, -0.75), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.nameOfChar.reparentTo(self.charFrame)    
        self.nameOfCharTextbox = DirectEntry(text = "" ,scale=.07,pos=(0.3,0, -.75),command=self.setnameOfChar,initialText="Anonymous", numLines = 1,focus=0,focusInCommand=self.clearnameOfChar, focusOutCommand=self.getnameOfChar)
        self.nameOfCharTextbox.reparentTo(self.charFrame)   
        
        self.factionSelection = OnscreenText(text = "Faction Selection :", pos = (-0.15, -1.0), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)
        self.factionSelection.reparentTo(self.charFrame)
        self.blueImage=OnscreenImage(image = Constants.IMG_BLUE, pos = (0.4, 0, -.9),scale = 0.08)
        self.blueImage.setTransparency(TransparencyAttrib.MAlpha) 
        self.blueImage.reparentTo(self.charFrame)
        self.redImage=OnscreenImage(image = Constants.IMG_RED, pos = (0.7, 0, -.9),scale = 0.08)
        self.redImage.reparentTo(self.charFrame)
        self.redImage.setTransparency(TransparencyAttrib.MAlpha)
        self.factionBtns = [
        DirectRadioButton(text = '', variable=self.v1, value=[0], scale=0.07, pos=(0.45,0,-1.1), command=self.setfaction),
        DirectRadioButton(text = '', variable=self.v1, value=[1], scale=0.07, pos=(0.75,0,-1.1), command=self.setfaction)
        ]
         
        for button1 in self.factionBtns:
            button1.setOthers(self.factionBtns)
            button1.reparentTo(self.charFrame)
        self.okForCreateBtn = DirectButton(text = ("Create", "Create", "Create", "disabled"), scale=.09, command=self.clickedOkForCreateBtn, pos=(0.2, 0.0, -1.3))
        self.cancelForCreateBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "disabled"), scale=.09, command=self.clickedCancelForCreateBtn, pos=(0.6, 0.0, -1.3))
        self.okForCreateBtn.reparentTo(self.charFrame)
        self.cancelForCreateBtn.reparentTo(self.charFrame)
        
    def destroyCreateCharWindow(self):
        #self.nameOfChar.destroy()
        #self.swordImage.destroy()
        #self.axeImage.destroy()
        #self.blueImage.destroy()
        #self.redImage.destroy()
        #self.nameOfChar.destroy()
        #self.nameOfCharTextbox.destroy()
        #self.factionSelection.destroy()
        #self.okForCreateBtn.destroy()
        #self.cancelForCreateBtn.destroy()
        #self.factionSelection.destroy()
        #self.frame.destroy()
        #self.factionBtns.destroy()
        #self.button.destory()
        self.charFrame.hide()
                                
    def mainresp(self,chartype,charname,charfact,cid):
        print "printed these",chartype,charname,charfact
        chardata="".join((chartype," ",charname," ",charfact, " ", str(cid)))
        if(self.lengthdic<=3):
            self.dict[self.lengthdic+1] = chardata  
        else:
            print "u can have only 3 character"
        self.clickedCancelForCreateBtn()
        #self.createSelectionWindow()
    def addChar(self):
        self.mainresp(self.chartitle, self.nameOfCharInput, self.factiontitle)
        self.clickedCancelForCreateBtn()
    def initializeChars(self, chars):
        #self.dict = {}
        print "number of chars: ", len(chars)
        self.lengthdic = len(self.dict)
        for x in chars:
            self.type = "sword"
            self.faction = "blue"
            self.cid = x[0]
            self.name = x[1]
            self.t1 = x[2]
            self.f1 = x[3]
            if self.t1 == 0:
                self.type = "axe"
            if self.f1 == 0:
                self.faction = "red"   
            chardata="".join((self.type," ",self.name," ",self.faction, " ", str(self.cid)))
            if(self.lengthdic<=3):
                self.dict[self.lengthdic+1] = chardata
                self.lengthdic = self.lengthdic + 1
            else:
                print "U CAN ONLY HAVE 3 CHAR"
        
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
        #self.cManager = ConnectionManager()
        #self.startConnection()
        if(self.chartitle == "axe"):
            self.type = 0
        else:
            self.type = 1
            
        if self.factiontitle == "blue":
            self.faction = 1
        else:
            self.faction = 0
        self.cManager.sendRequest(Constants.CMSG_CREATE_CHARACTER, (self.nameOfCharInput, self.type ,self.faction));
        #print "print somethg:",self.some
        
     
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
        self.registerFrame.hide()
        self.selFrame = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                                frameSize=(-3, 3, -3, 3),#(Left,Right,Bottom,Top)
                                pos=(-0.5, 0, 0.9))
        self.lengthdic = len(self.dict)
        print self.lengthdic
        if(self.lengthdic>3):
            del self.dict[4]
            self.lengthdic = len(self.dict)
            print "updated lenght : ",self.lengthdic 
            
        if(self.lengthdic == 0):
            print "lenght is zero no character"
        
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
            
        #print self.dicts1[0]
            
        if(self.lengthdic==1):
             #image = Constants.IMG_GREY
            self.greyImage1=OnscreenImage(image = Constants.IMG_GREY , pos = (1.35, 0, -0.45),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = Constants.IMG_GREY, pos = (0.55, 0, -0.45),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = self.fristimageforchartype, pos = (-0.25, 0, -0.45),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
            
            self.name1 = OnscreenText(text = self.name11, pos = (-0.25,-0.85), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.factionImage1=OnscreenImage(image = self.fristimagefactiontype, pos = (-0.25, 0, -1.0),scale = 0.08)
            self.factionImage1.setTransparency(TransparencyAttrib.MAlpha) 
            self.factionImage1.reparentTo(self.selFrame)
            self.name1.reparentTo(self.selFrame)
            #change method and variable names
            self.mainRadioBtns1 = [
                DirectRadioButton(text = '', variable=self.va1, value=[0], scale=0.07, pos=(-0.2,0,-1.2), command=self.setcharselection1)
                ]
            for mainbutton1 in self.mainRadioBtns1:
                mainbutton1.setOthers(self.mainRadioBtns1)
                mainbutton1.reparentTo(self.selFrame)
            
        elif(self.lengthdic==2):
            #image = Constants.IMG_GREY
            self.greyImage1=OnscreenImage(image = Constants.IMG_GREY, pos = (1.35, 0, -0.45),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = self.secondimageforchartype, pos = (0.55, 0, -0.45),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = self.fristimageforchartype, pos = (-0.25, 0, -0.45),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
            
            self.name1 = OnscreenText(text = self.name11, pos = (-0.25,-0.85), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.name2 = OnscreenText(text = self.name22, pos = (0.55, -0.85), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            
            self.factionImage1=OnscreenImage(image = self.fristimagefactiontype, pos = (-0.25, 0, -1.0),scale = 0.08)
            self.factionImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.factionImage1.reparentTo(self.selFrame)
            self.name1.reparentTo(self.selFrame)
            self.name2.reparentTo(self.selFrame)
            self.factionImage2=OnscreenImage(image = self.secondimagefactiontype, pos = (0.55, 0, -1.0),scale = 0.08)
            self.factionImage2.setTransparency(TransparencyAttrib.MAlpha)
            
            self.factionImage1.reparentTo(self.selFrame)
            self.factionImage2.reparentTo(self.selFrame)
            #change method and variable names
            self.mainRadioBtns2 = [
                DirectRadioButton(text = '', variable=self.va2, value=[0], scale=0.07, pos=(-0.2,0,-1.2), command=self.setcharselection2),
                DirectRadioButton(text = '', variable=self.va2, value=[1], scale=0.07, pos=(0.6,0,-1.2), command=self.setcharselection2)
                ]
            for mainbutton2 in self.mainRadioBtns2:
                mainbutton2.setOthers(self.mainRadioBtns2)
                mainbutton2.reparentTo(self.selFrame)
            
        elif(self.lengthdic>=3):
            self.greyImage1=OnscreenImage(image = self.thridimageforchartype, pos = (1.35, 0, -0.45),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = self.secondimageforchartype, pos =  (0.55, 0, -0.45),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = self.fristimageforchartype, pos = (-0.25, 0, -0.45),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
            
            self.name1 = OnscreenText(text = self.name11, pos =  (-0.25,-0.85), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.name2 = OnscreenText(text = self.name22, pos = (0.55, -0.85), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.name3 = OnscreenText(text = self.name33, pos = (1.35, -0.85), scale = 0.08,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
            self.name1.reparentTo(self.selFrame)
            self.name2.reparentTo(self.selFrame)
            self.name3.reparentTo(self.selFrame)
            self.factionImage1=OnscreenImage(image = self.fristimagefactiontype, pos = (-0.25, 0, -1.0),scale = 0.08)
            self.factionImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.factionImage2=OnscreenImage(image = self.secondimagefactiontype, pos = (0.55, 0, -1.0),scale = 0.08)
            self.factionImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.factionImage3=OnscreenImage(image = self.thridimagefactiontype, pos = (1.35, 0, -1.0),scale = 0.08)
            self.factionImage3.setTransparency(TransparencyAttrib.MAlpha)
            self.factionImage1.reparentTo(self.selFrame)
            self.factionImage2.reparentTo(self.selFrame)
            self.factionImage3.reparentTo(self.selFrame)
            #change method and variable names
            self.mainRadioBtns3 = [
                DirectRadioButton(text = '', variable=self.va3, value=[2], scale=0.07, pos=(-0.2,0,-1.2), command=self.setcharselection3),
                DirectRadioButton(text = '', variable=self.va3, value=[1], scale=0.07, pos=(0.6,0,-1.2), command=self.setcharselection3),
                DirectRadioButton(text = '', variable=self.va3, value=[0], scale=0.07, pos=(1.4,0,-1.2), command=self.setcharselection3)
                ]
            for mainbutton3 in self.mainRadioBtns3:
                mainbutton3.setOthers(self.mainRadioBtns3)
                mainbutton3.reparentTo(self.selFrame)
        else:
            self.greyImage1=OnscreenImage(image = Constants.IMG_GREY, pos = (1.35, 0, -0.45),scale = 0.2)
            self.greyImage1.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage2=OnscreenImage(image = Constants.IMG_GREY, pos = (0.55, 0, -0.45),scale = 0.2)
            self.greyImage2.setTransparency(TransparencyAttrib.MAlpha)
            self.greyImage3=OnscreenImage(image = Constants.IMG_GREY, pos = (-0.25, 0, -0.45),scale = 0.2)
            self.greyImage3.setTransparency(TransparencyAttrib.MAlpha)
        
        self.submitBtn = DirectButton(text = ("PLAY", "PLAY", "PLAY", "PLAY"), scale=.1, command=self.clickedSubmit, pos=(0.1, 0.0, -1.45))
        if(self.lengthdic >= 3):
            print "u have maximum characters"
            #self.createbtn = DirectButton(text = ("Create", "Create", "Create", "Create"), scale=.1, command=self.clickedCreate, pos=(0.4, 0.0, -1.45),state=DGG.DISABLED)
        else:
            self.createbtn = DirectButton(text = ("CREATE", "CREATE", "CREATE", "CREATE"), scale=.1, command=self.clickedCreate, pos=(0.5, 0.0, -1.45))
            self.createbtn.reparentTo(self.selFrame)
        
        self.cancelBtn =  DirectButton(text = ("CANCEL", "CANCEL", "CANCEL", "CANCEL"), scale=.1, command=self.clickedCancel, pos=(0.97, 0.0, -1.45))
        
        self.submitBtn.reparentTo(self.selFrame)
        
        self.cancelBtn.reparentTo(self.selFrame)
        
        self.greyImage1.reparentTo(self.selFrame)
        self.greyImage2.reparentTo(self.selFrame)
        self.greyImage3.reparentTo(self.selFrame)
    def destroySelectionWindow(self):
        #self.frame.destroy()
        #self.greyImage1.destroy()
        #self.greyImage2.destroy()
        #self.greyImage3.destroy()
        #self.name1.destroy()
        #self.name2.destroy()
        #self.name3.destroy()
        #self.submitBtn.destroy()        
        #self.cancelBtn.destroy()
        #self.createbtn.destroy()
        self.selFrame.hide()
    
    def clickedCancel(self):
        print "You pressed Cancel"
        self.destroySelectionWindow()
        #self.destroyCreateCharWindow()
        self.registerFrame.show()
        self.clearPassword()
        
    def setcharselection1(self):
        self.finalchar = self.dicts1[0]
        self.finalname = self.dicts1[1]
        self.finaltype = self.dicts1[2]
        self.finalcid = self.dicts1[3]
        print ""
    def setcharselection2(self):
        if self.va2[0]:
            self.finalchar = self.dicts2[0]
            self.finalname = self.dicts2[1]
            self.finaltype = self.dicts2[2]
            self.finalcid = self.dicts2[3]
        else:
            self.finalchar = self.dicts1[0]
            self.finalname = self.dicts1[1]
            self.finaltype = self.dicts1[2]
            self.finalcid = self.dicts1[3]
        print ""
    def setcharselection3(self):
        if self.va3==[2]:
            self.finalchar = self.dicts1[0]
            self.finalname = self.dicts1[1]
            self.finaltype = self.dicts1[2]
            self.finalcid = self.dicts1[3]
        elif self.va3==[1]:
            self.finalchar = self.dicts2[0]
            self.finalname = self.dicts2[1]
            self.finaltype = self.dicts2[2]
            self.finalcid = self.dicts2[3]
        else:
            self.finalchar = self.dicts3[0]
            self.finalname = self.dicts3[1]
            self.finaltype = self.dicts3[2]
            self.finalcid = self.dicts3[3]
        print ""
    
    def clearselectCharacterTextbox(self):
        self.selectCharacterTextbox.enterText('')
        
    def getselectCharacterTextbox(self):
        self.selectCharacterTextbox = self.selectCharacterTextbox.get()
    
    def setselectCharacterTextbox(self, textEntered):
        print "name Of Char: ",textEntered
        self.selectCharacterTextbox = textEntered
        
    def clickedSubmit(self):
        print "you pressed play button and the game will start with cid: ", self.finalcid, "; character type : ",self.finalchar,"; character name :",self.finalname,"; and Faction :",self.finaltype
        #game starts from its base faction you have selected
        self.tempType = 0
        self.tempFact = 0
        if self.finalname == "sword":
            self.tempType = 1
        if self.finaltype == "blue":
            self.tempFact = 1
        if self.startConnection():
            self.cManager.sendRequest(Constants.CMSG_SELECT_CHARACTER, (self.mainUsername, self.finalname, self.finalcid, self.tempType, self.tempFact));
        else:
            self.cManager = ConnectionManager()
            self.startConnection()
            self.cManager.sendRequest(Constants.CMSG_SELECT_CHARACTER, (self.mainUsername, self.finalname, self.finalcid, self.tempType, self.tempFact));
    def clickedCreate(self):
        print "you pressed create button"
        self.destroySelectionWindow()
        self.createCreateCharWindow()

    