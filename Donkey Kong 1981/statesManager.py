from mainMenu import MainMenu
from game import Game

class StatesManager(object):
	"""Gestor de estados del juego"""
	def __init__(self):
		"""Inicializa todos los estados del juego."""
		self.__states = [#MainMenu(self), 
						Game(self)]
		self.__currentState = 0

	def render(self, _screen):
		"""Dibuja en la pantalla el estado actual del juego.
			Parámetros:
				_screen -- Superficie donde se dibujará el estado."""
		self.__states[self.__currentState].render(_screen)

	def update(self, _dt):
		"""Actualiza el estado actual del juego.
			Parámetros:
				_dt -- Tiempo que ha transcurrido en milisegundos desde la última
					vez que se ejecutó este método."""
		self.__states[self.__currentState].update(_dt)

	def setState(self, _state):
		"""Establece un nuevo estado actual para el juego.
			Parámetros:
				_state -- Estado que se quiere poner."""
		self.__currentState = _state