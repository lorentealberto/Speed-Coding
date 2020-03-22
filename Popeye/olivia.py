import pygame as py
import random
from timer import Timer
from corazon import Corazon
from gestor_animaciones import GestorAnimaciones

class Olivia(object):
	"""Objeto que representa a Olivia
		Parámetros:
			_lista_corazones -- Lista de corazones del nivel. Aquí se añadirá
				un nuevo corazón en la posición donde se encuentre el objeto
				en un tiempo aleatorio.""" 
	def __init__(self, _lista_corazones):
		#Cuerpo y posición del objeto
		self.bounds = py.Rect(240, 155, 0, 0)
		self.gestor_animaciones = GestorAnimaciones()
		self.bounds.width, self.bounds.height = self.gestor_animaciones.añadir_animacion("moviendose", self.gestor_animaciones.cargar_frames("olivia/", "walking", 3, 2), 200)
		self.bounds.y -= self.bounds.height
		
		#Velocidad del objeto
		self.speed = 1
		self.vx = self.speed

		#Relacionado con los corazones
		self.temporizador_lanzar_corazon = Timer(random.randrange(1200, 1500))
		self.lista_corazones = _lista_corazones
		
		#Renderizado
		self.hacia_izquierda = False

	def render(self, _screen):
		"""Dibuja el objeto en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujará."""
		self.gestor_animaciones.render(_screen, self.bounds, self.hacia_izquierda)

	def update(self, _dt):
		"""Actualiza el objeto.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde la última
					vez que se llamó a este método."""
		self.gestor_animaciones.update(_dt)
		self.mover()
		self.comprobar_bordes()
		self.lanzar_corazon(_dt)
		self.mirar_lados()

	def mirar_lados(self):
		"""Si la velocidad horizontal del objeto es negativa, el objeto mirará
			hacía la izquierda, a la derecha en caso contrario"""
		if self.vx < 0:
			self.hacia_izquierda = True
		elif self.vx > 0:
			self.hacia_izquierda = False

	def lanzar_corazon(self, _dt):
		"""Actualiza el temporizador del lanzamiento de corazones y lanza un
			nuevo corazón cada X tiempo.
			Parámetros:
				_dt -- Tiempo en milisegundos desde la última vez que se llamó
					al método."""
		self.temporizador_lanzar_corazon.update(_dt)

		if self.temporizador_lanzar_corazon.tick:
			self.temporizador_lanzar_corazon.delay = random.randrange(1000, 1500)
			self.lista_corazones.append(Corazon(self.bounds.center[0], self.bounds.center[1]))

	def mover(self):
		"""Mueve el objeto en base a su velocidad"""
		self.bounds.move_ip(self.vx, 0)

	def comprobar_bordes(self):
		"""Comprueba los bordes ficticios de la pantalla, para evitar que el
			objeto lance corazones en sitios inesperados."""
		if self.bounds.left <= 128:
			self.bounds.left =  128
			self.vx *= -1
		elif self.bounds.right >= 383:
			self.bounds.right = 383
			self.vx *= -1