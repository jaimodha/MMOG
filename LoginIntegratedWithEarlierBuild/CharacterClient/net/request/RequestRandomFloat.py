from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestRandomFloat(ServerRequest):


    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.RAND_FLOAT)
            pkg.addFloat32(args)

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_FLOAT) + '] Float Request')
        except:
            self.log('Bad [' + str(Constants.RAND_FLOAT) + '] Float Request')
            print_exc()