from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRandomString(ServerResponse):

    def execute(self, data):

        try:
            
            self.userName = data.getString()
            self.factionId = data.getInt32()
            self.password = data.getString()
            main.userName = self.userName
            print "ResponseRandomString_dummyLogin - ", self.userName
            print "ResponseRandomString_dummyLogin ", self.password
            print "ResponseRandomString_dummyLogin", self.factionId
            
            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
