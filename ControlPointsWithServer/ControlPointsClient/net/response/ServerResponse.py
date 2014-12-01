# To change this template, choose Tools | Templates
# and open the template in the editor.

from datetime import datetime

from common.Constants import Constants

class ServerResponse:

    def log(self, msg):
        """Log a simple response message.

        Print the timestamp at which the response is being received following a
        simple description of the response. For instance:

        [2010-01-01 11:59:59]
          Received [2] Login Response

        """
        if Constants.DEBUG:
            print '[' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ']' + '\n' + '  ' + str(msg)

    def set(self, main):
        """Initialize a reference for the main instance."""
        self.main = main

    def execute(self, data):
        """Abstract method defined by a subclass to handle a specific response."""
        pass