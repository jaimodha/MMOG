# To change this template, choose Tools | Templates
# and open the template in the editor.

from datetime import datetime

from common.Constants import Constants

class ServerRequest:

    def log(self, msg):
        """Log a simple request message.

        Print the timestamp at which the request is being sent following a
        simple description of the request. For instance:

        [2010-01-01 11:59:59]
          Sent [1] Login Request

        """
        if Constants.DEBUG:
            print '[' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ']' + '\n' + '  ' + str(msg)

    def set(self, cWriter, connection):
        """Initialize a reference for the output stream."""
        self.cWriter = cWriter
        self.connection = connection

    def send(self, args):
        """Abstract method defined by a subclass to handle a specific request."""
        pass
