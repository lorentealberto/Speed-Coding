import pygame as py

class Saco(object):
	"""Representa el saco que golpea al cubo."""
	def __init__(self):
		self.bounds = py.Rect((330, 160, 20, 20))
		self.img = py.image.load("resources/graphics/sprites/saco/saco.png").convert_alpha()
		self.bounds.width, self.bounds.height = self.img.get_width(), self.img.get_height()

		#TO-DO Aplicar funcionamiento

	def render(self, _screen):
		"""Dibuja el cubo en la pantalla en la posición indicada anteriormente.
			Parámetros:
				_screen -- Pantalla donde se dibujará"""
		_screen.blit(self.img, self.bounds)