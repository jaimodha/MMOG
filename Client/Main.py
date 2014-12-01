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

from main.login import *
from main.characterSelection import *

""" Custom Imports """
# import your modules
from main.login import login
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager

class Main(DirectObject):

    def __init__(self):
        
	    # Network Setup
        self.cManager = ConnectionManager()
        self.startConnection()
        print "Ran Main2"
        #taskMgr.add(self.menu, "Menu")
        self.login = login()
        self.login.createLogo()
        self.login.createLoginWindow()
        print "Finished"
    def startConnection(self):
        """Create a connection to the remote host.

        If a connection cannot be created, it will ask the user to perform
        additional retries.

        """
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False

        return True
    
    def menu(self, task):
        # Accept raw_input choice
        self.login = login()
        if self.login.getStatus() == "Authorized":
            print "going to character Select Menu"
            return task.done
        
        return task.again

m = Main()
run()
