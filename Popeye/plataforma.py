import pygame as py
 
class Plataforma(object):
	"""Objeto que representa una plataforma dentro del juego. Este objeto no tiene
		ningún gráfico, simplemente es una posición.
		Parámetros:
			_bounds -- Posición del objeto."""
	def __init__(self, _bounds):
		self.bounds = py.Rect(_bounds)