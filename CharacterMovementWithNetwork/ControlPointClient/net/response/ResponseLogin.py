from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from BasicCharacter import BasicCharacter

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.charType = data.getInt32()
            self.faction = data.getInt32()

            if main.username != self.username:
                main.characters[self.username] = BasicCharacter(self.username, self.faction)

        except:
            self.log('Bad [' + str(Constants.RAND_INT) + '] Int Response')
            print_exc()
