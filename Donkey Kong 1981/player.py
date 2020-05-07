import pygame as py
from pixelsmash.animator import Animator
from pixelsmash.functions import load_img


class Player(object):
	"""Representa a Super Mario dentro del juego"""
	def __init__(self):
		"""Constructor"""

		# Partes del cuerpo
		self.__bounds = py.Rect(118, 431, 0, 0)
		self.__feet = py.Rect(0, 0, 18, 4)
		self.__body = py.Rect(0, 0, 16, 28)

		# Refertente a animator
		self.__animator = Animator()
		self.__animator.add_animation("idle", 0, "mario/mario_idle", 1, 2)
		self.__bounds.width, self.__bounds.height = self.__animator.add_animation("walk", 150, "mario/mario_walk", 2, 2)
		self.__animator.add_animation("onStairs", 100, "mario/mario_stair", 2, 2)
		self.__bounds.y -= self.__bounds.height

		# Velocidad actual
		self.__vx, self.__vy = 0, 0
		
		# Velocidad total
		self.__hSpeed = 2
		self.__vSpeed = 7

		# Referente a las plataformas
		self.__onGround = False
		self.__gravity = 1
		self.__onLadder = False

		# Referente a los gráficos
		self.__facingLeft = False
		
		# Indica si el objeto está vivo
		self.__alive = True

	def render(self, _screen):
		"""Si está vivo, dibuja el objeto en la pantalla.
			Parámetros:
				_screen -- Superficie donde se dibujará el objeto"""
		if self.__alive:
			self.__animator.render(_screen, self.__bounds, self.__facingLeft)

	def update(self, _dt, _level):
		"""Si el personaje está vivo, actualiza todos los componentes.
			Parámetros:
				_dt -- Tiempo que ha transcurrido en milisegundos desde la
					última vez que se llamó a este método.
				_level -- Referencia al nivel del juego para saber donde están
					las plataformas y las escaleras."""
		if self.__alive:
			self.__animator.update(_dt)
			self.__manageAnimations()

			self.__applyGravity()
			self.__controls()
			self.__move()
			self.__updateFeet()
			self.__updateBody()

			self.__checkPlatformsCollision(_level)
			self.__checkLadders(_level)

	def __applyGravity(self):
		"""Si el personaje no está tocando ninguna plataforma, aplicar gravedad
			para que caíga al suelo."""
		if not self.__onGround:
			self.__vy += self.__gravity
		else:
			self.__vy = 0

	def __controls(self):
		"""Gestiona las pulsaciones del teclado y realiza una función diferente
			dependiendo de la tecla que se haya pulsado."""
		key = py.key.get_pressed()

		if key[py.K_RIGHT]: # Flecha derecha
			self.__vx = self.__hSpeed
			self.__facingLeft = False
		elif key[py.K_LEFT]: # Flecha izquierda
			self.__vx = -self.__hSpeed
			self.__facingLeft = True
		else: # Ninguna flecha de dirección pulsada
			self.__vx = 0

		# Si se ha pulsado la tecla espacio y además el personaje está sobre el suelo
		if key[py.K_SPACE] and self.__onGround:
			self.__onGround = False
			self.__vy = -self.__vSpeed

		# Si el personaje está en frente de una escalera y se pulsa la tecla de
		# dirección arriba.
		if key[py.K_UP] and self.__onLadder:
			self.__onGround = False
			self.__vy = -self.__hSpeed
		# Si el personaje está en frente de una escalera pero pulsa la tecla de
		# dirección hacía abajo.
		elif key[py.K_DOWN] and self.__onLadder:
			self.__vy = self.__hSpeed
		else: # Si el personaje no está sobre ninguna escalera o no se está pulsando
				# arriba o abajo.
			self.__onGround = True

	def __move(self):
		"""Mueve al personaje en base a la velocidad actual"""
		self.__bounds.move_ip(self.__vx, self.__vy)

	def __manageAnimations(self):
		"""Gestiona las animaciones del jugador en base a los distintos eventos
			que se den por ejemplo, que el jugador esté parado o que esté en frente
			de una escalera."""
		if self.__onLadder:
			self.__animator.play_animation("onStairs")
			if self.__vy == 0:
				self.__animator.enableUpdating(False)
			else:
				self.__animator.enableUpdating(True)
		else:
			if self.__vx == 0:
				self.__animator.play_animation("idle")
			else:
				self.__animator.play_animation("walk")
				self.__animator.enableUpdating(True)

	def __checkPlatformsCollision(self, _level):
		"""Comprueba que el jugador choque contra alguna de las piezas del suelo
			para poder saber si el jugador está sobre el suelo o no.
			Parámetros:
				_level -- Referencia al nivel. En el nivel están guardadas todas
					las piezas del suelo."""
		self.__onGround = False
		for platform in _level.getFloor():
			if self.__feet.colliderect(platform):
				if self.__vy > 0:
					self.__bounds.bottom = platform.top
					self.__onGround = True

	def __checkLadders(self, _level):
		"""Comprueba que el jugador esté en frente de alguna escalera.
			Parámetros:
				_level -- Referencia al nivel. El nivel guarda la posición
					de todas las escaleras del juego."""
		self.__onLadder = False
		for ladder in _level.getLadders():
			if self.__body.colliderect(ladder):
				self.__onLadder = True
				self.__onGround = True

	# Estos dos métodos actualizan las distintas partes del cuerpo en base a
	# los 'bounds'. No es necesario crear estas subpartes del cuerpo para que
	# el juego funcione correctamente, pero sí añade algo de realismo. Si
	# estas partes no estuvieran definidas, el personaje estaría sobre el suelo
	# con tan solo tocar una plataforma con la cabeza y, estaría en frente de
	# una escalera aunque la imagen únicamente tuviera un píxel en frente.
	def __updateFeet(self):
		self.__feet.x, self.__feet.y = self.__bounds.x + 2, self.__bounds.y + 28
	def __updateBody(self):
		self.__body.x, self.__body.y = self.__bounds.x + 4, self.__bounds.y

	# Getters & Setters
	def getBounds(self):
		return self.__body

	def setAlive(self, _alive):
		self.__alive = _alive