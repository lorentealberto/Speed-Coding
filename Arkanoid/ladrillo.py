import pygame as py

class Ladrillo(object):

	def __init__(self, _x, _y, _img):
		self.bounds = _img.get_rect()
		self.bounds.x = _x
		self.bounds.y = _y
		self.img = _img
		self.vivo = False
		self.brillar = False
		self.vidas = 1

	def dibujar(self, _pantalla):
		_pantalla.blit(self.img, self.bounds)

	def actualizar(self, _dt):
		pass

	def golpear(self):
		pass