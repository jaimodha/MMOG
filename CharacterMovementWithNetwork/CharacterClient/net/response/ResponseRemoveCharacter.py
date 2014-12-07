from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from Character import Character
from Swordsman import Swordsman
from Axeman import Axeman
from miniMap import miniMap

class ResponseRemoveCharacter(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            
            main.characters[self.username]._character.cleanup()

        except:
            self.log('Bad [' + str(Constants.SMSG_REMOVE_CHARACTER) + '] Remove Character')
            print_exc()
