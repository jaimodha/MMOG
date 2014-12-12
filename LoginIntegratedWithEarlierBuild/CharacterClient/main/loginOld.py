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
from panda3d.core import Vec4
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.interval.IntervalGlobal import Sequence

from main.characterSelection import *
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager


class loginOld():
    TEXT_COLOR = (1,1,1,1)
    TEXT_COLOR_WHITE = (255, 255, 255, 1)
    TEXT_SCALE = 0.07
    FONT_TYPE_01 = 0
    TEXT_SHADOW_COLOR = (0,0,0,0.5)
    usernameInput = ""
    passwordInput = ""
    frame = DirectFrame()
    username = OnscreenText()
    password = OnscreenText()
    cpassword = OnscreenText()
    failed = OnscreenText()
    userTextbox = DirectEntry()
    passTextbox = DirectEntry()
    submitBtn = DirectButton()
    registerBtn = DirectButton()
    cancelBtn = DirectButton()
    
    
    registerUsername = ""
    registerPassword = ""
    registerCPassword = ""
    
    regInputUser = DirectEntry()
    regInputPass = DirectEntry()
    regInputCPass = DirectEntry()
    
    regRegisterBtn = DirectButton()
    regCancelBtn = DirectButton()
    
    def __init__(self):
        print 'Loading Login...'
        self.error = False
        self.status = "NotAuthorized";
            
    def createLogo(self):
        base.win.setClearColor(Vec4(0,0,0,1))
        
        self.main = DirectFrame(frameColor=(0, 0, 0, 1), #(R,G,B,A)
                            frameSize=(-2, 2, -2, 2),#(Left,Right,Bottom,Top)
                            pos=(0, 0, 0))
        self.logo = OnscreenImage(image = 'logo.png', pos = (0, 1.4, .6), scale=(0.75, .5, .4))
        self.logo.reparentTo(self.main)
    def startConnection(self):
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True
    def getStatus(self):
        return self.status
    def clearPassText(self):
        self.passTextbox.enterText('')
    def clearUserText(self):
        self.userTextbox.enterText('')
    def getUserText(self):
        self.usernameInput = self.userTextbox.get()
    def getPassText(self):
        self.passwordInput = self.passTextbox.get()
    def setUserText(self, textEntered):
        #print "username: ",textEntered
        self.usernameInput = textEntered
    def setPassText(self, textEntered):
        #print "password: ",textEntered
        self.passwordInput = textEntered
        self.clickedSubmit()
    def clickedSubmit(self):
        self.usernameInput = self.userTextbox.get().strip()
        self.passwordInput = self.passTextbox.get().strip()
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
            else:
                print "Please enter in a username and password"
        else:
            print "Cannot connect to server."
    def clickedCancel(self):
        print "You pressed Cancel"
        exit()
    def clickedRegister(self):
        print "You pressed Register"
        self.createRegisterWindow()
    def clickedRegRegister(self):
        self.registerUsername = self.regInputUser.get()
        self.registerPassword = self.regInputPass.get()
        self.registerCPassword = self.regInputCPass.get()
        self.error = False
        try:
            self.cManager = ConnectionManager()
            self.startConnection()
        except Exception:
            self.error = True
            
        if self.error is False:
            if self.registerPassword == self.registerCPassword and self.registerPassword.strip() != "" and self.registerUsername.strip() != "":
                print "Success (",self.registerUsername, ", ",self.registerPassword,", ",self.registerCPassword,")"
                self.cManager.sendRequest(Constants.CMSG_REGISTER, (self.registerUsername, self.registerPassword))
                self.clickedRegCancel()
            else:
                self.failed = OnscreenText(text="Your password does not match Confirm Password.", pos=(0, -.7), scale=0.06,fg=Constants.TEXT_ERROR_COLOR, align=TextNode.ACenter,mayChange=0)
                self.failed.reparentTo(self.frame)
                print "Failed (",self.registerUsername, ", ",self.registerPassword,", ",self.registerCPassword,")"
        else:
            print "Cannot Connect to the Server"
    def clickedRegCancel(self):
        self.destroyRegisterWindow()
        self.createLoginWindow()
    def destroyLoginWindow(self):
        self.frame.destroy()
        self.username.destroy()
        self.password.destroy()
        self.userTextbox.destroy()
        self.passTextbox.destroy()
        self.submitBtn.destroy()
        self.registerBtn.destroy()
        self.cancelBtn.destroy()
    def destroyRegisterWindow(self):
        self.frame.destroy()
        self.username.destroy()
        self.password.destroy()
        self.cpassword.destroy()
        self.regInputUser.destroy()
        self.regInputPass.destroy()
        self.regInputCPass.destroy()
        self.cancelBtn.destroy()
        self.registerBtn.destroy()
        self.failed.destroy();
    def throwIncorrectUsername(self):
        self.incorrectUsername = OnscreenText(text="Incorrect Username/Password", pos=(0, -.5), scale=0.05, fg=(1,0.5,0.5,1), mayChange=0)
    def throwServerError(self):
        self.incorrectUsername = OnscreenText(text="Unable to Connect to Server", pos=(0, -.5), scale=0.05, fg=(1,0.5,0.5,1), mayChange=0)
    def createLoginWindow(self):
        self.frame = DirectFrame(frameColor=(255, 255, 255, 0.5), #(R,G,B,A)
                                frameSize=(-1, 1, -1, 0.0),#(Left,Right,Bottom,Top)
                                pos=(0, 0, 0.25))
        self.frame.reparentTo(self.main)
        self.loginTitle = OnscreenText(text = "Login", pos = (0,-0.2), scale=0.1, fg=(1,0.5,0.5,1), align=TextNode.ACenter, mayChange=0)
        self.username = OnscreenText(text = "username:", pos = (-0.1, -0.4), scale = 0.07,fg=self.TEXT_COLOR_WHITE,align=TextNode.ACenter,mayChange=0)
        self.password = OnscreenText(text="password: ", pos = (-0.1, -0.6), scale=0.07, fg=self.TEXT_COLOR_WHITE, align=TextNode.ACenter, mayChange=0)
        self.loginTitle.reparentTo(self.frame)
        self.username.reparentTo(self.frame)
        self.password.reparentTo(self.frame)
        self.userTextbox = DirectEntry(text = "" ,scale=.05,pos=(.1,0, -0.4), command=self.setUserText, numLines = 1,focus=1,focusInCommand=self.clearUserText, focusOutCommand=self.getUserText)
        self.passTextbox = DirectEntry(text = "" ,scale=.05,pos=(.1,0, -0.6), obscured=1, command=self.setPassText, numLines = 1,focus=0,focusInCommand=self.clearPassText, focusOutCommand=self.getPassText)
        self.userTextbox.reparentTo(self.frame)
        self.passTextbox.reparentTo(self.frame)
        self.submitBtn = DirectButton(text = ("Submit", "Login", "Submit", "disabled"), scale=.08, command=self.clickedSubmit, pos=(0.8, 0.0, -0.90))
        self.registerBtn =  DirectButton(text = ("Register", "Register", "Register", "disabled"), scale=.075, command=self.clickedRegister, pos=(0.5, 0.0, -0.90))
        self.cancelBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "disabled"), scale=.08, command=self.clickedCancel, pos=(0.2, 0.0, -0.90))
        self.submitBtn.reparentTo(self.frame)
        self.cancelBtn.reparentTo(self.frame)
        self.registerBtn.reparentTo(self.frame)
    def createRegisterWindow(self):
        self.createLogo()
        self.frame = DirectFrame(frameColor=(100, 100, 100, .5), #(R,G,B,A)
                                frameSize=(-1, 1, -1, 0.0),#(Left,Right,Bottom,Top)
                                pos=(0, 0, 0.25))
        self.frame.reparentTo(self.main)
        self.registerTitle = OnscreenText(text = "Register", pos = (0,-0.2), scale=0.1, fg=(1,0.5,0.5,1), align=TextNode.ACenter, mayChange=0)
        self.username = OnscreenText(text = "Username:", pos = (-0.1, -.4), scale = 0.07,fg=self.TEXT_COLOR_WHITE,align=TextNode.ACenter,mayChange=0)
        self.password = OnscreenText(text="Password: ", pos = (-0.1, -0.5), scale=0.07, fg=self.TEXT_COLOR_WHITE, align=TextNode.ACenter, mayChange=0)
        self.cpassword = OnscreenText(text="Confirm Password: ", pos = (-0.25, -0.6), scale=0.07, fg=self.TEXT_COLOR_WHITE, align=TextNode.ACenter, mayChange=0)
        self.registerTitle.reparentTo(self.frame)
        self.username.reparentTo(self.frame)
        self.password.reparentTo(self.frame)
        self.cpassword.reparentTo(self.frame)
        self.regInputUser = DirectEntry(text = "" ,scale=.05,pos=(.1,0,-.4), command=self.setUserText,initialText="", numLines = 1,focus=1,focusInCommand=self.clearUserText, focusOutCommand=self.getUserText)
        self.regInputPass = DirectEntry(text = "" ,scale=.05,pos=(.1,0, -.5),obscured=1,command=self.setPassText,initialText="", numLines = 1,focus=0,focusInCommand=self.clearPassText, focusOutCommand=self.getPassText)
        self.regInputCPass = DirectEntry(text = "" ,scale=.05,pos=(.1,0, -.6),obscured=1,command=self.setPassText,initialText="", numLines = 1,focus=0,focusInCommand=self.clearPassText, focusOutCommand=self.getPassText)
        self.regInputUser.reparentTo(self.frame)
        self.regInputPass.reparentTo(self.frame)
        self.regInputCPass.reparentTo(self.frame)
        self.registerBtn =  DirectButton(text = ("Register", "Register", "Register", "disabled"), scale=.075, command=self.clickedRegRegister, pos=(0.8, 0.0, -0.90))
        self.cancelBtn =  DirectButton(text = ("Cancel", "Cancel", "Cancel", "disabled"), scale=.08, command=self.clickedRegCancel, pos=(0.5, 0.0, -0.90))
        self.cancelBtn.reparentTo(self.frame)
        self.registerBtn.reparentTo(self.frame)
