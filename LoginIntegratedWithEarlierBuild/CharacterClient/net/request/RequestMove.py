from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestMove(ServerRequest):


    def send(self, args = None):
        
        
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_MOVE)
            pkg.addFloat32(args[0])#x
            pkg.addFloat32(args[1])#y
            pkg.addFloat32(args[2])#z
            pkg.addFloat32(args[3])#h
            pkg.addInt32(args[4])#isMoving

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_FLOAT) + '] Float Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_MOVE) + '] Move Request')
            print_exc()