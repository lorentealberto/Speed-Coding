import pygame as py
from math import sqrt
from gestor_animaciones import GestorAnimaciones
class Enemigo(object):
	"""Representa al enemigo (Brutus) dentro del juego"""
	def __init__(self):
		
		#Animaciones y cuerpo
		self.gestor_animaciones = GestorAnimaciones()
		self.bounds = py.Rect(298, 343, 0, 0)
		self.bounds.width, self.bounds.height = self.gestor_animaciones.añadir_animacion("andar", self.gestor_animaciones.cargar_frames("brutus/", "walking", 3, 2), 200)

		#Velocidades
		self.velocidad = 2
		self.vx, self.vy = 0, 0
		self.gravedad = 1

		#Inteligencia Artificial
		self.jugador_arriba = self.jugador_abajo = False
		self.escalera_seleccionada = None
		
		#Comportamiento plataformero
		self.tamaño_pies = 10
		self.pies = py.Rect(self.bounds.x, self.bounds.y + self.bounds.height - self.tamaño_pies, self.bounds.width, self.tamaño_pies)
		self.sobre_suelo = False

		#Renderizado
		self.hacia_izquierda = False
		
	def render(self, _screen):
		"""Dibuja la animación en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujará."""
		self.gestor_animaciones.render(_screen, self.bounds, self.hacia_izquierda)

	def update(self, _dt, _player_bounds, _lista_plataformas, _lista_escaleras):
		"""Actualiza todos los datos del objeto.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde que se
					ejecutó esté método por última vez.
				_player_bounds -- Posición donde se encuentra el jugador.
				_lista_plataformas -- Lista con todas las plataformas que hay en
					el nivel.
				_lista_escaleras -- Lista con todas las escaleras que hay en el
					nivel."""
		self.gestor_animaciones.update(_dt)
		self.mirar_lados()
		self.aplicar_gravedad()
		self.move(_player_bounds, _lista_escaleras)
		self.comprobar_jugador(_player_bounds)
		self.comprobar_escaleras(_lista_escaleras)
		self.comprobar_plataformas(_lista_plataformas)

	def mirar_lados(self):
		"""Si la velocidad horizontal del objeto es negativa, el objeto mirará
			hacía la izquierda, a la derecha en caso contrario"""
		if self.vx < 0:
			self.hacia_izquierda = True
		elif self.vx > 0:
			self.hacia_izquierda = False

	def aplicar_gravedad(self):
		"""Mientras que el objeto no esté tocando ninguna plataforma, la gravedad
			actuará sobre él."""
		if not self.sobre_suelo:
			self.vy += self.gravedad
		else:
			self.vy = 0

	def comprobar_plataformas(self, _lista_plataformas):
		"""Comprueba si el objeto está sobre alguna plataforma de la lista de
			plataformas.
			Parámetros:
				_lista_plataformas -- Lista de plataformas que hay en el nivel."""
		self.sobre_suelo = False
		for plataforma in _lista_plataformas:
			if self.pies.colliderect(plataforma.bounds) and self.vy >= 0:
				self.sobre_suelo = True
				self.pies.bottom = plataforma.bounds.top
				self.bounds.bottom = self.pies.bottom

	def move(self, _player_bounds, _lista_escaleras):
		"""Mueve al enemigo de una forma diferente de si se encuentra en la misma
			línea que el jugador o no. Si se encuentra en la misma altura que el
			jugador irá a por él, si por el caso contrarío se encuentra más arriba
			o más abajo, se activará una pequeña inteligencia artificial que encontrará
			la escalera más próxima al objeto que lleve hacía el jugador.
			Parámetros:
				_player_bounds -- Posición actual del jugador.
				_lista_escaleras -- Lista con todas las escaleras que hay en el
					nivel."""
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
		"""Seleccion la escalera que esté más próxima al objeto y que además
			lleve hacía el jugador.
			Parámetros:
				_player_bounds -- Posición actual del jugador
				_lista_escaleras -- Lista con todas las escaleras que hay en el
					nivel."""
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
		"""Comprueba la posición del jugador para saber si está más o ariba o
			más abajo del objeto.
			Parámetros:
				_player_bounds -- Posición actual del jugador."""
		if _player_bounds.bottom < self.bounds.top:
			self.jugador_arriba = True
			self.jugador_abajo = False
		elif _player_bounds.top > self.bounds.bottom:
			self.jugador_abajo = True
			self.jugador_arriba = False
		else:
			self.jugador_arriba = self.jugador_abajo = False

	def comprobar_escaleras(self, _lista_escaleras):
		"""Comprueba si el objeto está sobre alguna escalera
			Parámetros:
			_lista_escaleras -- Lista de escaleras del nivel"""
		for escalera in _lista_escaleras:
			if self.jugador_arriba:
				if self.bounds.colliderect(escalera.bounds):
					self.bounds.bottom = escalera.bounds.top + 1
			elif self.jugador_abajo:
				if self.bounds.colliderect(escalera.bounds):
					self.bounds.bottom = escalera.bounds.bottom