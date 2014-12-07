from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestSelectCharacter(ServerRequest):


    def send(self, data = None):

        try:
            """ USERNAME """
            """ char_id """
            """ type """
            """ faction """
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_SELECT_CHARACTER)
            pkg.addString(list(data)[0]) #username
            pkg.addString(list(data)[1]) #char_name
            pkg.addInt32(list(data)[2]) #char_id
            pkg.addInt32(list(data)[3]) #char_type
            pkg.addInt32(list(data)[4]) #char_faction
            

            self.cWriter.send(pkg, self.connection)

            #self.log('Sent [' + str(Constants.RAND_STRING) + '] Int Request')
        except:
            self.log('Bad [' + str(Constants.RAND_STRING) + '] Int Request')
            print_exc()
