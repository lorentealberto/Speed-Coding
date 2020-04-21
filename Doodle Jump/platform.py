from pixelsmash.functions import load_img
from settings import HEIGHT
class Platform(object):

	def __init__(self, _img, _x, _y):
		self.img = _img
		self.bounds = _img.get_rect()
		self.bounds.x = _x
		self.bounds.y = _y
		self.on_screen = True

	def render(self, _screen):
		_screen.blit(self.img, self.bounds)

	def update(self, _dt, _player):
		if _player.bounds.top < HEIGHT // 4:
			self.bounds.move_ip(0, 6)

		self.check_on_screen()

	def check_on_screen(self):
		if self.bounds.top > HEIGHT:
			self.on_screen = False
