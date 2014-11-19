from traceback import print_exc

from common.Constants import Constants
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectGui import *
from direct.task import Task
from net.response.ServerResponse import ServerResponse

from main.login import *

class ResponseRegister(ServerResponse):

    def execute(self, data):
        try:
            self.status = data.getString()
            print "ResponseRegister - ", self.status
            
            if(self.status == "Success"):
                
                print "Created Successfully!"
            elif self.status == "Same Username":
                print "Already have that username"
                #self.l = login2()
                #self.l.throwIncorrectUsername()
                taskMgr.add(self.destroyIncorrectUsername, "destroyIncorrectUsername")
                self.throwIncorrectUsername()
            else:
                print "there was a problem with the server"
                taskMgr.add(self.destroyServerError, "destroyServerError")
                self.throwServerError()

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(self.status) + '] Register Response')
            print_exc()
    def throwIncorrectUsername(self):
        self.incorrectUsername = OnscreenText(text="Already have that username", 
                                pos=(0, -.5), scale=0.05, fg=Constants.TEXT_ERROR_COLOR, mayChange=0)
    def throwServerError(self):
        self.serverError = OnscreenText(text="Unable to Connect to Server",
                                pos=(0, -.5), scale=0.05, fg=Constants.TEXT_ERROR_COLOR, mayChange=0)
    def destroyIncorrectUsername(self, task):
        if task.time < 5.0:
            return task.cont
        else:  
            self.incorrectUsername.destroy()
            return task.done
    def destroyServerError(self, task):
        if task.time < 5.0:
            return task.cont
        else:  
            self.serverError.destroy()
            return task.done    
    
