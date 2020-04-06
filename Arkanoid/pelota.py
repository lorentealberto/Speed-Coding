import random
from pixelsmash.funciones import cargar_img
#PELOTA REBOTE 30 274 41
class Pelota(object):
	def __init__(self):
		random.seed()
		self.img = cargar_img("elementos/pelota")
		self.bounds = self.img.get_rect()
		self.bounds.x = 150 
		self.bounds.y = 200
		
		self.velocidad = 3
		self.vx, self.vy = 0, -self.velocidad

		while self.vx == 0:
			self.vx = random.randrange(-self.velocidad, self.velocidad)

	def dibujar(self, _pantalla):
		_pantalla.blit(self.img, self.bounds)

	def actualizar(self, _dt, _jugador):
		self.gestionar_velocidad()
		self.mover()
		self.comprobar_marcos()
		self.comprobar_jugador(_jugador)
		self.fuera_pantalla(_jugador)

	def gestionar_velocidad(self):
		if self.vx < 0 and self.vx > -self.velocidad:
			self.vx -= 1
		elif self.vx > 0 and self.vx < self.velocidad:
			self.vx += 1

	def mover(self):
		self.bounds.move_ip(self.vx, self.vy)

	def comprobar_marcos(self):
		if self.bounds.left < 30:
			self.bounds.left = 30
			self.vx *= -1
		elif self.bounds.right > 274:
			self.bounds.right = 274
			self.vx *= -1

		if self.bounds.top < 12:
			self.bounds.top = 12
			self.vy *= -1

	def comprobar_jugador(self, _jugador):
		if self.bounds.colliderect(_jugador.bounds):
			self.bounds.bottom = _jugador.bounds.top
			self.vy *= -1

	def fuera_pantalla(self, _jugador):
		if self.bounds.bottom > 320:
			_jugador.matar()