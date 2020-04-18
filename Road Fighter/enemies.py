import random

from pixelsmash.funciones import cargar_img
from pixelsmash.array import Array
from pixelsmash.timer import Timer

from settings import HEIGHT
from enemy import Enemy

class Enemies(object):

	def __init__(self):
		random.seed()
		self.enemies = Array()

		self.gfx = [cargar_img("enemies/enemy_1", 2),
					cargar_img("enemies/enemy_3", 2),
					cargar_img("enemies/enemy_2", 2),
					cargar_img("enemies/bonus", 2)]

		self.timer = Timer(2000)

	def update(self, _dt, _player, _UI):
		self.enemies.update(_dt)
		self.timer.update(_dt)
		if _player.alive:
			self.generate_enemy()
			self.attack(_player, _UI)
		else:
			self.enemies.array = []

		self.remove_trash()

	def render(self, _screen):
		self.enemies.render(_screen)

	def generate_enemy(self):
		if self.timer.tick:
			enemy_type = random.randrange(len(self.gfx))
			self.enemies.add_element(Enemy(random.randrange(170, 300), self.gfx[enemy_type], enemy_type))
			self.timer.delay = random.randrange(2000, 3600, 100)

	def attack(self, _player, _UI):
		for element in self.enemies.array:
			element.vx = 0
			if element.bounds.colliderect(_player.bounds):
				if element.type != 3:
					if element.vx > 0:
						_player.animator.reproducir_animacion("hacia_derecha", 1)
					elif element.vx < 0:
						_player.animator.reproducir_animacion("hacia_izquierda", 1)
					else:
						_player.explotar()
				else:
					_UI.score += 10
					self.enemies.delete_element(element)

		if self.enemies.get_current_element() != None:
			if self.enemies.get_current_element().bounds.left > _player.bounds.right:
				self.enemies.get_current_element().vx = -self.enemies.get_current_element().speed
			elif self.enemies.get_current_element().bounds.right < _player.bounds.left:
				self.enemies.get_current_element().vx = self.enemies.get_current_element().speed
			else:
				self.enemies.get_current_element().vx = 0

	def remove_trash(self):
		for enemy in self.enemies.array:
			if enemy.bounds.top > HEIGHT:
				enemy.alive = False

