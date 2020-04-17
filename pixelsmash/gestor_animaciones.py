from pixelsmash.animacion import Animacion
from pixelsmash.funciones import cargar_img
import pygame as py

class GestorAnimaciones(object):
	"""Objeto que servirá de contenedor de animaciones de otro objeto superior."""
	def __init__(self):
		self.animaciones = {}
		self.animacion_actual = ""
		self.n_veces = 0
		self.veces_ahora = 0
		self.terminada = False

	def render(self, _screen, _bounds, _hacia_izquierda = False):
		"""Dibuja la animación actual en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujará.
				_bounds -- Posición donde se dibujará.
				_hacia_izquierda -- Bandera que indica si el objeto está mirando
					hacía la izquierda."""
		self.animaciones[self.animacion_actual].render(_screen, _bounds, _hacia_izquierda)

	def update(self, _dt):
		"""Actualiza la animación.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha pasado desde que se llamó
					el método por última vez."""
		if self.n_veces == 0:
			self.animaciones[self.animacion_actual].update(_dt)
		else:
			if self.veces_ahora <= self.n_veces:
				if (self.animaciones[self.animacion_actual].frame_actual >= 
					len(self.animaciones[self.animacion_actual].frames) - 1):
					self.veces_ahora += 1
				else:
					self.animaciones[self.animacion_actual].update(_dt)
			else:
				self.terminada = True
		
	def reproducir_animacion(self, _nombre_animacion, loop = 0):
		"""Reproduce la animación seleccionada siempre y cuando la animación
			seleccionada no sea nula, sea una animación válida o no se esté
			reproduciendo ya.
			Parámetros:
				_nombre_animacion -- Nombre de la animación que se desea reproducir."""
		if self.animacion_actual != '':
			#if self.animacion_actual != _nombre_animacion:
			self.animacion_actual = _nombre_animacion
			self.n_veces = loop
			self.veces_ahora = 0
			self.terminada = False
			self.animaciones[self.animacion_actual].parar()
			return self.animaciones[_nombre_animacion].anchura, self.animaciones[_nombre_animacion].altura

	def añadir_animacion(self, _nombre_animacion, _frames, _velocidad, loop = 0):
		"""Añade una nueva animación al catálogo de animaciones de la instancia
			del objeto. La pone como animación actual que se quiere reproducir y
			devuelve el ancho y el alto del primer frame de la animación.
			Parámetros:
				_nombre_animacion -- Nombre que tendrá la animación internamente.
				_frames -- Lista de frames que componen la animación.
				_velocidad -- Velocidad a la que se desea reproducir la animación
			Devuelve:
				anchura -- La anchura del primer frame de la animación.
				altura -- La altura del primer frame de la animación."""
		self.animaciones[_nombre_animacion] = Animacion(_nombre_animacion, _frames, _velocidad)
		self.animacion_actual = _nombre_animacion
		self.n_veces = loop
		self.veces_ahora = 0
		return self.animaciones[_nombre_animacion].anchura, self.animaciones[_nombre_animacion].altura

	def cargar_frames(self, _nombre_imagen, _numero_frames, _escala = 1):
		"""Carga una lista de frames
			Parámetros:
				_nombre_imagen -- Nombre que tienen los frames dentro de la
					carpeta. Todos los frames de la misma se tienen que llamar del
					mismo modo, pero tiene que ir numerados para que se carguen
					correctamente.
				_numbero_frames -- Número de frames que tiene la animación.
				_escala -- Escala a la que se quieren redimensionar los frames
					de la animación. Por defecto ningún frame de la animación
					se escalará."""
		frames = []
		for i in range(1, _numero_frames + 1):
			frames.append(cargar_img(_nombre_imagen + " (" + str(i) + ")", _escala))
		return frames

	def ended_animation(self, _animation, _ended = True):
		if (self.animacion_actual == _animation and
			self.terminada == _ended):
			return True
		return False