import pygame as py
from pixelsmash.funciones import cargar_img
from pixelsmash.timer import Timer

#122 164 253 24

class MenuPrincipal(object):

	def __init__(self, _gestor_estados):
		self.fondo = cargar_img("fondos/intro")
		self.temporizador_parpadeo = Timer(250)
		self.parpadear = True
		self.gestor_estados = _gestor_estados

	def dibujar(self, _pantalla):
		_pantalla.blit(self.fondo, (0, 0))

		if self.parpadear:
			py.draw.rect(_pantalla, (6, 6, 6), (122, 164, 253, 24))

	def actualizar(self, _dt):
		self.temporizador_parpadeo.update(_dt)

		if self.temporizador_parpadeo.tick:
			self.parpadear = not self.parpadear

		self.iniciar_juego()

	def iniciar_juego(self):
		key = py.key.get_pressed()

		if key[py.K_RETURN]:
			self.gestor_estados.estado_actual = 1
