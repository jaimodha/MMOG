from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseHeartbeat(ServerResponse):

   def execute(self, data):

        try:
            self.status = data.getUint16()

            print "ResponseHeartBeat", self.status

            self.log('Received [' + str(Constants.SMSG_HEARTBEAT) + '] Heart Beat Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_HEARTBEAT) + '] Heart Beat Response')
            print_exc()
