from pygame import Rect
from settings import HEIGHT, DIFFICULTY
class RoadPiece(object):

	def __init__(self, _img, _x, _y):
		self.img = _img
		self.bounds = Rect(_x, _y, self.img.get_width(), self.img.get_height())
		self.alive = True
		self.road_speed = DIFFICULTY

	def render(self, _screen):
		_screen.blit(self.img, self.bounds)

	def update(self, _dt):
		self.bounds.move_ip(0, self.road_speed)

		if self.bounds.top > HEIGHT:
			self.alive = False