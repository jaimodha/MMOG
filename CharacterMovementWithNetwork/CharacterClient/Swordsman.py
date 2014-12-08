from Character import Character
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

class Swordsman(Character):
	ATK_RANGE = 3
	BASIC_ATK_DMG = 15
	SPECIAL_ATK_DMG = 30
	MOVE_SPEED = 10
	CHARGE_SPEED = 15
	MAX_HEALTH = 100
	FOV = 45

	def __init__(self, *args):
		super(Swordsman, self).__init__(*args)
		Character.set_health(self, Swordsman.MAX_HEALTH)
		Character.set_speed(self, Swordsman.MOVE_SPEED)
		actor = Actor("models/swordsman", 
						{"idle": "models/swordsman-idle", 
						 "walk": "models/swordsman-walk", 
						 "run": "models/swordsman-run", 
						 "hurt": "models/swordsman-hurt", 
						 "die": "models/swordsman-die", 
						 "attack": "models/swordsman-attack"})

		team = Character.get_team(self)
		if team == 0:
			"""
			actor = Actor("models/swordsman_red", 
						{"idle": "models/swordsman-idle", 
						 "walk": "models/swordsman-walk", 
						 "run": "models/swordsman-run", 
						 "hurt": "models/swordsman-hurt", 
						 "die": "models/swordsman-die", 
						 "attack": "models/swordsman-attack"})
			"""
			tex = loader.loadTexture("models/textures/swordsman_red.png")
			ts = actor.findTextureStage('*')
			actor.setTexture(ts, tex, 1)
			#ts = actor.findTextureStage('ts')
			#actor.setTexture(ts, tex)
		elif team == 1:
			"""
			actor = Actor("models/swordsman_blue", 
						{"idle": "models/swordsman-idle", 
						 "walk": "models/swordsman-walk", 
						 "run": "models/swordsman-run", 
						 "hurt": "models/swordsman-hurt", 
						 "die": "models/swordsman-die", 
						 "attack": "models/swordsman-attack"})
			"""
			tex = loader.loadTexture("models/textures/swordsman_blue.png")
			ts = actor.findTextureStage('*')
			actor.setTexture(ts, tex, 1)
			#ts = actor.findTextureStage('ts')
			#actor.setTexture(ts, tex)
		
		Character.set_actor(self, actor)
		self.hb = HealthBar(2.0, value=Swordsman.MAX_HEALTH)
		self.hb.reparentTo(self._character)
		
		self.model = loader.loadModel("models/circle")
		self.model.setTransparency(True)
		self.model.reparentTo(self._character)
		self.model.setAlphaScale(0.5)
		self.model.setScale(2)
		self.model.setPos(0, 0, -10)
		
	def basic_attack(self):
		total_dmg = Swordsman.BASIC_ATK_DMG
		swing_sound = loader.loadSfx("sound/Swoosh.mp3")

		if self._atk_buff==1:
			total_dmg *= 1.1
		elif self._atk_buff==2:
			total_dmg *= 1.25

		sound_interval = SoundInterval(
    								swing_sound,
    								loop = 2 ,
    								duration = 0.6,
    								volume = 0.7,
    								startTime = 0
									)
		atk_interval1 = self._character.actorInterval("attack", startFrame=1, endFrame=26)
		atk_interval2 = self._character.actorInterval("attack", startFrame=56, endFrame=80)
		seq = Sequence(atk_interval1, atk_interval2)
		if self._is_moving:
			seq.append(Func(self.animate, 2))
		seq2 = Sequence(Wait(0.5), sound_interval, sound_interval)
		seq.start()
		seq2.start()
		
		return total_dmg

	def special_attack(self):
		total_dmg = Swordsman.SPECIAL_ATK_DMG
		swing_sound = loader.loadSfx("sound/Swoosh.mp3")
			
		if self._atk_buff==1:
			total_dmg *= 1.1
		elif self._atk_buff==2:
			total_dmg *= 1.25

		sound_interval = SoundInterval(
    							swing_sound,
    							loop = 2 ,
    							duration = 0.8,
    							volume = 0.7,
    							startTime = 0
								)
		atk_interval1 = self._character.actorInterval("attack", startFrame=1, endFrame=13)
		atk_interval2 = self._character.actorInterval("attack", startFrame=38, endFrame=80)
		seq = Sequence(atk_interval1, atk_interval2)
		if self._is_moving:
			seq.append(Func(self.animate, 2))
		seq2 = Sequence(Wait(0.5), sound_interval, sound_interval)
		seq.start()
		seq2.start()
		
		return total_dmg

	def take_damage(self, health_change):
		health = Character.get_health(self)
		if health < health_change and not self._is_dead:
			Character.set_health(self, 0)
			self.hb.setValue(0)
			hurt_interval = self._character.actorInterval("hurt")
			death_interval = self._character.actorInterval("die")
			seq = Sequence(hurt_interval, death_interval)
			seq.append(Wait(2))
			# add Func interval to place the character at a new location
			seq.append(Func(self.respawn))
			seq.start()
			self._is_dead = True
			#self._is_moving=2
		else:
			Character.set_health(self, health-health_change)
			#self.hb.setValue(Character.get_health(self)-health_change)
			self.hb.setValue(Character.get_health(self))
			self._character.play("hurt")

	def apply_def_buff(self):
		if not self._is_dead:
			health = Character.get_health(self)
			if self._def_buff==1:
				Character.set_health(self, health*1.1)
				Swordsman.MAX_HEALTH = Swordsman.MAX_HEALTH*1.1
			elif self._def_buff==2:
				Character.set_health(self, health*1.25)
				Swordsman.MAX_HEALTH = Swordsman.MAX_HEALTH*1.25

	def unapply_def_buff(self):
		if not self._is_dead:
			if self._def_buff==0:
				Swordsman.MAX_HEALTH = 100
			elif Swordsman.MAX_HEALTH==125 and self._def_buff==1:
				Swordsman.MAX_HEALTH = 110

			health = Character.get_health(self)
			if health > Swordsman.MAX_HEALTH:
					health = Swordsman.MAX_HEALTH

	def animate(self, anim_type):
		if anim_type==0:
			self._character.loop("idle")
		elif anim_type==1:
			self._character.loop("walk")
		elif anim_type==2:
			self._character.loop("run")
		elif anim_type==3:
			atk_interval1 = self._character.actorInterval("attack", startFrame=1, endFrame=26)
			atk_interval2 = self._character.actorInterval("attack", startFrame=56, endFrame=80)
			seq = Sequence(atk_interval1, atk_interval2)
			seq.start()
		elif anim_type==4:
			atk_interval1 = self._character.actorInterval("attack", startFrame=1, endFrame=13)
			atk_interval2 = self._character.actorInterval("attack", startFrame=38, endFrame=80)
			seq = Sequence(atk_interval1, atk_interval2)
			seq.start()
		elif anim_type==5:
			self._character.play("hurt")
		elif anim_type==6:
			self._character.play("die")

	def respawn(self):
		self._is_moving=2
		self._character.loop("idle")