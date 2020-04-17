from pygame import Rect
from settings import DIFFICULTY
class Enemy(object):

	def __init__(self, _x, _img, _type):
		self.img = _img
		self.bounds = Rect(_x, -_img.get_height(), self.img.get_width(), self.img.get_height())
		self.alive = True
		self.speed = DIFFICULTY - 2
		self.vx = 0
		self.type = _type

	def update(self, _dt):
		self.bounds.move_ip(self.vx, self.speed)

	def render(self, _screen):
		_screen.blit(self.img, self.bounds)