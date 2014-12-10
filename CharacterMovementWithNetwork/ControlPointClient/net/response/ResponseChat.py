from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChat(ServerResponse):

    def execute(self, data):
        try:
            self.userName = data.getString()
            self.message = data.getString()

        except:
            self.log('Bad [' + str(Constants.SMSG_CHAT) + '] Chat Response')
            print_exc()
