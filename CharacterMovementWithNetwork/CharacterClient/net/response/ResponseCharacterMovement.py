from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCharacterMovement(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.x = data.getFloat32()
            self.y = data.getFloat32()
            self.z = data.getFloat32()
            self.h = data.getFloat32()
            self.isMoving = data.getInt32()

            #actions
            if self.username in main.characters:
                        main.characters[self.username].moveActor(self.x, self.y, self.z, self.h, self.isMoving, float(.1))
                        main.miniMap.updateTeamMatePos(self.username, main.characters[self.username]._character.getX(), main.characters[self.username]._character.getY())

        except:
            self.log('Bad [' + str(Constants.SMSG_MOVE) + '] Float Response')
            print_exc()
