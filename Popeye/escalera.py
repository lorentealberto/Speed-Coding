from pygame import Rect

class Escalera(object):
	"""Objeto que representa una escalera dentro del juego. Este objeto no tiene
		ningún gráfico, simplemente es una posición.
		Parámetros:
			_bounds -- Posición del objeto."""
	def __init__(self, _bounds):
		self.bounds = Rect(_bounds)