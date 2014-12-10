from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from BasicCharacter import BasicCharacter

class ResponseRemoveCharacter(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()

        except:
            self.log('Bad [' + str(Constants.SMSG_REMOVE_CHARACTER) + '] Remove Character')
            print_exc()
