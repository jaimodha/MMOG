from direct.distributed.PyDatagramIterator import PyDatagramIterator

from panda3d.core import ConnectionWriter
from panda3d.core import NetDatagram
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader

#import your modules here
from common.Constants import Constants
from net.request.ServerRequestTable import ServerRequestTable
from net.response.ServerResponseTable import ServerResponseTable

class ConnectionManager:

    def __init__(self):

        self.cManager = QueuedConnectionManager()
        self.cListener = QueuedConnectionListener(self.cManager, 0)
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager, 0)
        
        self.rqTable = ServerRequestTable()
        self.rsTable = ServerResponseTable()

        self.connection = None

    def startConnection(self):
        """Create a connection with the remote host.

        If a connection can be created, create a task with a sort value of -39
        to read packets from the socket.

        """
        try:
            if self.connection == None:
                self.connection = self.cManager.openTCPClientConnection(Constants.SERVER_IP,
                                                                        Constants.SERVER_PORT,
                                                                        1000)

                if self.connection:
                    self.cReader.addConnection(self.connection)

                    taskMgr.add(self.updateRoutine, 'updateRoutine-Connection', -39)
                    taskMgr.doMethodLater(5, self.checkConnection, 'checkConnection')

                    return True
        except:
            pass

        return False

    def closeConnection(self):
        """Close the current connection with the remote host.

        If an existing connection is found, remove both the Main task, which
        is responsible for the heartbeat, and the Connection task, which is
        responsible for reading packets from the socket, then properly close
        the existing connection.

        """
        if self.connection != None:
            taskMgr.remove('updateRoutine-Main')
            taskMgr.remove('updateRoutine-Connection')
            taskMgr.remove('checkConnection')

            self.cManager.closeConnection(self.connection)
            self.connection = None

    def sendRequest(self, requestCode, args = {}):
        """Prepare a request packet to be sent.

        If the following request code exists, create an instance of this
        specific request using any extra arguments, then properly send it to
        the remote host.

        """
        if self.connection != None:
            request = self.rqTable.get(requestCode)

            if request != None:
                request.set(self.cWriter, self.connection)
                request.send(args)

    def handleResponse(self, responseCode, data):
        """Prepare a response packet to be processed.

        If the following response code exists, create an instance of this
        specific response using its data to be executed.

        """
        response = self.rsTable.get(responseCode)

        if response != None:
            #response.set(main)
            response.execute(data)

    def checkConnection(self, task):

        if not self.cReader.isConnectionOk(self.connection):
            self.closeConnection()
            self.showDisconnected(0)

            return task.done

        return task.again

    def updateRoutine(self, task):
        """A once-per-frame task used to read packets from the socket."""
        while self.cReader.dataAvailable():
            # Create a datagram to store all necessary data.
            datagram = NetDatagram()
            # Retrieve the contents of the datagram.
            if self.cReader.getData(datagram):
                # Prepare the datagram to be iterated.
                data = PyDatagramIterator(datagram)
                # Retrieve a "short" that contains the response code.
                responseCode = data.getUint16()
                # Pass into another method to execute the response.
                if responseCode != Constants.MSG_NONE:
                    self.handleResponse(responseCode, data)

        return task.cont
