from traceback import print_exc

from common.Constants import Constants
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from net.response.ServerResponse import ServerResponse

from main.selectcharandteamtype import *
#from login import *
#from main.characterSelection import characterSelection
#from net.ConnectionManager import ConnectionManager

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getInt()
            #self.username = data.getString()
            print "ResponseLogin - ", self.status
            
            if(self.status == 1):
                print "logged In!"
                c = selectcharandteamtype()
            elif self.status == 0:
                print "incorrect username/password"
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
            self.log('Bad [' + str(self.status) + '] Login Response')
            print_exc()
    def throwIncorrectUsername(self):
        self.incorrectUsername = OnscreenText(text="Incorrect Username/Password", 
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
        
            
