import pygame as py
from timer import Timer

class Animacion(object):
	"""Representa una animación dentro del juego
		Parámetros:
			_nombre -- Nombre que recibirá la animación.
			_frames -- Lista que contiene los frames de la animación.
			_velocidad -- Velocidad en milisegundos que durará cada frame."""
	def __init__(self, _nombre, _frames, _velocidad):
		#Recibido por parámetro
		self.nombre = _nombre
		self.frames = _frames
		self.velocidad = _velocidad
		self.timer = Timer(_velocidad)

		#Variables internas
		self.frame_actual = 0
		self.anchura = self.frames[0].get_width()
		self.altura = self.frames[0].get_height()

	def render(self, _screen, _bounds, _hacia_izquierda):
		"""Dibuja la animación en la pantalla, sobre la posición pasada por
				parámetro.
			Parámetros:
				_screen -- Pantalla sobre la que se dibujarán los frames.
				_bounds -- Posición donde se dibujará la imagen.
				_hacia_izquierda -- Bool para indicar si la imagen estará girada
					hacía la izquierda."""
		_screen.blit(py.transform.flip(self.frames[self.frame_actual], _hacia_izquierda, False), _bounds)

	def update(self, _dt):
		"""Actualiza la animación.
			Parámetros:
				_dt -- Tiempo en milisegundos, desde que se ejecutó este método
					por última vez."""
		self.timer.update(_dt)

		#Cada vez que el temporizador interno de la animación emite un pulso
		#se avanza en la lista de frames. Si ya no hay más frames dentro de
		#la lista, se vuelve al principio.
		if self.timer.tick:
			self.frame_actual += 1
			if self.frame_actual > len(self.frames) - 1:
				self.frame_actual = 0

	def parar(self):
		"""Detiene el temporizador internto de la animación y resetea el contador
			de frames de la animación para volver a empezar desde el frame cero."""
		self.timer.parar()
		self.frame_actual = 0