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
	"""Primer nivel del juego"""
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

		self.cubo = Cubo()
		self.saco = Saco((330, 160, 20, 20))

		self.cargar_elementos_escenario()

	def update(self, dt = 0):
		"""Actualiza todos los elementos del primer nivel.
			Parámetros:
			dt -- Tiempo en milisegundos que ha transcurrido desde que se llamó
				este método por última vez. Tomará cero como valor por defecto,
				en caso de que no se le pase el tiempo real."""
		self.player.update(dt, self.plataformas, self.escaleras)
		self.olivia.update(dt)
		self.enemigo.update(dt, self.player.bounds, self.plataformas, self.escaleras)
		self.actualizar_corazones(dt)
		self.coger_corazones()

	def actualizar_corazones(self, _dt):
		"""Actualiza la lista de corazones del nivel.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde que se
					llamó a este método por última vez."""
		for corazon in self.corazones:
			corazon.update(_dt)
			if corazon.muerto:
				self.corazones.remove(corazon)

	def render(self, screen):
		"""Dibuja todos los elementos del nivel en la pantalla.
			Parámetros:
				screen -- Pantalla donde se dibujarán los elementos."""
		screen.blit(self.img_nivel, (0, 0))
		self.player.render(screen)
		self.olivia.render(screen)
		self.enemigo.render(screen)
		self.cubo.render(screen)
		self.saco.render(screen)
		self.render_corazones(screen)

	def render_corazones(self, _screen):
		"""Dibuja todos los corazones del nivel en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujarán"""
		for corazon in self.corazones:
			corazon.render(_screen)

	def render_plataformas(self, _screen):
		"""Dibuja todas las plataformas del nivel en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujarán"""
		for plataforma in self.plataformas:
			plataforma.render(_screen)

	def render_escaleras(self, _screen):
		"""Dibuja todas las escaleras del nivel en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujarán"""
		for escalera in self.escaleras:
			escalera.render(_screen)

	def render_macetas(self, _screen):
		"""Dibuja todas las macetas del nivel en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujarán"""
		for maceta in self.macetas:
			maceta.render(_screen)

	def cargar_fondo(self, _escala):
		"""Carga el fondo del nivel.
			Parámetros:
				_escala -- Escala del fondo.
			Devuelve la imagen del nivel."""
		img_nivel = py.image.load("resources/graphics/nivel/fondo_1.png").convert_alpha()
		img_nivel = py.transform.scale(img_nivel, (_escala * img_nivel.get_width(), _escala * img_nivel.get_height()))
		return img_nivel

	def cargar_elementos_escenario(self):
		"""Carga todos los elementos del nivel"""
		self.cargar_plataformas()
		self.cargar_escaleras()
		self.cargar_macetas()

	def cargar_escaleras(self):
		"""Carga todas las escaleras del nivel"""
		for bound in self.bounds_escaleras:
			self.escaleras.append(Escalera(bound))

	def cargar_plataformas(self):
		"""Carga todas las plataformas del nivel"""
		for bound in self.bounds_plataformas:
			self.plataformas.append(Plataforma(bound))

	def cargar_macetas(self):
		for bound in self.bounds_macetas:
			"""Carga todas las macetas del nivel"""
			self.macetas.append(Maceta(bound))

	def coger_corazones(self):
		"""Se encarga de gestionar la colisión entre el jugador y los corazones
			que lanza olivia.
			TO-DO: Aplicar un comportamiento correcto."""
		for corazon in self.corazones:
			if self.player.bounds.colliderect(corazon.bounds):
				self.player.corazones += 1
				self.corazones.remove(corazon)
