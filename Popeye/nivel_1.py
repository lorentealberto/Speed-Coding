import pygame as py
from player import Player
from plataforma import Plataforma
from escalera import Escalera
from maceta import Maceta
from cubo import Cubo
from saco import Saco
from olivia import Olivia
from enemigo import Enemigo



class Nivel_1(object):

	def __init__(self):
		self.img_nivel = self.cargar_fondo(2)
		self.corazones = []

		self.player = Player()

		self.olivia = Olivia(self.corazones)
		self.enemigo = Enemigo()

		
		self.plataformas = []
		self.bounds_plataformas = [(16, 216, 112, 8),
									(384, 216, 128, 8),
									(24, 280, 464, 8),
									(24, 344, 464, 8),
									(24, 344, 464, 8),
									(16, 408, 479, 15)]
		
		self.escaleras = []
		self.bounds_escaleras = [(32, 215, 48, 65),
								 (32, 279, 48, 65),
								 (32, 343, 48, 65),
								 (192, 343, 48, 65),
								 (272, 343, 48, 65),
								 (240, 279, 31, 65),
								 (432, 215, 48, 68),
								 (432, 279, 48, 65),
								 (432, 343, 48, 65)]
		self.macetas = []
		self.bounds_macetas = [(16, 264, 16, 16), (16, 328, 16, 16)]

		self.cubo = Cubo((245, 160, 20, 20))
		self.saco = Saco((330, 160, 20, 20))

		self.cargar_elementos_escenario()

	def update(self, dt = 0):
		self.player.update(dt, self.plataformas, self.escaleras)
		self.olivia.update(dt)
		self.enemigo.update(dt, self.player.bounds, self.plataformas, self.escaleras)
		self.actualizar_corazones(dt)
		self.coger_corazones()

	def actualizar_corazones(self, _dt):
		for corazon in self.corazones:
			corazon.update(_dt)
			if corazon.muerto:
				self.corazones.remove(corazon)

	def render(self, screen):
		screen.blit(self.img_nivel, (0, 0))
		self.player.render(screen)
		self.olivia.render(screen)
		self.enemigo.render(screen)
		self.render_elementos(screen)
		self.cubo.render(screen)
		self.saco.render(screen)
		self.render_corazones(screen)

	def render_corazones(self, _screen):
		for corazon in self.corazones:
			corazon.render(_screen)

	def render_elementos(self, _screen):
		self.render_plataformas(_screen)
		self.render_escaleras(_screen)
		self.render_macetas(_screen)

	def render_plataformas(self, _screen):
		for plataforma in self.plataformas:
			plataforma.render(_screen)

	def render_escaleras(self, _screen):
		for escalera in self.escaleras:
			escalera.render(_screen)

	def render_macetas(self, _screen):
		for maceta in self.macetas:
			maceta.render(_screen)

	def cargar_fondo(self, _escala):
		img_nivel = py.image.load("resources/graphics/nivel/fondo_1.png").convert_alpha()
		img_nivel = py.transform.scale(img_nivel, (_escala * img_nivel.get_width(), _escala * img_nivel.get_height()))
		return img_nivel

	def cargar_elementos_escenario(self):
		self.cargar_plataformas()
		self.cargar_escaleras()
		self.cargar_macetas()

	def cargar_escaleras(self):
		for bound in self.bounds_escaleras:
			self.escaleras.append(Escalera(bound))

	def cargar_plataformas(self):
		for bound in self.bounds_plataformas:
			self.plataformas.append(Plataforma(bound))

	def cargar_macetas(self):
		for bound in self.bounds_macetas:
			self.macetas.append(Maceta(bound))

	def coger_corazones(self):
		for corazon in self.corazones:
			if self.player.bounds.colliderect(corazon.bounds):
				self.player.corazones += 1
				self.corazones.remove(corazon)
