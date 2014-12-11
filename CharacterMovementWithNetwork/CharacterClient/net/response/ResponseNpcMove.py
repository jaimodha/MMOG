from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseNpcMove(ServerResponse):

    def execute(self, data):

        try:
            for i in range(0,25):
                npcId = data.getInt32()
                #print npcId
                targetState = data.getString()
                #print targetState
                targetUsername = data.getString()
                #print targetUsername
                        
                if(targetUsername != main.player.get_name() and targetUsername != "none"):
                    for target in main.characters.values():
                        #print "Target Username",
                        #print target.get_name()
                        if(target.get_name() == targetUsername):
                            #print target.username+ "  ",
                            if(targetState == "start"):
                                #print targetState,
                                #print "   ",
                                if( not main.controlNpc.npcStatus(npcId)):
                                    #print main.controlNpc.npcStatus(npcId)
                                    main.controlNpc.move(npcId, target._character)
                            elif(targetState == "stop"):
                                #print "Reached stop"
                                if(main.controlNpc.npcStatus(npcId)):
                                    main.controlNpc.stop(npcId)

        except:
            self.log('Bad [' + str(Constants.SMSG_NPCMOVE) + '] Float Response')
            print_exc()
