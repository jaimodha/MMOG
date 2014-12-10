from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCharacterAttack(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.attackId = data.getInt32()

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] Float Response')
            print_exc()
