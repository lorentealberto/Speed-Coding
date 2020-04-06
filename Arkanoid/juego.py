from pixelsmash.funciones import cargar_img


from jugador import Jugador
from pelota import Pelota
from escenario import Escenario


class Juego(object):

	def __init__(self, _gestor_estados):
		self.fondo = cargar_img("fondos/fondo")

		self.jugador = Jugador()
		self.pelota = Pelota()
		self.escenario = Escenario()

	def dibujar(self, _pantalla):
		_pantalla.blit(self.fondo, (20, 0))

		self.jugador.render(_pantalla)
		self.pelota.dibujar(_pantalla)
		self.escenario.dibujar(_pantalla)

	def actualizar(self, _dt):
		self.jugador.actualizar(_dt)
		self.pelota.actualizar(_dt, self.jugador);
		self.escenario.actualizar(_dt, self.pelota)