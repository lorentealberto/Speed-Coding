import random
from pixelsmash.functions import load_img
from platform import Platform
from settings import WIDTH, HEIGHT

class PlatformsManager(object):

	def __init__(self):
		random.seed()
		self.platforms = []
		self.platform_img = load_img("platform")
		self.generate_start_platforms()

	def render(self, _screen):
		for platform in self.platforms:
			platform.render(_screen)

	def update(self, _dt, _player):
		self.check_platforms_land(_player)
		for platform in self.platforms:
			platform.update(_dt, _player)
			if self.clear_platforms(platform):
				self.generate_platform()

	def clear_platforms(self, _platform):
		if not _platform.on_screen:
			self.platforms.remove(_platform)
			return True
		return False

	def generate_platform(self):
		self.platforms.append(Platform(self.platform_img, random.randrange(0, WIDTH - self.platform_img.get_width()), -50))

	def generate_start_platforms(self):
		for i in range(HEIGHT // 50):
			self.platforms.append(Platform(self.platform_img, random.randrange(0, WIDTH - self.platform_img.get_width()), i * 50))

	def check_platforms_land(self, _player):
		for platform in self.platforms:
			if _player.bounds.colliderect(platform.bounds) and _player.vy > 0:
				if _player.bounds.bottom > platform.bounds.top:
					_player.jump()
