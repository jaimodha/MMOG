from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRandomInt(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getInt32()

            print "ResponseRandomInt - ", self.msg

            #self.log('Received [' + str(Constants.RAND_INT) + '] Int Response')

        except:
            self.log('Bad [' + str(Constants.RAND_INT) + '] Int Response')
            print_exc()
