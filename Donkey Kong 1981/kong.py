import random
from pygame import Rect
from pixelsmash.animator import Animator
from pixelsmash.array import Array

from barrel import Barrel

class Kong(object):
	"""Objeto que representa a Donkey Kong"""
	def __init__(self):
		"""Constructor"""
		random.seed()

		# Configuración del cuerpo del objeto.
		self.__bounds = Rect(85, 0, 0, 0)
		self.__bounds.bottom = 127

		# Configuración del objeto 'Animator'.
		self.__animator = Animator()
		self.__bounds.width, self.__bounds.height = self.__animator.add_animation("angry", 500, "kong/kong_angry", 2, 2)
		self.__animator.add_animation("take_barrel", 750, "kong/kong_take_barrel", 2, 2)
		self.__animator.add_animation("idle", 0, "kong/kong_idle", 1, 2)
		self.__animator.play_animation("angry", 1)

		# Array de barriles.
		self.__barrels = Array()
		
	def update(self, _dt, _level, _player):
		"""Actualiza todos los componentes del objeto.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde que se
					ejecutó este método por última vez.
				_level -- Nivel del juego, este objeto no necesita procesar el
					nivel, pero sí lo debe pasar hacía los barriles ya que éstos
					sí lo necesitan procesar.
				_player -- Jugador (Mario) al igual que pasaba con el nivel,
					el objeto no es necesario para el buen funcionamiento del
					mono (Donkey Kong), pero sí es necesario pasarlo a los
					barriles."""
		self.__animator.update(_dt)
		self.__manageAnimations()

		# Actualiza la lista de barriles
		self.__barrels.update(_dt, _level.getFloor())
		# Si el jugador choca con algún barril
		if self.__barrels.intersect(_player.getBounds()):
			_player.setAlive(False)

	def render(self, _screen):
		"""Dibuja en la pantalla todos los componentes del objeto.
			Parámetros:
				_screen -- Superficie donde se dibujarán los componentes."""
		self.__animator.render(_screen, self.__bounds)
		self.__barrels.render(_screen)

	def __manageAnimations(self):
		"""Gestiona las distintas animaciones que tiene el objeto.
			No hace falta explicar qué hace cada parte porque el nombre
			de los métodos son lo suficientemente descriptivos."""
		if self.__animator.animationHasEndedPlaying("take_barrel"):
			self.__animator.resetCurrentAnimation()
			self.__barrels.add_element(Barrel(111, 104))
			self.__animator.play_animation("angry", random.randrange(1, 4))
		elif self.__animator.animationHasEndedPlaying("angry"):
			self.__animator.resetCurrentAnimation()
			self.__animator.play_animation("take_barrel", 1)

