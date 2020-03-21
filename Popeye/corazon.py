import pygame as py
import random
from gestor_animaciones import GestorAnimaciones
from timer import Timer

class Corazon(object):

	def __init__(self, _x, _y):
		self.bounds = py.Rect(_x, _y, 5, 5)
		self.vx = random.randrange(-1, 1)
		self.vy = -2
		self.muerto = False
		self.gravedad = 1
		self.velocidad_caida_maxima = 5

		self.gestor_animaciones = GestorAnimaciones((self.bounds.x, self.bounds.y))
		self.bounds.width, self.bounds.height = self.gestor_animaciones.añadir_animacion("caer", self.gestor_animaciones.cargar_frames("corazon/", "corazon", 3, 2), 250)

		self.temporizador_frenado = Timer(250)
		self.temporizador_gravedad = Timer(500)

	def render(self, _screen):
		#py.draw.rect(_screen, (0, 0, 255), self.bounds)
		self.gestor_animaciones.render(_screen, self.bounds, False)

	def update(self, _dt):
		self.aplicar_gravedad(_dt)
		self.gestor_animaciones.update(_dt)
		self.bounds.move_ip(self.vx, self.vy)

		if self.bounds.top > 420:
			self.muerto = True

	def aplicar_gravedad(self, _dt):
		self.temporizador_gravedad.update(_dt)
		if self.temporizador_gravedad.tick:
			self.vy += self.gravedad

		if self.vy > self.velocidad_caida_maxima:
			self.vy = self.velocidad_caida_maxima

	def frenar(self, _dt):
		self.temporizador_frenado.update(_dt)
		if self.temporizador_frenado.tick:
			if self.vx < 0:
				self.vx += 1
			elif self.vx > 0:
				self.vx -= 1