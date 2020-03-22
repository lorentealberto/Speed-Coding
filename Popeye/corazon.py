import pygame as py
import random
from gestor_animaciones import GestorAnimaciones
from timer import Timer

class Corazon(object):
	"""Representa un corazón lanzada por Olivia dentro del juego
		Parámetros:
			_x -- Posición X donde se iniciará el corazón.
			_y -- Posición Y donde se iniciará el corazón."""
	def __init__(self, _x, _y):
		#Cuerpo del corazón, utiliza las variables recibidas por parámetro.
		self.bounds = py.Rect(_x, _y, 5, 5)

		#Velocidades del objeto
		self.vx = random.randrange(-1, 1)
		self.vy = -2
		self.velocidad_caida_maxima = 5

		#Gravedad que se aplicará al objeto
		self.gravedad = 1

		#Bandera que sirve para indicar si el objeto debe ser borrado de la lista
		#que lo contiene o no.
		self.muerto = False
		
		#Se tiene que iniciar un pequeño gestor de animaciones para reproducir
		#para reproducir la animación que tiene el objeto.
		self.gestor_animaciones = GestorAnimaciones()

		#Se cambia la anchura y altura del cuerpo por la anchura y la altura
		#que obtenemos de la animación.
		self.bounds.width, self.bounds.height = self.gestor_animaciones.añadir_animacion("caer", self.gestor_animaciones.cargar_frames("corazon/", "corazon", 3, 2), 250)

		#Se crean múltiples temporizadores para evitar que el objeto se mueva
		#de forma descontrolada.
		self.temporizador_frenado = Timer(250)
		self.temporizador_gravedad = Timer(500)

		#Posición del suelo imaginario con el que chocará el objeto y se destruirá.
		self.suelo = 420

	def render(self, _screen):
		""""Se dibuja la animación
			Parámetros:
				_screen -- Pantalla donde se dibujará"""
		self.gestor_animaciones.render(_screen, self.bounds, False)

	def update(self, _dt):
		"""Actualiza el objeto
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde que se
					ejecuto este método por última vez."""
		self.gestor_animaciones.update(_dt)

		self.aplicar_gravedad(_dt)
		self.frenar(_dt)
		self.mover()
		self.comprobar_suelo()

	def aplicar_gravedad(self, _dt):
		"""Aplica la gravedad al objeto. No se aplica la gravedad de forma contínua
			para evitar que el objeto alcance una gran velocidad de caída en muy
			poco tiempo, si no que se va aplicando la gravedad de forma
			intermitente.
				Parámetros:
					_dt -- Tiempo en milisegundos desde que se ejecutó esté
						método por última vez."""
		self.temporizador_gravedad.update(_dt)
		
		if self.temporizador_gravedad.tick:
			self.vy += self.gravedad

		self.limitar_velocidad_caída()

	def frenar(self, _dt):
		"""Va frenando el objeto horizontalmente de forma intermitente.
			Parámetros:
				_dt -- Tiempo en milisegundos de que se ejcutó este método por
					última vez."""
		self.temporizador_frenado.update(_dt)

		if self.temporizador_frenado.tick:
			if self.vx < 0:
				self.vx += 1
			elif self.vx > 0:
				self.vx -= 1
			else:
				self.vx = 0

	def mover(self):
		"""Mueve el objeto utilizando las distintas velocidades"""
		self.bounds.move_ip(self.vx, self.vy)

	def comprobar_suelo(self):
		"""Comprueba que el objeto ha chocado contra el suelo"""
		if self.bounds.top > self.suelo:
			self.muerto = True

	def limitar_velocidad_caída(self):
		"""Limita la velocidad de caída para evitar que el objeto se acelere
			de forma incontrolada"""
		if self.vy > self.velocidad_caida_maxima:
			self.vy = self.velocidad_caida_maxima