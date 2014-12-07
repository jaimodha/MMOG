from traceback import print_exc

from common.Constants import Constants
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from net.response.ServerResponse import ServerResponse

#from main.selectcharandteamtype import selectcharandteamtype
#from main.login2 import login
#from net.ConnectionManager import ConnectionManager

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            self.allChars = []
            self.status = data.getInt32()
            self.characters = data.getInt32()
            #self.characters = 0
            print "NUMBER OF CHARACTERS = ",self.characters
            if self.characters > 0:
                for x in range(0, self.characters):
                    #self.username = data.getString()
                    #print "Username: " + self.username
                    self.name = data.getString()
                    print "Charname: "+ self.name
                    self.cid = data.getInt32()
                    print "C_id: ", self.cid
                    self.type = data.getInt32()
                    print "CharType: ", self.type
                    self.faction = data.getInt32()
                    print "CharFaction: ", self.faction
                    self.allChars.append((self.cid, self.name, self.type, self.faction))
            #self.username = data.getString()
            print "ResponseLogin - ", self.status
            
            if(self.status == 1):
                print "logged In!"
                if self.characters > 0:
                    main.initializeChars(self.allChars)
                else:
                    main.createSelectionWindow()
            elif self.status == 0:
                print "incorrect username/password"
                #self.l = login2()
                #self.l.throwIncorrectUsername()
                taskMgr.add(self.destroyIncorrectUsername, "destroyIncorrectUsername")
                self.throwIncorrectUsername()
                #c = selectcharandteamtype()
            else:
                print "there was a problem with the server"
                taskMgr.add(self.destroyServerError, "destroyServerError")
                self.throwServerError()
               # c = selectcharandteamtype()

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(self.status) + '] Login Response')
            print_exc()
    def throwIncorrectUsername(self):
        self.incorrectUsername = OnscreenText(text="Incorrect Username/Password", 
                                    pos=(0, -0.1), scale=0.05, fg=Constants.TEXT_ERROR_COLOR, mayChange=0)
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
        
            