from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestSelectCharAndTeamType(ServerRequest):


    def send(self, message = None):

        try:
            
            print "Character type: ", list(message)[0], "; faction : ", list(message)[1]
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_CHARACTER)
            pkg.addString(list(message)[0])
            pkg.addString(list(message)[1])

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + list(message)[0] + ", "+ list(message)[1] + '] selection Request')
            print_exc()
