import random
from pixelsmash.funciones import cargar_img

from ladrillo import Ladrillo
from ladrillo_brillante import LadrilloBrillante
from power_ups import LaserPowerUp, EnlargePowerUp, CatchPowerUp, PlayerPowerUp, SlowPowerUp
"""
	- 0 = Espacio Vacío
	- 1 = Azul Claro
	- 2 = Naranja
	- 3 = Azul Oscuro
	- 4 = Rosa
	- 5 = Rojo
	- 6 = Salmón
	- 7 = Verde
	- 10 = Plata
	- 11 = Oro
"""
mapa = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
	[0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
	[0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0],
	[0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0],
	[0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 0, 0],
	[0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 0, 0],
	[0, 0, 0, 10, 10, 5, 10, 10, 10, 5, 10, 10, 0],
	[0, 0, 0, 10, 10, 5, 10, 10, 10, 5, 10, 10, 0],
	[0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
	[0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
	[0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
	[0, 0, 10, 0, 10, 10, 10, 10, 10, 10, 10, 0, 10],
	[0, 0, 10, 0, 10, 0, 0, 0, 0, 0, 10, 0, 10],
	[0, 0, 10, 0, 10, 0, 0, 0, 0, 0, 10, 0, 10],
	[0, 0, 0, 0, 0, 10, 10, 0, 10, 10, 0, 0, 0],
	[0, 0, 0, 0, 0, 10, 10, 0, 10, 10, 0, 0, 0]]

#cargar_frames(self, _nombre_imagen, _numero_frames, _escala = 1)
class Escenario(object):

	def __init__(self):
		random.seed()
		self.cargar_ladrillos()
		self.ladrillos = []
		self.cargar_mapa()
		self.power_ups = []

	def dibujar(self, _pantalla):
		self.dibujar_mapa(_pantalla)
		self.dibujar_power_ups(_pantalla)

	def actualizar(self, _dt, _pelota):
		for ladrillo in self.ladrillos:
			ladrillo.actualizar(_dt)
		self.comprobar_colisiones(_pelota)

		self.actualizar_power_ups(_dt)

	def dibujar_power_ups(self, _pantalla):
		for power_up in self.power_ups:
			power_up.dibujar(_pantalla)

	def actualizar_power_ups(self, _dt):
		for power_up in self.power_ups:
			power_up.actualizar(_dt)

	def dibujar_mapa(self, _pantalla):
		for ladrillo in self.ladrillos:
			ladrillo.dibujar(_pantalla)

	def cargar_mapa(self):
		for i in range(len(mapa)):
			for j in range(len(mapa[i])):
				if mapa[i][j] > 0 and mapa[i][j] < 10:
					self.ladrillos.append(Ladrillo(30 + j * self.imgs_ladrillos[(mapa[i][j] - 1)].get_width(), 
													12 + i * self.imgs_ladrillos[(mapa[i][j] - 1)].get_height(),
													self.imgs_ladrillos[(mapa[i][j] - 1)]))
				elif mapa[i][j] == 10:
					self.ladrillos.append(LadrilloBrillante(30 + j * self.imgs_ladrillos[0].get_width(), 
													12 + i * self.imgs_ladrillos[0].get_height(),
													"ladrillos/ladrillo_plateado", 6))

	def cargar_ladrillos(self):
		self.imgs_ladrillos = [
			cargar_img("ladrillos/ladrillo_azul_claro"),
			cargar_img("ladrillos/ladrillo_naranja"),
			cargar_img("ladrillos/ladrillo_azul_oscuro"),
			cargar_img("ladrillos/ladrillo_rosa"),
			cargar_img("ladrillos/ladrillo_rojo"),
			cargar_img("ladrillos/ladrillo_salmon"),
			cargar_img("ladrillos/ladrillo_verde")
		]

	def comprobar_colisiones(self, _pelota):
		for ladrillo in self.ladrillos:
			if ladrillo.bounds.colliderect(_pelota.bounds):
				ladrillo.golpear()
			
				_pelota.vy *= -1
				
				ladrillo.vidas -= 1
				if ladrillo.vidas <= 0:
					spawn_power_up = random.randint(1, 100)
					if spawn_power_up <= 5:
						tipo_power_up = random.randint(1, 5)
						self.añadir_power_up(ladrillo.bounds.center[0], ladrillo.bounds.center[1], tipo_power_up)
					self.ladrillos.remove(ladrillo)

					break

	def añadir_power_up(self, _x, _y, _tipo):
		#Láser
		if _tipo == 1:
			self.power_ups.append(LaserPowerUp(_x, _y))
		elif _tipo == 2:
			self.power_ups.append(EnlargePowerUp(_x, _y))
		elif _tipo == 3:
			self.power_ups.append(CatchPowerUp(_x, _y))
		elif _tipo == 4:
			self.power_ups.append(SlowPowerUp(_x, _y))
		elif _tipo == 5:
			self.power_ups.append(PlayerPowerUp(_x, _y))
