from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRandomFloat(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getFloat32()

            print "ResponseRandomFloat - ", self.msg

            #self.log('Received [' + str(Constants.RAND_FLOAT) + '] Float Response')

        except:
            self.log('Bad [' + str(Constants.RAND_FLOAT) + '] Float Response')
            print_exc()
