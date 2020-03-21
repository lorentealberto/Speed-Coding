import pygame as py
import random
from timer import Timer
from corazon import Corazon
from gestor_animaciones import GestorAnimaciones
class Olivia(object):

	#128 izquierda
	#383 derecha
	def __init__(self, _lista_corazones):
		self.bounds = py.Rect(240, 155, 25, 25)
		
		self.speed = 1
		self.vx = self.speed

		self.temporizador_lanzar_corazon = Timer(random.randrange(1200, 1500))
		self.lista_corazones = _lista_corazones
		self.hacia_derecha = False

		self.gestor_animaciones = GestorAnimaciones((self.bounds.x, self.bounds.y))
		self.bounds.width, self.bounds.height = self.gestor_animaciones.añadir_animacion("moviendose", self.gestor_animaciones.cargar_frames("olivia/", "walking", 3, 2), 200)
		self.bounds.y -= self.bounds.height

	def render(self, _screen):
		#py.draw.rect(_screen, (255, 0, 0), self.bounds)
		self.gestor_animaciones.render(_screen, self.bounds, self.hacia_derecha)

	def update(self, _dt):
		self.gestor_animaciones.update(_dt)
		self.mover()
		self.comprobar_bordes()
		self.lanzar_corazon(_dt)

	def lanzar_corazon(self, _dt):
		self.temporizador_lanzar_corazon.update(_dt)

		if self.temporizador_lanzar_corazon.tick:
			self.temporizador_lanzar_corazon.delay = random.randrange(1000, 1500)
			self.lista_corazones.append(Corazon(self.bounds.center[0], self.bounds.center[1]))

	def mover(self):
		self.elegir_animacion()
		self.bounds.move_ip(self.vx, 0)

	def comprobar_bordes(self):
		if self.bounds.left <= 128:
			self.bounds.left =  128
			self.vx *= -1
		elif self.bounds.right >= 383:
			self.bounds.right = 383
			self.vx *= -1

	def elegir_animacion(self):
		if self.vx < 0:
			self.hacia_derecha = True
		elif self.vx > 0:
			self.hacia_derecha = False