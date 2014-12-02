from Character import Character
from math import sqrt
from direct.actor.Actor import Actor
from panda3d.core import PandaNode,NodePath,TextNode
from direct.gui.DirectGui import DirectWaitBar
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Parallel
from direct.interval.ActorInterval import ActorInterval
from direct.interval.IntervalGlobal import SoundInterval
from direct.interval.IntervalGlobal import Wait
from direct.interval.IntervalGlobal import Func
from HealthBar import HealthBar

class Axeman(Character):
    BASIC_ATK_DMG = 12
    SPECIAL_ATK_DMG = 40
    MAX_HEALTH = 120
    ATK_RANGE = 3
    MOVE_SPEED = 8
    FOV = 45
    
    def __init__(self, *args):
        super(Axeman, self).__init__(*args)
        Character.set_health(self, Axeman.MAX_HEALTH)
        actor = Actor("models/axeman", {"idle": "models/axeman-idle", 
                                        "walk": "models/axeman-walk", 
                                        "run": "models/axeman-run" ,
                                        "hurt": "models/axeman-hurt", 
                                        "die": "models/axeman-die", 
                                        "attack": "models/axeman-swing", 
                                        "special":"models/axeman-special-attack"})
        Character.set_speed(self, Axeman.MOVE_SPEED)

        # loda texture based on team 
        team = Character.get_team(self)
        if team == 0:
            tex = loader.loadTexture("models/textures/axeman_red.png")
            ts = actor.findTextureStage("*")
            actor.setTexture(ts, tex, 1)
        elif team == 1:
            tex = loader.loadTexture("models/textures/axeman_blue.png")
            ts = actor.findTextureStage('*')
            actor.setTexture(ts, tex, 1)

        Character.set_actor(self, actor)

        #attach axe 
        rightHand = self._character.exposeJoint(None, 'modelRoot', 'hand_ctrl_r')
        axe = loader.loadModel("models/axe")
        axe_tex = loader.loadTexture("models/textures/axe.png")
        axe.setTexture(axe_tex, 1)
        axe.setPos(-3.0, 0.6, -0.2)
        axe.setHpr(0, -90, -90)
        axe.setScale(10)
        axe.reparentTo(rightHand)
        axe.show()

        self.hb = HealthBar(1.5, value=Axeman.MAX_HEALTH)
        self.hb.reparentTo(self._character)
        
    def basic_attack(self):
        total_dmg = Axeman.BASIC_ATK_DMG
        swing_sound = loader.loadSfx("sound/Woosh.wav")
        
        if self._atk_buff==1:
            total_dmg *= 1.1
        elif self._atk_buff==2:
            total_dmg *= 1.25
        # play animation
        sound_interval1 = SoundInterval(
                                    swing_sound,
                                    loop = 1 ,
                                    duration = 0,
                                    volume = 0.7,
                                    startTime = 0
                                    )
        seq2 = Sequence(Wait(0.5),sound_interval1, sound_interval1)
        #self._character.play("attack")
        atk_interval = self._character.actorInterval("attack")
        seq = Sequence(atk_interval)
        if self._is_moving:
            seq.append(Func(self.loop_run))
        seq.start()
        seq2.start()

        return total_dmg

          
    def special_attack(self):
        total_dmg = Axeman.SPECIAL_ATK_DMG
        
        if self._atk_buff==1:
            total_dmg *= 1.1
        elif self._atk_buff==2:
            total_dmg *= 1.25
         
        #self._character.play("special",fromFrame = 10)
        atk_interval = self._character.actorInterval("special", startFrame=10)
        seq = Sequence(atk_interval)
        if self._is_moving:
            seq.append(Func(self.loop_run))
        seq.start()

        return total_dmg
             
    def loop_run(self):
        self._character.loop("run")

    def apply_def_buff(self):
        if not self._is_dead:
            health = Character.get_health(self)
            if self._def_buff==1:
                Character.set_health(self, health*1.1)
                Axeman.MAX_HEALTH = Axeman.MAX_HEALTH*1.1
            elif self._def_buff==2:
                Character.set_health(self, health*1.25)
                Axeman.MAX_HEALTH = Axeman.MAX_HEALTH*1.25
        
    def unapply_def_buff(self):
        if not self._is_dead:
            if self._def_buff==0:
                Axeman.MAX_HEALTH = 100
            elif Axeman.MAX_HEALTH==140 and self._def_buff==1:
                Axeman.MAX_HEALTH = 110

            health = Character.get_health(self)
            if health > Axeman.MAX_HEALTH:
                    health = Axeman.MAX_HEALTH
        pass
       
    def take_damage(self, health_change):
        health = Character.get_health(self)
        if health <= health_change and not self._is_dead:
            Character.set_health(self, 0)
            self.hb.setValue(0)
            hurt_interval = self._character.actorInterval("hurt")
            death_interval = self._character.actorInterval("die")
            seq = Sequence(hurt_interval, death_interval)
            seq.start()
            self._is_dead = True
        else:
            Character.set_health(self, health-health_change)
            self.hb.setValue(Character.get_health(self)-health_change)
            self._character.play("hurt")

    def animate(self, anim_type):
        if anim_type==0:
            self._character.loop("idle")
        elif anim_type==1:
            self._character.loop("walk")
        elif anim_type==2:
            self._character.loop("run")
        elif anim_type==3:
            self._character.play("attack")
        elif anim_type==4:
            self._character.play("special",fromFrame = 10)
        elif anim_type==5:
            self._character.play("hurt")
        elif anim_type==6:
            self._character.play("die")