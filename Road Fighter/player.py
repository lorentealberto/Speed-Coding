import pygame as py
from pixelsmash.gestor_animaciones import GestorAnimaciones
from pixelsmash.funciones import cargar_img
from settings import WIDTH, HEIGHT

class Player(object):

	def __init__(self):
		self.animator = GestorAnimaciones()

		self.bounds = py.Rect(WIDTH // 2, HEIGHT - HEIGHT // 4, 0, 0)
		self.bounds.width, self.bounds.height = self.animator.añadir_animacion("recto", [cargar_img("jugador/recto", 2)], 0)
		self.bounds.x -= self.bounds.width // 2
		self.vx = 0
		self.speed = 2

		self.animator.añadir_animacion("explosion", self.animator.cargar_frames("jugador/explosion/explosion", 3, 2), 250, 1)
		self.animator.añadir_animacion("hacia_derecha", self.animator.cargar_frames("jugador/hacia_derecha", 3, 2), 200, 1)
		self.animator.añadir_animacion("hacia_izquierda", self.animator.cargar_frames("jugador/hacia_izquierda", 3, 2), 250, 1)
		self.animator.reproducir_animacion("recto", 0)
		self.alive = True


	def update(self, _dt, _road):
		self.animator.update(_dt)
		self.check_ended_animations()

		if self.alive:
			self.controls()
			self.move()

			self.on_road(_road)

	def render(self, _screen):
		self.animator.render(_screen, self.bounds)

	def move(self):
		self.bounds.move_ip(self.vx, 0)

	def controls(self):
		key = py.key.get_pressed()

		if key[py.K_RIGHT]:
			self.vx = self.speed
		elif key[py.K_LEFT]:
			self.vx = -self.speed
		else:
			self.vx = 0

	def on_road(self, _road):
		for road_piece in _road.array:
			if not (self.bounds.left > road_piece.bounds.left + 80 and self.bounds.right < road_piece.bounds.right - 80):
				self.explotar()

	def check_ended_animations(self):
		if (self.animator.ended_animation("hacia_derecha") or
			self.animator.ended_animation("hacia_izquierda")):
				self.explotar()

	def explotar(self):
		self.animator.reproducir_animacion("explosion", 1)
		self.alive = False