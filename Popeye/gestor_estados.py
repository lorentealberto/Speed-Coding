from nivel_1 import Nivel_1

class GestorEstados(object):
	"""Gestiona los estados que hay dentro del juego."""
	def __init__(self):
		self.estados = [Nivel_1()]
		self.estado_actual = 0

	def update(self, _dt):
		"""Actualiza solo el estado actual del juego.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde que se
					ejecutó este método por última vez."""
		self.estados[self.estado_actual].update(_dt)

	def render(self, _screen):
		"""Dibuja los elementos del estado en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujarán los elementos."""
		self.estados[self.estado_actual].render(_screen)
