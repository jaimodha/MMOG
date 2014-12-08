from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCP(ServerRequest):


    def send(self, args = None):
        
        
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CONTROL_POINT_STATE)
            pkg.addInt32(args[0])#cpId
            pkg.addInt32(args[1])#timer
            pkg.addInt32(args[2])#factionId

            self.cWriter.send(pkg, self.connection)

        except:
            self.log('Bad [' + str(Constants.CMSG_CONTROL_POINT_STATE) + '] CP Request')
            print_exc()