from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestLogin(ServerRequest):
    def send(self, message = None):
        try:      
            print "username: ", list(message)[0], "; password: ", list(message)[1]
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_AUTH)
            pkg.addString(list(message)[0])
            pkg.addString(list(message)[1])

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + list(message)[0] + ", "+ list(message)[1] + '] Login Request')
            print_exc()
