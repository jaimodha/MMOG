# Don't display a window
from panda3d.core import loadPrcFileData
loadPrcFileData ("", "window-type none")

from direct.directbase.DirectStart import *
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math

from BasicControlPoint import *

from common.Constants import Constants
from net.ConnectionManager import ConnectionManager
import __builtin__

SPEED = 0.5

class World(DirectObject):

    def __init__(self):
        __builtin__.main = self
        self.taskMgr = taskMgr
        self.base = base
        
        # Connect to the server
        self.cManager = ConnectionManager()
        self.startConnection()
    
        self.characters = dict()
        self.cpList = dict()
        
        # Login as 'CPHandler'
        # Temporary workaround, can add a seperate request/response for client/NPC client logins later
        self.username = "CPHandler"
        type = 0
        factionId = 0
        self.cManager.sendRequest(Constants.CMSG_AUTH, [self.username, type, factionId])

        # Create control points
        self.cpList[1] = BasicControlPoint(1, -23.1, -137.9, 0, 10, RED)
        self.cpList[2] = BasicControlPoint(2, 110.6, -255.6, 0, 10, RED)
        self.cpList[3] = BasicControlPoint(3, 7.7, -14.8, 0, 10, RED)
        self.cpList[4] = BasicControlPoint(4, -1.1, 134.3, 0, 10, BLUE)
        self.cpList[5] = BasicControlPoint(5, 94.1, 197.3, 0, 10, BLUE)

        taskMgr.doMethodLater(0.1, self.refresh, "heartbeat")
        taskMgr.doMethodLater(1, self.CPHandler, 'CPHandler')
        
    def startConnection(self):
        if self.cManager.connection == None:
            if not self.cManager.startConnection():
                return False
        return True
        
    def refresh(self,task):
        self.cManager.sendRequest(Constants.REQ_HEARTBEAT)
        return task.again
        
    def CPHandler(self, task):
        for cp in self.cpList.values():
            if cp.factionId == RED:
                if cp.checkContested(self.characters):
                    print("CP [", cp.id, "] is contested")
                elif cp.checkBluePresence(self.characters):
                    cp.timer -= 1
                    print(cp.id, cp.timer)

                    if cp.timer == 0:
                        print("CP [", cp.id, "] taken by Blue")
                        cp.factionId = BLUE
                else:
                    cp.timer = 30
                    
            elif cp.factionId == BLUE:
                if cp.checkContested(self.characters):
                    print("CP [", cp.id, "] contested")
                elif cp.checkRedPresence(self.characters):
                    cp.timer += 1
                    print(cp.id, cp.timer)

                    if cp.timer == 30:
                        print("CP [", cp.id, "] taken by Red")
                        cp.factionId = RED
                else:
                    cp.timer = 0
            
            # Send 'timer' to server, which send to all clients
            self.cManager.sendRequest(Constants.CMSG_CONTROL_POINT_STATE, [cp.id, cp.timer, cp.factionId])

        return task.again;

w = World()
run()

