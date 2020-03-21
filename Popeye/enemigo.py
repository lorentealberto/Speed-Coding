import pygame as py
from math import sqrt
from gestor_animaciones import GestorAnimaciones
class Enemigo(object):

	def __init__(self):
		self.bounds = py.Rect(298, 343, 25, 25)

		self.gestor_animaciones = GestorAnimaciones((self.bounds.x, self.bounds.y))

		self.bounds.width, self.bounds.height = self.gestor_animaciones.añadir_animacion("andar", self.gestor_animaciones.cargar_frames("brutus/", "walking", 3, 2), 200)

		self.bounds.y -= self.bounds.height
		self.velocidad = 2
		self.vx = 0
		self.escalera_seleccionada = None
		self.jugador_arriba = self.jugador_abajo = False
		self.hacia_derecha = False
		self.tamaño_pies = 10
		self.pies = py.Rect(self.bounds.x, self.bounds.y + self.bounds.height - self.tamaño_pies, self.bounds.width, self.tamaño_pies)

		self.gravedad = 1
		self.vy = 0
		self.sobre_suelo = False

	def render(self, _screen):
		#py.draw.rect(_screen, (255, 0, 0), self.bounds)
		#py.draw.rect(_screen, (200, 0, 0), self.pies, 1)
		self.mirar_lados()
		self.gestor_animaciones.render(_screen, self.bounds, self.hacia_derecha)

		#if self.escalera_seleccionada != None:
		#	py.draw.rect(_screen, (0, 255, 0), self.escalera_seleccionada)

	def mirar_lados(self):
		if self.vx < 0:
			self.hacia_derecha = True
		elif self.vx > 0:
			self.hacia_derecha = False

	def update(self, _dt, _player_bounds, _lista_plataformas, _lista_escaleras):
		self.gestor_animaciones.update(_dt)
		self.aplicar_gravedad()
		self.move(_player_bounds, _lista_escaleras)
		self.comprobar_jugador(_player_bounds)
		self.comprobar_escaleras(_lista_escaleras)
		self.comprobar_plataformas(_lista_plataformas)

	def aplicar_gravedad(self):
		if not self.sobre_suelo:
			self.vy += self.gravedad
		else:
			self.vy = 0

	def comprobar_plataformas(self, _lista_plataformas):
		self.sobre_suelo = False
		for plataforma in _lista_plataformas:
			if self.pies.colliderect(plataforma.bounds) and self.vy >= 0:
				self.sobre_suelo = True
				self.pies.bottom = plataforma.bounds.top
				self.bounds.bottom = self.pies.bottom

	def move(self, _player_bounds, _lista_escaleras):
		if self.bounds.bottom >= _player_bounds.top and self.bounds.bottom <= _player_bounds.bottom:
			if self.bounds.left > _player_bounds.right:
				self.vx = -self.velocidad
			elif self.bounds.right < _player_bounds.left:
				self.vx = self.velocidad
		else:
			self.seleccionar_escalera(_player_bounds, _lista_escaleras)
			if self.escalera_seleccionada.right < self.bounds.left:
				self.vx = -self.velocidad
			elif self.escalera_seleccionada.left > self.bounds.right:
				self.vx = self.velocidad

		self.bounds.move_ip(self.vx, self.vy)
		self.pies.x = self.bounds.x
		self.pies.y = self.bounds.y + (self.bounds.height - self.tamaño_pies)

	def seleccionar_escalera(self, _player_bounds, _lista_escaleras):
		menos_distancia = 999
		for escalera in _lista_escaleras:
			if _player_bounds.bottom > escalera.bounds.top:

				x2 = escalera.bounds.center[0]
				y2 = escalera.bounds.center[1]

				x1 = self.bounds.center[0]
				y1 = self.bounds.center[1]

				op1 = pow(x2 - x1, 2)
				op2 = pow(y2 - y1, 2)

				d = sqrt(op1 + op2)

				if d < menos_distancia:
					menos_distancia = d
					self.escalera_seleccionada = escalera.bounds

	def comprobar_jugador(self, _player_bounds):
		if _player_bounds.bottom < self.bounds.top:
			self.jugador_arriba = True
			self.jugador_abajo = False
		elif _player_bounds.top > self.bounds.bottom:
			self.jugador_abajo = True
			self.jugador_arriba = False
		else:
			self.jugador_arriba = self.jugador_abajo = False

	def comprobar_escaleras(self, _lista_escaleras):
		for escalera in _lista_escaleras:
			if self.jugador_arriba:
				if self.bounds.colliderect(escalera.bounds):
					self.bounds.bottom = escalera.bounds.top + 1
			elif self.jugador_abajo:
				if self.bounds.colliderect(escalera.bounds):
					self.bounds.bottom = escalera.bounds.bottom