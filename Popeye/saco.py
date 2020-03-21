import pygame as py

class Saco(object):

	def __init__(self, _bounds):
		self.bounds = py.Rect(_bounds)
		self.img = py.image.load("resources/graphics/sprites/saco/saco.png").convert_alpha()
		#self.img = py.transform.scale(self.img, (2 * self.img.get_width(), 2 * self.img.get_height()))
		self.bounds.width, self.bounds.height = self.img.get_width(), self.img.get_height()

	def render(self, _screen):
		#py.draw.rect(_screen, (0, 0, 200), self.bounds, 1) 
		_screen.blit(self.img, self.bounds)