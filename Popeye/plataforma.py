import pygame as py

class Plataforma(object):

	def __init__(self, _bounds):
		self.bounds = py.Rect(_bounds)

	def render(self, _screen):
		#py.draw.rect(_screen, (255, 0, 0), self.bounds, 1)
		pass
