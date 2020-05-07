import pygame as py
from pixelsmash.functions import load_img

class MainMenu(object):

	def __init__(self, _sm):
		"""Inicializa todos los componentes del estado.
			Parámetros:
				_sm -- Gestor de estados por si se quiere moverse entre estados."""
		self.__gfx = load_img("backgrounds/main_menu", 2)
		self.__statesManager = _sm

	def render(self, _screen):
		"""Dibuja todos los compones del juego.
			Parámetros:
				_screen -- Superficie donde se dibujarán los componentes."""
		_screen.blit(self.__gfx, (0, 0))

	def update(self, _dt):
		"""Comprueba la pulsación de la teclas para moverse entre estados.
			Parámetros:
				_dt -- Tiempo que ha transcurrido en milisegundos que ha
					transcurrido desde la última vez que se ejecutó este método."""
		key = py.key.get_pressed()

		if key[py.K_RETURN]:
			self.__statesManager.setState(1)