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
# import your modules

#from main.Register import *
from main.selectcharandteamtype import selectcharandteamtype
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager

class login:

    def __init__(self):
        
        #self.loginEntry = []
        self.createLogin();
        
    
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
                                              command=self.submitLogin,
                                              focus=1,
                                              focusInCommand=self.focus("username"),
                                              #focusInExtraArgs=[0],
                                              rolloverSound = None)
        self.usernameEntry.reparentTo(self.registerFrame)
        #self.loginEntry.append(self.usernameEntry)
        
        self.passwordEntry = DirectEntry(self.registerFrame,
                                              scale=0.055,
                                              pos=(-0.14, 0, -0.08),
                                              command=self.submitLogin,
                                              obscured=1,
                                              focusInCommand=self.focus("password"),
                                              #focusInExtraArgs=[1],
                                              rolloverSound = None)
        self.passwordEntry.reparentTo(self.registerFrame)
        #self.loginEntry.append(self.passwordEntry)

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
    def clickedCancel(self):
        print "You pressed Cancel"
        exit()
    def submitLogin(self):
        print "Login"
        print "username: "+self.usernameEntry.get()
        print "password: "+self.passwordEntry.get()
        self.usernameInput = self.usernameEntry.get().strip()
        self.passwordInput = self.passwordEntry.get().strip()
        self.error = False
        try:
            self.cManager = ConnectionManager()
            self.startConnection()
        except Exception:
            self.error = True
        if self.error is False:
            if(self.usernameInput is not "" and self.passwordInput is not ""):
                #c = characterSelection()
                print "You pressed Submit", self.usernameInput, " ; ",self.passwordInput
                self.cManager.sendRequest(Constants.CMSG_AUTH, (self.usernameInput, self.passwordInput));
                """ THiS IS WHERE IT STARTS TO GET WEIRD """
                #self.registerFrame.hide()
                #c = selectcharandteamtype(self.registerFrame)
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
        try:
            self.cManager = ConnectionManager()
            self.startConnection()
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

    
