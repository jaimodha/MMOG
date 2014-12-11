from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from Character import Character
from Swordsman import Swordsman
from Axeman import Axeman
from miniMap import miniMap
import os

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
                        main.player._character.setScale(.4)
                        #main.player._character.setPos(swordsmanStartPos)
                        #main.player._character.setPos(0,0,0)
                        if self.faction==0:
                              	main.player._character.setPos(254.271, 6.72015, 0)
				main.player._floater.setPos(254.271, 6.72015, 0)
			
                        elif self.faction==1:
				main.player._character.setPos(-268.27, 8.0602, 0)
                             	main.player._floater.setPos(-268.27, 8.0602, 0)
                        #swordsmanStartPos.setY(swordsmanStartPos.getY())
                        #main.player._character.setPos(swordsmanStartPos.getX(),swordsmanStartPos.getY(),swordsmanStartPos.getZ())
                        #main.initx = swordsmanStartPos.getX()
                        main.base.camera.setPos(main.player._character.getX(),main.player._character.getY()+10,2)

                        main.miniMap = miniMap(main.player._character)
                        main.tower1 = main.miniMap.setTower("tower1", 0.08, 210.984, 115.005)
                        main.tower2 = main.miniMap.setTower("tower2", 0.08, 141.016, 0.440607)
                        main.tower3 = main.miniMap.setTower("tower3", 0.08, -0.903916, 11.3765)
                        main.tower4 = main.miniMap.setTower("tower4", 0.08, -210.771, 113.753)
                        main.tower5 = main.miniMap.setTower("tower5", 0.08, -149.953, 0.674369)
                        
            else:
                        #swordsmanStartPos = main.environ.find("**/start_point").getPos()
                        
                        if self.charType%2 == 0:
                                    main.characters[self.username] = Swordsman(self.username, self.faction)
                        if self.charType%2 == 1:
                                    main.characters[self.username] = Axeman(self.username, self.faction)
                                    
			if main.player._team == self.faction:
                                    main.miniMap.setTeamMate(self.username, 0.06, main.characters[self.username]._character.getX(), main.characters[self.username]._character.getY())
                                    
                        main.characters[self.username]._character.reparentTo(render)
                        main.characters[self.username]._character.setScale(.4)
                        main.characters[self.username]._character.setPos(500,500,0)
                        #main.characters[self.username]._character.setPos(swordsmanStartPos)
                        #swordsmanStartPos.setY(swordsmanStartPos.getY())
                        #main.characters[self.username]._character.setPos(swordsmanStartPos.getX(),swordsmanStartPos.getY(),swordsmanStartPos.getZ())
                        #main.initx = swordsmanStartPos.getX()

            main.taskMgr.add(self.main.move,"moveTask")
            

            #self.log('Received [' + str(Constants.RAND_INT) + '] Int Response')

        except:
            self.log('Bad [' + str(Constants.RAND_INT) + '] Int Response')
            print_exc()
