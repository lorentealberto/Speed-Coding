from road import Road
from player import Player
from enemies import Enemies

from ui import UI

class Game(object):

	def __init__(self, _states_manager):
		self.road = Road()
		self.player = Player()
		self.enemies = Enemies()
		self.ui = UI()

	def update(self, _dt):
		self.ui.update(_dt)
		self.road.update(_dt, self.ui)
		self.player.update(_dt, self.road.road)
		self.enemies.update(_dt, self.player, self.ui)

		if not self.player.alive:
			self.road.stop()

	def render(self, _screen):
		self.road.render(_screen)
		self.player.render(_screen)
		self.enemies.render(_screen)
		self.ui.render(_screen)