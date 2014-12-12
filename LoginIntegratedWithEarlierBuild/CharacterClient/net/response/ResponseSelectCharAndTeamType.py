from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from main.selectcharandteamtype import selectcharandteamtype

class ResponseSelectCharAndTeamType(ServerResponse):

    def execute(self, data):
            
        try:
            
            #self.type=data.getString()
            #self.name=data.getString()
            #self.func=data.getString()
            #responsedata = self.type," ",self.name," ",self.func
            #main.mainresp(self.type,self.name,self.func)
            self.status = data.getInt32()
            if self.status == 1:
                self.count = data.getInt32()
                self.name = data.getString()
                self.cid = data.getInt32()
                self.type = data.getInt32()
                self.faction = data.getInt32()
                self.tempType = "sword"
                if(self.type == 0):
                    self.tempType = "axe"
                self.tempFaction = "blue"
                if self.faction == 0:
                    self.tempFaction = "red"
                main.login.mainresp(self.tempType, self.name, self.tempFaction, self.cid)
                #main.addChar()
                print ""
            else:
                print "ERROR CREATING CHARACTER"
            print "COOOOOOODDDDDEEEEEE: " + str(self.status)
            #print "Response Create Character - ",self.type,self.name,self.func
            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')
        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()

     