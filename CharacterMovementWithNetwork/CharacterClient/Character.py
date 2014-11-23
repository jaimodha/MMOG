import random, sys, os, math

from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Parallel
from direct.interval.ActorInterval import ActorInterval
from panda3d.core import Point3

class Character(object):

	def __init__(self, name, team):
		#self._player = player
		
		self._health = 0
		self._speed = 0
		
		self._is_playing = False
		self._is_moving = False	
		self._is_attacking = False
		self._is_dead = False
		#self._total_kills = 0
		
		self._name = name
		self._team = team
		#_character is an actor with pos and heading
		self._character = None

		self._atk_buff = 0
		self._def_buff = 0

	def basic_attack(self, target):
		pass

	def special_attack(self, target):
		pass

	"""
	Todd will handle this part
	"""
	#parameters are boolean values for the directions input by player and delta is time since last action.
	def move( self, fw, bw, lf, rt, delta ):
		#check direction
		if fw and not bw:
			if lf and not rt:
				angle = 45
			elif rt:
				angle = 315
			else:
				angle = 0
		elif bw and not fw:
			if lf and not rt:
				angle = 135
			elif rt:
				angle = 225
			else:
				angle = 180
		elif lf and not rt:
			angle = 90
		elif rt and not lf:
			angle = 270
		else:
			return

		#move based on speed and angle
		self._character.setH(angle)
		angle = angle * math.pi / 180
		x = self._character.getX() + (math.sin(angle) * self._speed * delta)
		y = self._character.getY() - (math.cos(angle) * self._speed * delta)
		if self.checkBoundary():
			self._character.setX( x )
			self._character.setY( y )

	#use to update movement from heartbeats.
	#heartbeat is time between heartbeats.
	def moveActor(self, x, y, z, rotation, isMoving, heartbeat):
		if isMoving:
			if not self._is_moving:
				self._is_moving = True
				self._character.loop("walk")
		moveInterval = self._character.posInterval(heartbeat, Point3(x, y, z))
		rotationInterval = self._character.hprInterval(heartbeat, Point3(rotation, 0, 0))
		sequence = Sequence(Parallel(rotationInterval, moveInterval))
		if not isMoving:
			self._is_moving = False
			#standInterval = self._character.actorInterval("walk", startFrame = 5, endFrame = 5)
			#sequence.append(standInterval)
			standInterval = self._character.actorInterval("idle")
			sequence.append(standInterval)
		sequence.start()

	def checkBoundary(self):
		return True
	
	def is_dead(self):
		return self._is_dead

	"""
	Getters
	"""
	def get_name(self):
		return self._name

	def get_team(self):
		return self._team

	def get_player(self):
		return self._player

	def get_kills(self):
		return self._total_kills

	def get_health(self):
		return self._health

	def is_moving(self):
		return self._is_moving

	"""
	Setters
	"""
	def set_kills(self,kills):
		self._total_kills = kills

	def set_health(self, health):
		self._health = health

	def set_is_moving(self, is_moving):
		self._is_moving = is_moving

	def set_speed(self, speed):
		self._speed = speed

	def set_actor(self, actor):
		self._character = actor