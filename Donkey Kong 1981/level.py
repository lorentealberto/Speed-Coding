import pygame as py
from pixelsmash.functions import load_img


class Level(object):
	"""Nivel del juego"""
	
	def __init__(self):
		"""Constructor"""
		self.__background = load_img("backgrounds/level", 2)

		self.__floor = []
		self.__ladders = []
		
		self.__loadFloor()
		self.__loadLadders()

	def render(self, _screen):
		"""Dibuja el nivel en la pantalla.
			Parámetros:
				_screen -- Superficie donde se dibujará."""
		_screen.blit(self.__background, (0, 0))

	def __loadLadders(self):
		"""Carga todas las escaleras del nivel."""
		self.__addLadder((416, 376, 16, 48),
			(240, 310, 16, 58),
			(112, 316, 16, 46),
			(272, 250, 16, 58),
			(192, 192, 16, 54),
			(352, 134, 16, 50),
			(96, 196, 16, 46))

	def __loadFloor(self):
		"""Carga todas las partes de suelo del nivel."""
		self.__addFloor((32, 432, 240, 16),
						(272, 430, 48, 16),
						(32, 432, 240, 16),
						(272, 430, 48, 16),
						(320, 428, 48, 16),
						(368, 426, 48, 16),
						(416, 424, 48, 16),
						(464, 422, 48, 16),
						(416, 376, 48, 16),
						(368, 374, 48, 16),
						(320, 372, 48, 16),
						(272, 370, 48, 16),
						(224, 368, 48, 16),
						(176, 366, 48, 16),
						(128, 364, 48, 16),
						(80, 362, 48, 16),
						(48, 360, 32, 16),
						(80, 316, 48, 16),
						(128, 314, 48, 16),
						(176, 312, 48, 16),
						(224, 310, 48, 18),
						(272, 308, 16, 18),
						(288, 308, 32, 16),
						(320, 306, 48, 16),
						(368, 304, 64, 16),
						(368, 254, 32, 16),
						(320, 252, 48, 16),
						(272, 250, 48, 16),
						(224, 248, 48, 16),
						(176, 246, 48, 16),
						(128, 244, 48, 16),
						(80, 242, 48, 16),
						(16, 240, 64, 16),
						(64, 196, 48, 16),
						(112, 194, 48, 16),
						(160, 192, 48, 16),
						(208, 190, 64, 16),
						(272, 188, 32, 16),
						(304, 186, 48, 16),
						(352, 184, 80, 16),
						(352, 134, 32, 16),
						(304, 132, 48, 16),
						(272, 130, 32, 16),
						(48, 128, 224, 16))

	def __addFloor(self, *_floor):
		"""Añade una múltiples partes del suelo a la lista de partes del objeto
			para así componer un único objeto.
			Parámetros:
				*_floor -- Distintas partes de suelo que se añadirán a la lista
					de partes del suelo para componer todas las plataformas
					del nivel."""
		for fp in _floor:
			self.__floor.append(py.Rect(fp))

	def __addLadder(self, *_ladders):
		"""Añade múltiples escaleras a la lista de escaleras del juego.
			Parámetros:
			*_ladders -- Múltiples escaleras que se añadirán."""
		for ladder in _ladders:
			self.__ladders.append(py.Rect(ladder))

	# Getters & Setters
	def getFloor(self):
		return self.__floor

	def getLadders(self):
		return self.__ladders