#@PydevCodeAnalysisIgnore
# To change this template, choose Tools | Templates
# and open the template in the editor.

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestRandomShort(ServerRequest):

    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.RAND_SHORT)
            pkg.addUint16(args)

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_SHORT) + '] Short Request')
        except:
            self.log('Bad [' + str(Constants.RAND_SHORT) + '] Short Request')
            print_exc()