from common.Constants import Constants

from net.request.RequestRandomInt import RequestRandomInt
from net.request.RequestRandomString import RequestRandomString
from net.request.RequestRandomShort import RequestRandomShort
from net.request.RequestRandomFloat import RequestRandomFloat
from net.request.RequestLogin import RequestLogin

class ServerRequestTable:
    """
    The ServerRequestTable contains a mapping of all requests for use
    with the networking component.
    """
    requestTable = {}

    def __init__(self):
        """Initialize the request table."""
        self.add(Constants.RAND_INT, 'RequestRandomInt')
        self.add(Constants.RAND_STRING, 'RequestRandomString')
        self.add(Constants.RAND_SHORT, 'RequestRandomShort')
        self.add(Constants.RAND_FLOAT, 'RequestRandomFloat')
        self.add(Constants.CMSG_AUTH, 'RequestLogin')
        self.add(Constants.CMSG_CREATE_CHARACTER,'RequestCreateCharacter')

    def add(self, constant, name):
        """Map a numeric request code with the name of an existing request module."""
        if name in globals():
            self.requestTable[constant] = name
        else:
            print 'Add Request Error: No module named ' + str(name)

    def get(self, requestCode):
        """Retrieve an instance of the corresponding request."""
        serverRequest = None

        if requestCode in self.requestTable:
            serverRequest = globals()[self.requestTable[requestCode]]()
        else:
            print 'Bad Request Code: ' + str(requestCode)

        return serverRequest
