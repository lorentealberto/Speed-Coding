from level import Level
from player import Player
from kong import Kong
from peach import Peach

class Game(object):
	def __init__(self, _sm):
		"""Inicializa todos los componentes del estado.
			Parámetros:
				_sm -- Gestor de estados por si se quiere moverse entre estados."""
		self.__level = Level()
		self.__player = Player()
		self.__kong = Kong()
		self.__peach = Peach()
	
	def render(self, _screen):
		"""Dibuja todos los compones del juego.
			Parámetros:
				_screen -- Superficie donde se dibujarán los componentes."""
		self.__level.render(_screen)
		self.__player.render(_screen)
		self.__kong.render(_screen)
		self.__peach.render(_screen)
	
	def update(self, _dt):
		"""Actualiza todos los componentes.
			Parámetros:
				_dt -- Tiempo que ha transcurrido en milisegundos que ha
					transcurrido desde la última vez que se ejecutó este método."""
		self.__player.update(_dt, self.__level)
		self.__kong.update(_dt, self.__level, self.__player)
		self.__peach.update(_dt)