from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from Character import Character
from Swordsman import Swordsman
from Axeman import Axeman
from miniMap import miniMap

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            self.username = data.getString()
            self.charType = data.getInt32()
            self.faction = data.getInt32()

            print "new challenger"
            if main.username == self.username:
                        
                        #swordsmanStartPos = self.main.environ.find("**/start_point").getPos()
                        
                        if self.charType%2 == 0:
                                    main.player = Swordsman(self.username, self.faction)
                        if self.charType%2 == 1:
                                    main.player = Axeman(self.username, self.faction)

                        main.player._character.reparentTo(render)
                        main.player._character.setScale(.1)
                        #main.player._character.setPos(swordsmanStartPos)
                        main.player._character.setPos(0,0,0)
                        #swordsmanStartPos.setY(swordsmanStartPos.getY())
                        #main.player._character.setPos(swordsmanStartPos.getX(),swordsmanStartPos.getY(),swordsmanStartPos.getZ())
                        #main.initx = swordsmanStartPos.getX()
                        main.base.camera.setPos(main.player._character.getX(),main.player._character.getY()+10,2)

                        main.miniMap = miniMap(main.player._character)
                        main.tower1 = main.miniMap.setTower("tower1", 0.15, 0.5, -0.5)
                        
            else:
                        #swordsmanStartPos = main.environ.find("**/start_point").getPos()
                        
                        if self.charType%2 == 0:
                                    main.characters[self.username] = Swordsman(self.username, self.faction)
                        if self.charType%2 == 1:
                                    main.characters[self.username] = Axeman(self.username, self.faction)

                        main.characters[self.username]._character.reparentTo(render)
                        main.characters[self.username]._character.setScale(.1)
                        main.characters[self.username]._character.setPos(0,0,0)
                        #main.characters[self.username]._character.setPos(swordsmanStartPos)
                        #swordsmanStartPos.setY(swordsmanStartPos.getY())
                        #main.characters[self.username]._character.setPos(swordsmanStartPos.getX(),swordsmanStartPos.getY(),swordsmanStartPos.getZ())
                        #main.initx = swordsmanStartPos.getX()

                        main.miniMap = miniMap(main.player._character)
                        main.tower1 = main.miniMap.setTower("tower1", 0.05, 0.5, -0.5)

            main.taskMgr.add(self.main.move,"moveTask")
            

            #self.log('Received [' + str(Constants.RAND_INT) + '] Int Response')

        except:
            self.log('Bad [' + str(Constants.RAND_INT) + '] Int Response')
            print_exc()
