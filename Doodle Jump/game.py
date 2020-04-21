from player import Player
from platforms_manager import PlatformsManager

class Game(object):

	def __init__(self, _states_manager):
		self.player = Player()
		self.platforms_manager = PlatformsManager()

	def render(self, _screen):
		self.player.render(_screen)
		self.platforms_manager.render(_screen)

	def update(self, _dt):
		self.player.update(_dt)
		self.platforms_manager.update(_dt, self.player)