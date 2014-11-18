from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRandomString(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getString()

            print "ResponseRandomString - ", self.msg

            #self.log('Received [' + str(Constants.RAND_STRING) + '] String Response')

        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] String Response')
            print_exc()
