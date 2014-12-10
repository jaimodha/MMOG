from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCharacterChangeHealth(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.healthChange = data.getInt32() #healthChange assumed to be damage so healing is negative

        except:
            self.log('Bad [' + str(Constants.SMSG_ATTACK) + '] Attack Response')
            print_exc()
