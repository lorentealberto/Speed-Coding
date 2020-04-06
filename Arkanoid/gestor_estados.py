
from menu_principal import MenuPrincipal
from juego import Juego

class GestorEstados(object):

	def __init__(self):
		self.estados = [
			#MenuPrincipal(self),
			Juego(self)]
		self.estado_actual = 0

	def actualizar(self, _dt):
		self.estados[self.estado_actual].actualizar(_dt)

	def dibujar(self, _pantalla):
		self.estados[self.estado_actual].dibujar(_pantalla)