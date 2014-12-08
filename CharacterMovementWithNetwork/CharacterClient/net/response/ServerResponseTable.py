from common.Constants import Constants

from net.response.ResponseRandomInt import ResponseRandomInt
from net.response.ResponseRandomString import ResponseRandomString
from net.response.ResponseRandomShort import ResponseRandomShort
from net.response.ResponseRandomFloat import ResponseRandomFloat
from net.response.ResponseCharacterMovement import ResponseCharacterMovement
from net.response.ResponseCharacterAttack import ResponseCharacterAttack
from net.response.ResponseCharacterChangeHealth import ResponseCharacterChangeHealth
from net.response.ResponseChat import ResponseChat
from net.response.ResponseLogin import ResponseLogin
from net.response.ResponseRenderCharacter import ResponseRenderCharacter
from net.response.ResponseRemoveCharacter import ResponseRemoveCharacter
from net.response.ResponseCP import ResponseCP

class ServerResponseTable:
    """
    The ServerResponseTable contains a mapping of all responses for use
    with the networking component.
    """
    responseTable = {}

    def __init__(self):
        """Initialize the response table."""
        self.add(Constants.RAND_INT, 'ResponseRandomInt')
        self.add(Constants.RAND_STRING, 'ResponseRandomString')
        self.add(Constants.RAND_SHORT, 'ResponseRandomShort')
        self.add(Constants.RAND_FLOAT, 'ResponseRandomFloat')
        self.add(Constants.SMSG_AUTH, 'ResponseLogin')
        self.add(Constants.SMSG_MOVE, 'ResponseCharacterMovement')
        self.add(Constants.SMSG_ATTACK, 'ResponseCharacterAttack')
        self.add(Constants.SMSG_CHAT, 'ResponseChat')
        self.add(Constants.SMSG_HEALTH, 'ResponseCharacterChangeHealth')
        self.add(Constants.SMSG_RENDER_CHARACTER, 'ResponseRenderCharacter')
        self.add(Constants.SMSG_REMOVE_CHARACTER, 'ResponseRemoveCharacter')
        self.add(Constants.SMSG_CONTROL_POINT_STATE, 'ResponseCP')

    def add(self, constant, name):
        """Map a numeric response code with the name of an existing response module."""
        if name in globals():
            self.responseTable[constant] = name
        else:
            print 'Add Response Error: No module named ' + str(name)

    def get(self, responseCode):
        """Retrieve an instance of the corresponding response."""
        serverResponse = None

        if responseCode in self.responseTable:
            serverResponse = globals()[self.responseTable[responseCode]]()
        else:
            print 'Bad Response Code: ' + str(responseCode)

        return serverResponse
