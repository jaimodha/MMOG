# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 29, 2011 2:47:11 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRandomShort(ServerResponse):

    def execute(self, data):

        try:
            self.msg = data.getUint16()

            print "ResponseRandomShort - ", self.msg

            #self.log('Received [' + str(Constants.RAND_SHORT) + '] Short Response')

        except:
            self.log('Bad [' + str(Constants.RAND_SHORT) + '] Short Response')
            print_exc()
