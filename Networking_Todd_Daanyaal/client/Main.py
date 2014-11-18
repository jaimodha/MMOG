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

""" Custom Imports """
# import your modules
from common.Constants import Constants
from net.ConnectionManager import ConnectionManager

class Main(DirectObject):

    def __init__(self):
        
	    # Network Setup
        self.cManager = ConnectionManager()
        self.startConnection()
        
        taskMgr.add(self.menu, "Menu")

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
        choice = input("1 - Rand int\n2 - Rand string\n3 - Rand short\n4 - Rand float\n101 - login\n6 - Exit\n")
        
        msg = 0
        username = 0
        password = 0
        
        if choice is 1: msg = random.randint(-(2**16), 2**16 - 1)
        elif choice is 2: msg = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(7))
        elif choice is 3: msg = random.randint(0, 2**16 - 1)
        elif choice is 4: msg = 100 * random.random()
        elif choice is 101: 
        	username = "user"
        	password = "pass"
        elif choice is 6: sys.exit()
        else: print "Invalid input"
        
        if choice is 101:
        	self.cManager.sendRequest(choice, username+" "+password)
        else:
        	self.cManager.sendRequest(choice, msg);
        
        return task.again

m = Main()
run()
