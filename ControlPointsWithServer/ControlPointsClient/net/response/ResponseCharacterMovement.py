from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCharacterMovement(ServerResponse):

    def execute(self, data):

        try:
            self.name = data.getString()
            self.x = data.getFloat32()
            self.y = data.getFloat32()
            self.z = data.getFloat32()
            self.h = data.getFloat32()

            #actions
            if self.name in main.characters:
                main.characters[self.name].actor.setX(self.x)
                main.characters[self.name].actor.setY(self.y)
                main.characters[self.name].actor.setZ(self.z)
                main.characters[self.name].actor.setH(self.h)

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] Float Response')
            print_exc()
