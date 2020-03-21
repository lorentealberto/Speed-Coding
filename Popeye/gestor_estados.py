from nivel_1 import Nivel_1

class GestorEstados(object):

	def __init__(self):
		self.estados = [Nivel_1()]
		self.estado_actual = 0

	def update(self, dt):
		self.estados[self.estado_actual].update(dt)

	def render(self, screen):
		self.estados[self.estado_actual].render(screen)
