import pygame as py
from timer import Timer

class Animacion(object):
	def __init__(self, _nombre, _frames, _velocidad, _posicion):
		self.nombre = _nombre
		self.frames = _frames
		self.velocidad = _velocidad
		self.frame_actual = 0
		self.posicion = _posicion
		self.timer = Timer(_velocidad)
		self.anchura = self.frames[0].get_width()
		self.altura = self.frames[0].get_height()

	def render(self, _screen, _bounds, _hacia_derecha):
		_screen.blit(py.transform.flip(self.frames[self.frame_actual], _hacia_derecha, False), _bounds)

	def update(self, _dt):
		self.timer.update(_dt)
		if self.timer.tick:
			self.frame_actual += 1
			if self.frame_actual > len(self.frames) - 1:
				self.frame_actual = 0

	def parar(self):
		self.timer.parar()
		self.frame_actual = 0