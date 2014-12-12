from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from Character import Character
from Swordsman import Swordsman
from Axeman import Axeman
from miniMap import miniMap
from Chat import Chat

class ResponseRenderCharacter(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.charType = data.getInt32()
            self.faction = data.getInt32()
            self.x = data.getFloat32()
            self.y = data.getFloat32()
            self.z = data.getFloat32()

            print "new challenger"
            if main.username == self.username:
                        
                        if self.charType%2 == 0:
                                    main.player = Swordsman(self.username, self.faction)
                        if self.charType%2 == 1:
                                    main.player = Axeman(self.username, self.faction)

                        main.player._character.reparentTo(render)
                        main.player._character.setScale(.4)
                        main.player._character.setPos(self.x,self.y,self.z)
                        main.base.camera.setPos(main.player._character.getX(),main.player._character.getY()+10,2)
                        
                        
                        main.accept("mouse1", main.attack, [3])
                        main.accept("mouse3", main.attack, [4])
                        main.Chat = Chat(main.cManager)

                        main.miniMap = miniMap(main.player._character)
                        main.taskMgr.add(self.main.move,"moveTask")

                        
            else:
                        
                        if self.charType%2 == 0:
                                    main.characters[self.username] = Swordsman(self.username, self.faction)
                        if self.charType%2 == 1:
                                    main.characters[self.username] = Axeman(self.username, self.faction)

                        main.characters[self.username]._character.reparentTo(render)
                        main.characters[self.username]._character.setScale(.4)
                        main.characters[self.username]._character.setPos(self.x, self.y, self.z)
                        
        except:
            self.log('Bad [' + str(Constants.SMSG_RENDER_CHARACTER) + '] Render Character')
            print_exc()
