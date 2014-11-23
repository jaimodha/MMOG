from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChat(ServerResponse):

    def execute(self, data):
        try:
            self.userName = data.getString()
            self.message = data.getString()
            
            #send this message and username to the medthod
            main.putToChatQ(self.userName,self.message)
           
            #self.log('Received [' + str(Constants.RAND_INT) + '] Int Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CHAT) + '] Chat Response')
            print_exc()
