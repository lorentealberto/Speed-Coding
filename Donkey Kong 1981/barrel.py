from pygame import Rect
from pixelsmash.animator import Animator

class Barrel(object):
	"""Objeto que representa un barril dentro del juego.
		Parámetros:
			_x -- Posición X donde se colocará inicialmente el barril.
			_y -- Posición Y donde se colocará inicialmente el barril."""
	def __init__(self, _x, _y):
		# Crea un nuevo objeto del tipo 'Animator' del motor PixelSmash
		self.__animator = Animator()

		# Crea un nuevo cuerpo para el objecto con la posición que hemos pasado
		# como parámetro, pero aún no le damos un tamaño.
		self.__bounds = Rect(_x, _y, 0, 0)
		
		# Añadimos una nueva animación al objecto animador y usamos el tamaño
		# del objeto devuelvo para terminar de configurar el cuerpo de nuestro
		# objecto.
		self.__bounds.size = self.__animator.add_animation("fall", 300, "barrel/barrel_fall", 2, 2)

		# Añadimos una nueva animación a nuestro objeto animador, aunque esta vez
		# no necesitamos actualizar el tamaño de nuestro objeto.
		self.__animator.add_animation("move", 300, "barrel/barrel_move", 2, 2)

		# Velocidad que tendrá el objeto.
		#	VX -- Velocidad actual horizontal
		#	VY -- Velocidad actual vertical
		self.__vx, self.__vy = 1, 0

		# Constante para modificar la velocidad actual del objeto
		self.__speed = 3

		# Gravedad que se aplicará al objeto
		self.__gravity = 1

		# La velocidad vertical del objeto no podrá ser superior
		# a la velocidad máxima
		self.__maxFallSpeed = 5

		# Comprueba si el objeto sobre alguna plataforma
		self.__onGround = False

		# Guarda la plataforma que está tocando el objeto
		self.__oldPlatform = None

		# Si el objeto no está vivo, el sistema lo borrará
		self.__alive = True

	def render(self, _screen):
		"""Dibuja el objeto en la pantalla.
			Parámetros:
				_screen -- Superficie donde se dibujará el objeto."""
		self.__animator.render(_screen, self.__bounds)

	def update(self, _dt, _resources_needed):
		"""Actualiza todos los componentes del objeto.
			Parámetros:
				_dt -- Tiempo que ha transcurrido (MS) desde que se llamó a
					método por última vez.
				_resources_needed -- Parámetro utilizado por el componente
					'array' de PixelSmash. No tiene ningún tipo definido.
					Es decir, este parámetro podría significar cualquier cosa
					que utilice el objeto."""
		self.__animator.update(_dt)
		self.__manageAnimations()
		self.__applyGravity()
		self.__move()
		self.__checkFloor(_resources_needed)
		self.__checkBounds()

	def __manageAnimations(self):
		"""Gestiona las animaciones del objeto 'animator' en base a las propiedades
			actuales del objeto."""
		if self.__vx != 0: # Si el objeto se está moviendo horizontalmente.
			self.__bounds.size = self.__animator.play_animation("move")
		else:
			# Si el objeto tiene una determinada velocidad de caída.
			if self.__vy >= self.__maxFallSpeed:
				self.__animator.play_animation("fall")
				self.__falling = True

	def __checkFloor(self, _floor):
		"""Comprueba todas las plataformas del nivel para ver si el barril está
			sobre alguna de ellas.
			Parámetros:
				_floor -- Este objeto está compuesto por todas las piezas
					individuales del suelo."""
		self.__onGround = False
		for floor in _floor:
			# Si el cuerpo del objeto está chocando con alguna parte del suelo
			if self.__bounds.colliderect(floor):
				self.__onGround = True
				self.__bounds.bottom = floor.top

				# Guarda la plataforma con la que ha chocado para que solo
				# se ejecute una única vez el evento.
				if floor != self.__oldPlatform:
					self.__oldPlatform = floor
					if self.__vy == self.__maxFallSpeed:
						self.__speed *= -1

	def __applyGravity(self):
		"""Aplica la gravedad al objeto"""
		if not self.__onGround:
			self.__vy += self.__gravity
		else:
			self.__vy = 0

		if self.__vy > self.__maxFallSpeed:
			self.__vy = self.__maxFallSpeed

	def __move(self):
		"""Mueve el objeto"""
		if not self.__onGround:
			self.__vx = 0
		else:
			self.__vx = self.__speed

		self.__bounds.move_ip(self.__vx, self.__vy)

	def __checkBounds(self):
		"""Comprueba que el objeto no se haya salido de la pantalla.
			Si se ha salido, se marcará para ser eliminado."""
		if self.__bounds.top > 600:
			self.__alive = False

	# Getters & Setters
	def isAlive(self):
		return self.__alive

	def getBounds(self):
		return self.__bounds