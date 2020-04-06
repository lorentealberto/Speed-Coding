import pygame as py
from pixelsmash.gestor_animaciones import GestorAnimaciones
from pixelsmash.funciones import cargar_img

class Jugador(object):
	def __init__(self):
		self.graficos = GestorAnimaciones()

		self.bounds = py.Rect(140 , 291, 0, 0)
		self.graficos.añadir_animacion("muerte", self.graficos.cargar_frames("jugador/muerte_jugador", 3), 200)
		self.bounds.width, self.bounds.height = self.graficos.añadir_animacion("normal", [cargar_img("jugador/jugador_normal")], 0)
		
		self.vx = 0
		self.velocidad = 4
		self.vivo = True

	def render(self, _pantalla):
		self.graficos.render(_pantalla, self.bounds, False)

	def actualizar(self, _dt):
		self.graficos.update(_dt)
		if self.vivo:
			self.controles()
			self.mover()
			self.comprobar_bordes()

	def controles(self):
		tecla = py.key.get_pressed()

		if tecla[py.K_RIGHT]:
			self.vx = self.velocidad
		elif tecla[py.K_LEFT]:
			self.vx = -self.velocidad
		else:
			self.vx = 0

	def mover(self):
		self.bounds.move_ip(self.vx, 0)

	def comprobar_bordes(self):
		#30 274
		if self.bounds.left <= 30:
			self.bounds.left = 30
			self.vx = 0
		elif self.bounds.right >= 274:
			self.bounds.right = 274
			self.vx = 0

	def matar(self):
		if self.graficos.animacion_actual != "muerte":
			self.graficos.reproducir_animacion("muerte", 1)
		self.vivo = False