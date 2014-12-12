from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestSelectCharAndTeamType(ServerRequest):


    def send(self, message = None):

        try:
            # self.cManager.sendRequest(Constants.CMSG_CREATE_CHARACTER, (self.username01,self.chartitle, self.nameOfCharInput,self.factiontile));
            print "name of char: ", list(message)[0], "; chartype: "+ str(list(message)[1])+"; faction:"+str(list(message)[2])
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CREATE_CHARACTER)
            pkg.addString(list(message)[0])
            pkg.addInt32(list(message)[1])
            pkg.addInt32(list(message)[2])
          
            print 'hello packet sent'
            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + list(message)[0] + ", "+ list(message)[1] + '] selection Request')
            print_exc()
