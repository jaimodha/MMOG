from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from Swordsman import Swordsman
from Axeman import Axeman

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
                    #self.main.player.set_health(self.main.player.get_health() - self.healthChange)
                    if isinstance(self.main.player, Swordsman):
                        if (self.main.player.get_health()-self.healthChange)>Swordsman.MAX_HEALTH:
                            self.main.player.set_health(Swordsman.MAX_HEALTH)
                        else:
                            self.main.player.set_health(self.main.player.get_health() - self.healthChange)
                    elif isinstance(self.main.player, Axeman):
                        if (self.main.player.get_health()-self.healthChange)>Axeman.MAX_HEALTH:
                            self.main.player.set_health(Axeman.MAX_HEALTH)
                        else:
                            self.main.player.set_health(self.main.player.get_health() - self.healthChange)
                    self.main.player.hb.setValue(self.main.player.get_health())
                    if self.main.player._is_dead:
                        self.main.player._is_dead = False
                        self.main.player._is_moving = False
                else:
                    #self.main.characters[self.username].set_health(self.main.characters[self.username].get_health() - self.healthChange)
                    if isinstance(self.main.characters[self.username], Swordsman):
                        if (self.main.characters[self.username].get_health() - self.healthChange)>Swordsman.MAX_HEALTH:
                            self.main.characters[self.username].set_health(Swordsman.MAX_HEALTH)
                        else:
                            self.main.characters[self.username].set_health(self.main.characters[self.username].get_health() - self.healthChange)
                    elif isinstance(self.main.characters[self.username], Axeman):
                        if (self.main.characters[self.username].get_health() - self.healthChange)>Axeman.MAX_HEALTH:
                            self.main.characters[self.username].set_health(Axeman.MAX_HEALTH)
                        else:
                            self.main.characters[self.username].set_health(self.main.characters[self.username].get_health() - self.healthChange)
                    self.main.characters[self.username].hb.setValue(self.main.characters[self.username].get_health())
                    if self.main.characters[self.username]._is_dead:
                        self.main.characters[self.username]._is_dead = False
                        self.main.characters[self.username]._is_moving = False
        except:
            self.log('Bad [' + str(Constants.SMSG_ATTACK) + '] Attack Response')
            print_exc()
