from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from Character import Character

from direct.actor.Actor import Actor

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            self.name = data.getString()
            self.factionId = data.getInt32()

            print "new challenger"
            
            ralph = Actor("models/ralph",
                                     {"run":"models/ralph-run",
                                      "walk":"models/ralph-walk"})
            ralph.reparentTo(render)
            ralph.setScale(.2)
            ralph.setPos(main.ralphStartPos)
                
            if main.name == self.name:
                main.character = Character(self.name, ralph, self.factionId)
                main.base.camera.setPos(main.character.actor.getX(),main.character.actor.getY()+10,2)
                # Try this out
                main.characters[self.name] = main.character
            else:
                main.characters[self.name] = Character(self.name, ralph, self.factionId)

            main.taskMgr.add(self.main.move,"moveTask")
            #main.taskMgr.doMethodLater(1, self.main.CPHandler, "CPHandlerTask")
            

            #self.log('Received [' + str(Constants.RAND_INT) + '] Int Response')

        except:
            self.log('Bad [' + str(Constants.RAND_INT) + '] Int Response')
            print_exc()
