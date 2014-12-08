from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCP(ServerResponse):

    def execute(self, data):

        try:
            self.cpId = data.getInt32()
            self.timer = data.getInt32()
            self.factionId = data.getInt32()

            #actions
            main.cpList[self.cpId].setTimer(self.timer)
            main.cpList[self.cpId].setFactionId(self.factionId)

        except:
            self.log('Bad [' + str(Constants.SMSG_CONTROL_POINT_STATE) + '] CP Response')
            print_exc()
