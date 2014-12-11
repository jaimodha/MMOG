from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseNpcDeath(ServerResponse):

    def execute(self, data):

        try:
            cpId = data.getInt32()
            print cpId
            
            main.controlNpc.switchControl(cpId)

        except:
            self.log('Bad [' + str(Constants.SMSG_NPCDEATH) + '] Float Response')
            print_exc()
