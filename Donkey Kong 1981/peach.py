from pygame import Rect
from pixelsmash.animator import Animator
from pixelsmash.functions import load_img
from pixelsmash.timer import Timer

class Peach(object):
	"""Objeto que representa a la princesa Peach"""
	def __init__(self):
		"""Constructor"""
		self.__inimator = Animator()

		self.__bounds = Rect(250, 0, 0, 0)
		self.__bounds.size = self.__inimator.add_animation("moving", 500, "peach/peach", 2, 2)
		self.__bounds.bottom = 79

		# Elementos necesarios para mostrar el mensaje de HELP cada cierto tiempo
		self.__timer = Timer(550)
		self.__help = load_img("misc/help", 2)
		self.__showHelp = True

	def update(self, _dt):
		"""Actualiza todos los elementos del objeto.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde la última
					vez que se llamó el método."""
		self.__inimator.update(_dt)
		self.__timer.update(_dt)

		# Muestra u oculta el MSG de HELP cada vez que el temporizador emite un
		# pulso.
		if self.__timer.getTick():
			self.__showHelp = not self.__showHelp

	def render(self, _screen):
		"""Dibuja todos las partes que componen el objeto en la pantalla.
			Parámetros:
				_screen -- Superficie donde se dibujarán los elementos."""
		self.__inimator.render(_screen, self.__bounds)

		# Dibuja o no el mensaje de HELP en función del valor de la bandera
		# 'showHelp'.
		if self.__showHelp:
			_screen.blit(self.__help, (290, 25))