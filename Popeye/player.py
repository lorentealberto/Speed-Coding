import pygame as py
from gestor_animaciones import GestorAnimaciones
from timer import Timer

class Player(object):

	def __init__(self):
		x = y = 200
		self.gestor_animaciones = GestorAnimaciones((x, y))

		anchura, altura = self.gestor_animaciones.añadir_animacion("andar", self.gestor_animaciones.cargar_frames("popeye/walk", "walk", 2, 2), 175)
		self.gestor_animaciones.añadir_animacion("idle", self.gestor_animaciones.cargar_frames("popeye/idle/", "idle", 1, 2), 1)
		self.gestor_animaciones.añadir_animacion("golpear", self.gestor_animaciones.cargar_frames("popeye/hit/", "hit", 1, 2), 1)
		self.gestor_animaciones.reproducir_animacion("idle")

		self.bounds = py.Rect(105, 216 - altura, anchura, altura)

		self.tamaño_pies = 10
		self.tamaño_puño = 10
		self.pies = py.Rect(x,  y + altura - self.tamaño_pies, anchura, self.tamaño_pies)
		self.puño = py.Rect(0, 0, self.tamaño_puño, self.tamaño_puño)

		self.gravedad = 1
		self.vx, self.vy = 0, 0
		self.velocidad_horizontal = 3
		self.potencia_salto = 8
		self.sobreSuelo = False
		self.pulsando_arriba = False
		self.pulsando_abajo = False
		self.timer_golpear = Timer(500)
		self.golpeando = False
		self.hacia_derecha = True
		self.espacio_puño = 0
		self.puede_golpear = True

		self.corazones = 0

		self.quitar_animacion_golpeo = Timer(250)

	def render(self, _screen):
		self.gestor_animaciones.render(_screen, self.bounds, self.hacia_derecha)
		#py.draw.rect(_screen, (100, 0, 200), self.bounds)
		#py.draw.rect(_screen, (200, 0, 0), self.pies, 1)

		if self.golpeando:
			self.gestor_animaciones.reproducir_animacion("golpear")
			if not self.hacia_derecha:
				self.espacio_puño = 10
			else:
				self.espacio_puño = -10
		else:
			self.espacio_puño = 0

		self.puño.center = (self.puño.center[0] + self.espacio_puño, self.puño.center[1])

		#py.draw.rect(_screen, (255,  0, 0), self.puño, 1)

	def update(self, _dt, _lista_plataformas, _lista_escaleras):
		self.quitar_animacion_golpeo.update(_dt)
		
		self.gestor_animaciones.update(_dt)
		self.comprobar_escaleras(_lista_escaleras)
		self.aplicar_gravedad()
		self.mover()
		self.controles()
		self.comprobar_plataformas(_lista_plataformas)
		self.actualizar_golpe(_dt)
		self.elegir_animaciones()

	def elegir_animaciones(self):
		if not self.golpeando:
			if self.vx != 0:
				self.gestor_animaciones.reproducir_animacion("andar")
			else:
				self.gestor_animaciones.reproducir_animacion("idle")

	def actualizar_golpe(self, _dt):
		self.puño.center = self.bounds.center
		self.timer_golpear.update(_dt)
		if self.timer_golpear.tick:
			self.puede_golpear = True

	def mover(self):
		self.bounds.move_ip(self.vx, self.vy)
		self.pies.x = self.bounds.x
		self.pies.y = self.bounds.y + (self.bounds.height - self.tamaño_pies)

	def aplicar_gravedad(self):
		if not self.sobreSuelo:
			self.vy += self.gravedad
		else:
			self.vy = 0

	def controles(self):
		key = py.key.get_pressed()
		if key[py.K_RIGHT]:
			self.vx = self.velocidad_horizontal
			self.hacia_derecha = False
		elif key[py.K_LEFT]:
			self.vx = -self.velocidad_horizontal
			self.hacia_derecha = True
		else:
			self.vx = 0

		if key[py.K_UP] and self.sobreSuelo and len(self.escaleras_posibles) == 0:
			self.sobreSuelo = False
			self.vy = -self.potencia_salto

		if key[py.K_UP]:
			if self.vx == 0:
				self.subir_escaleras()
		
		if key[py.K_DOWN]:
			if self.vx == 0:
				self.bajar_escaleras()

		if key[py.K_SPACE] and self.puede_golpear:
			self.puede_golpear = False
			self.golpeando = True
		
		if self.quitar_animacion_golpeo.tick:
			self.golpeando = False

	def comprobar_plataformas(self, _lista_plataformas):
		self.sobreSuelo = False
		for plataforma in _lista_plataformas:
			if self.pies.colliderect(plataforma.bounds) and self.vy >= 0:
				self.sobreSuelo = True
				self.pies.bottom = plataforma.bounds.top
				self.bounds.bottom = self.pies.bottom

	def comprobar_escaleras(self, _lista_escaleras):
		self.escaleras_posibles = []
		for escalera in _lista_escaleras:
			if self.pies.colliderect(escalera.bounds) and self.sobreSuelo:
				self.escaleras_posibles.append(escalera)

	def subir_escaleras(self):
		if len(self.escaleras_posibles) > 0:
			escalera_elegida = self.escaleras_posibles[0]
			if len(self.escaleras_posibles) > 1:
				if self.escaleras_posibles[0].bounds.top > self.escaleras_posibles[1].bounds.top:
					escalera_elegida = self.escaleras_posibles[1]
			
			self.bounds.bottom = escalera_elegida.bounds.top
			self.pies.bottom = self.bounds.bottom

	def bajar_escaleras(self):
		if len(self.escaleras_posibles) > 0:
			escalera_elegida = self.escaleras_posibles[0]
			if len(self.escaleras_posibles) > 1:
				if self.escaleras_posibles[0].bounds.bottom < self.escaleras_posibles[1].bounds.bottom:
					escalera_elegida = self.escaleras_posibles[1]

			self.bounds.bottom = escalera_elegida.bounds.bottom
			self.pies.bottom = self.bounds.bottom