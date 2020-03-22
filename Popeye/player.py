import pygame as py
from gestor_animaciones import GestorAnimaciones
from timer import Timer
 
class Player(object):
	"""Objeto que representa al jugador"""
	def __init__(self):
		#Animaciones y posición
		self.bounds = py.Rect(105, 216, 0, 0)
		self.gestor_animaciones = GestorAnimaciones()

		self.bounds.width, self.bounds.height = self.gestor_animaciones.añadir_animacion("andar", self.gestor_animaciones.cargar_frames("popeye/walk", "walk", 2, 2), 175)
		self.gestor_animaciones.añadir_animacion("idle", self.gestor_animaciones.cargar_frames("popeye/idle/", "idle", 1, 2), 1)
		self.gestor_animaciones.añadir_animacion("golpear", self.gestor_animaciones.cargar_frames("popeye/hit/", "hit", 1, 2), 1)
		self.gestor_animaciones.reproducir_animacion("idle")

		#Pies
		self.tamaño_pies = 10
		self.pies = py.Rect(self.bounds.x,  self.bounds.y + self.bounds.height - self.tamaño_pies, self.bounds.width, self.tamaño_pies)

		#Puño
		self.tamaño_puño = 10
		self.puño = py.Rect(0, 0, self.tamaño_puño, self.tamaño_puño)

		#Velocidades
		self.gravedad = 1
		self.vx, self.vy = 0, 0
		self.velocidad_horizontal = 3
		self.potencia_salto = 8

		#Comportamiento plataformero
		self.sobreSuelo = False

		#Necesario para subir las escaleras
		self.pulsando_arriba = False
		self.pulsando_abajo = False

		#Necesario para golpear
		self.timer_golpear = Timer(500)
		self.golpeando = False
		self.puede_golpear = True
		self.espacio_puño = 0
		self.quitar_animacion_golpeo = Timer(250)

		#Renderizado
		self.hacia_izquierda = False
		
		#Puntuación
		self.corazones = 0

	def render(self, _screen):
		"""Dibuja la correspondiente animación en la pantalla en base a lo que
			el jugador esté haciendo.
			Parámetros:
				_screen -- Pantalla donde se dibujará."""
		self.gestor_animaciones.render(_screen, self.bounds, self.hacia_izquierda)

		#Se encarga de establecer la posición interna del puño correctamente.
		if self.golpeando:
			self.gestor_animaciones.reproducir_animacion("golpear")
			if not self.hacia_derecha:
				self.espacio_puño = 10
			else:
				self.espacio_puño = -10
		else:
			self.espacio_puño = 0

		self.puño.center = (self.puño.center[0] + self.espacio_puño, self.puño.center[1])

	def update(self, _dt, _lista_plataformas, _lista_escaleras):
		"""Actualiza los elementos del objeto.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde la última
					vez que se llamó este método.
				_lista_plataformas -- Lista de plataformas del nivel.
				_lista_escaleras -- Lista de escaleras del nivel."""
		self.quitar_animacion_golpeo.update(_dt)
		
		self.gestor_animaciones.update(_dt)
		self.comprobar_escaleras(_lista_escaleras)
		self.aplicar_gravedad()
		self.mover()
		self.controles()
		self.comprobar_plataformas(_lista_plataformas)
		self.actualizar_golpe(_dt)
		self.elegir_animaciones()
		self.mirar_lados()

	def mirar_lados(self):
		"""Si la velocidad horizontal del objeto es negativa, el objeto mirará
			hacía la izquierda, a la derecha en caso contrario"""
		if self.vx < 0:
			self.hacia_izquierda = True
		elif self.vx > 0:
			self.hacia_izquierda = False

	def elegir_animaciones(self):
		"""Elige la animación correcta en base a las variables internas del objeto."""
		if not self.golpeando:
			if self.vx != 0:
				self.gestor_animaciones.reproducir_animacion("andar")
			else:
				self.gestor_animaciones.reproducir_animacion("idle")

	def actualizar_golpe(self, _dt):
		"""Añade un pequeño retraso para evitar que la animación de golpeo únicamente
			dure un segundo.
			Parámetro:
				_dt -- Tiempo en milisegundos que ha transcurrido desde la última
					vez que se ejecutó este método."""
		self.puño.center = self.bounds.center
		self.timer_golpear.update(_dt)
		if self.timer_golpear.tick:
			self.puede_golpear = True

	def mover(self):
		"""Mueve el objeto"""
		self.bounds.move_ip(self.vx, self.vy)
		self.pies.x = self.bounds.x
		self.pies.y = self.bounds.y + (self.bounds.height - self.tamaño_pies)

	def aplicar_gravedad(self):
		"""Aplica la gravedad sobre el objeto si no está sobre una plataforma"""
		if not self.sobreSuelo:
			self.vy += self.gravedad
		else:
			self.vy = 0

	def controles(self):
		"""Gestiona la pulsación de teclas para realizar una acción u otra
			dependiendo de la tecla pulsada."""
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
		"""Comprueba que el objeto esté sobre una de las plataformas del nivel
			Parámetros:
				_lista_plataformas -- Lista de plataformas del nivel."""
		self.sobreSuelo = False
		for plataforma in _lista_plataformas:
			if self.pies.colliderect(plataforma.bounds) and self.vy >= 0:
				self.sobreSuelo = True
				self.pies.bottom = plataforma.bounds.top
				self.bounds.bottom = self.pies.bottom

	def comprobar_escaleras(self, _lista_escaleras):
		"""Comprueba que el objeto esté en una de las escaleras del nivel.
			Parámetros:
				_lista_escaleras -- Lista de escaleras del nivel."""
		self.escaleras_posibles = []
		for escalera in _lista_escaleras:
			if self.pies.colliderect(escalera.bounds) and self.sobreSuelo:
				self.escaleras_posibles.append(escalera)

	def subir_escaleras(self):
		"""El objeto sube un piso en caso de que esté tocando una escalera
			ascendente."""
		if len(self.escaleras_posibles) > 0:
			escalera_elegida = self.escaleras_posibles[0]
			if len(self.escaleras_posibles) > 1:
				if self.escaleras_posibles[0].bounds.top > self.escaleras_posibles[1].bounds.top:
					escalera_elegida = self.escaleras_posibles[1]
			
			self.bounds.bottom = escalera_elegida.bounds.top
			self.pies.bottom = self.bounds.bottom

	def bajar_escaleras(self):
		"""El objeto baja un piso en caso de que esté tocando una escalera
			descendente."""
		if len(self.escaleras_posibles) > 0:
			escalera_elegida = self.escaleras_posibles[0]
			if len(self.escaleras_posibles) > 1:
				if self.escaleras_posibles[0].bounds.bottom < self.escaleras_posibles[1].bounds.bottom:
					escalera_elegida = self.escaleras_posibles[1]

			self.bounds.bottom = escalera_elegida.bounds.bottom
			self.pies.bottom = self.bounds.bottom