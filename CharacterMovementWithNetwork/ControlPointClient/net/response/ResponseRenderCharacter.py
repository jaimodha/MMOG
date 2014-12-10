from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRenderCharacter(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.charType = data.getInt32()
            self.faction = data.getInt32()
            self.x = data.getFloat32()
            self.y = data.getFloat32()
            self.z = data.getFloat32()

            if main.username != self.username:
                main.characters[self.username] = BasicCharacter(self.username, self.faction)
                main.characters[self.username].move(self.x, self.y, self.z)

        except:
            self.log('Bad [' + str(Constants.RAND_INT) + '] Int Response')
            print_exc()
