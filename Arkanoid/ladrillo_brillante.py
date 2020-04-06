import pygame as py

from pixelsmash.gestor_animaciones import GestorAnimaciones

class LadrilloBrillante(object):

	def __init__(self, _x, _y, _nombre_animacion, _frames):
		self.bounds = py.Rect(_x, _y, 0, 0)

		self.animaciones = GestorAnimaciones()
		self.bounds.width, self.bounds.height = self.animaciones.añadir_animacion("brillar", self.animaciones.cargar_frames(_nombre_animacion, _frames), 100, 1)
		self.brillar = False
		self.vivo = False
		self.vidas = 3


	def dibujar(self, _pantalla):
		self.animaciones.render(_pantalla, self.bounds, False)

	def actualizar(self, _dt):
		self.animaciones.update(_dt)
		
		if self.animaciones.terminada:
			self.brillar = False
			

	def golpear(self):
		if not self.brillar:
			self.animaciones.reproducir_animacion("brillar", 1)
			self.brillar = True

