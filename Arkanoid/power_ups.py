from pygame import Rect

from pixelsmash.gestor_animaciones import GestorAnimaciones
from pixelsmash.timer import Timer


class PowerUp(object):

	def __init__(self, _x, _y, _nombre):
		self.bounds = Rect(_x, _y, 0, 0)
		self.animaciones = GestorAnimaciones()

		self.bounds.width, self.bounds.height = self.animaciones.añadir_animacion(_nombre, 
													self.animaciones.cargar_frames("powerups/"+_nombre, 6), 
													200, 0)
		self.temporizador_movimiento = Timer(10)
		self.tipo = _nombre

	def dibujar(self, _pantalla):
		self.animaciones.render(_pantalla, self.bounds)

	def actualizar(self, _dt):
		self.animaciones.update(_dt)
		self.temporizador_movimiento.update(_dt)
		self.mover()

	def mover(self):
		if self.temporizador_movimiento.tick:
			self.bounds.move_ip(0, 1)


class LaserPowerUp(PowerUp):
	def __init__(self, _x, _y):
		PowerUp.__init__(self, _x, _y, "laser")

class EnlargePowerUp(PowerUp):
	def __init__(self, _x, _y):
		PowerUp.__init__(self, _x, _y, "enlarge")

class CatchPowerUp(PowerUp):
	def __init__(self, _x, _y):
		PowerUp.__init__(self, _x, _y, "catch")

class SlowPowerUp(PowerUp):
	def __init__(self, _x, _y):
		PowerUp.__init__(self, _x, _y, "slow")

class PlayerPowerUp(PowerUp):
	def __init__(self, _x, _y):
		PowerUp.__init__(self, _x, _y, "player")