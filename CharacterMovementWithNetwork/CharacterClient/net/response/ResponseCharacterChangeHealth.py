from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCharacterChangeHealth(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.healthChange = data.getInt32() #healthChange assumed to be damage so healing is negative

            #actions
            if self.healthChange > 0:
                if self.main.player.get_name() == self.username:
                    self.main.player.take_damage(self.healthChange)
                else:
                    self.main.characters[self.username].take_damage(self.healthChange)
            else:
                if self.main.player.get_name() == self.username:
                    self.main.player.set_health(self.main.player.get_health - self.healthChange)
                else:
                    self.main.characters[self.username].set_health(self.main.characters[username].get_health - self.healthChange)
        except:
            self.log('Bad [' + str(Constants.SMSG_ATTACK) + '] Attack Response')
            print_exc()
