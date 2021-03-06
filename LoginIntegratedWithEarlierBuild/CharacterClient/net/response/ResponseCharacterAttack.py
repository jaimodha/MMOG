from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCharacterAttack(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.attackId = data.getInt32()

            #actions
            #only need to add animation for characters that are not the player
            if self.username in main.characters:
                main.characters[self.username].animate(self.attackId)

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] Float Response')
            print_exc()
