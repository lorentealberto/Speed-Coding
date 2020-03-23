import pygame as py
class Cubo(object):
	"""Representa el cubo que cae sobre brutus dentro del juego."""
	def __init__(self):
		self.bounds = py.Rect(245, 160, 20, 20)
		self.img = py.image.load("resources/graphics/sprites/cubo/cubo.png").convert_alpha()
		self.bounds.width, self.bounds.height = self.img.get_width(), self.img.get_height()

		#TO-DO Aplicar funcionamiento

	def render(self, _screen):
		"""Dibuja el cubo en la pantalla en la posición indicada anteriormente.
			Parámetros:
				_screen -- Pantalla donde se dibujará"""
		_screen.blit(self.img, self.bounds)