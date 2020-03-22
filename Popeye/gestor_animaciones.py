from animacion import Animacion
import pygame as py

class GestorAnimaciones(object):
	"""Objeto que servirá de contenedor de animaciones de otro objeto superior."""
	def __init__(self):
		self.animaciones = {}
		self.animacion_actual = ""

	def render(self, _screen, _bounds, _hacia_izquierda):
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
		self.animaciones[self.animacion_actual].update(_dt)

	def reproducir_animacion(self, _nombre_animacion):
		"""Reproduce la animación seleccionada siempre y cuando la animación
			seleccionada no sea nula, sea una animación válida o no se esté
			reproduciendo ya.
			Parámetros:
				_nombre_animacion -- Nombre de la animación que se desea reproducir."""
		if self.animacion_actual != '':
			if self.animacion_actual != _nombre_animacion:
				self.animacion_actual = _nombre_animacion
				self.animaciones[self.animacion_actual].parar()

	def añadir_animacion(self, _nombre_animacion, _frames, _velocidad):
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
		return self.animaciones[_nombre_animacion].anchura, self.animaciones[_nombre_animacion].altura

	def cargar_frames(self, _nombre_carpeta, _nombre_imagen, _numero_frames, _escala = 1):
		"""Carga una lista de frames
			Parámetros:
				_nombre_carpeta -- Nombre de la carpeta donde se encuentran los frames.
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
			frames.append(self.cargar_img(_nombre_carpeta, _nombre_imagen + " (" + str(i) + ")", _escala))
		return frames

	def cargar_img(self, _nombre_carpeta, _nombre_imagen, _escala = 1):
		"""Carga una imagen, la escala y la devuelve.
			Parámetros:
				_nombre_carpeta -- Nombre de la carpeta donde se encuentra la imagen.
				_nombre_imagen -- Nombre de la imagen.
				_escala -- Escala a la que se quiere escalar la imagen. Por
					defecto la imagen no se escalará.
			Devuelve:
				La imagen cargada y escalada a la escala indicada."""
		img = py.image.load("resources/graphics/sprites/" + _nombre_carpeta + "/" + _nombre_imagen +".png").convert_alpha()
		img = py.transform.scale(img, (img.get_width() * _escala, img.get_height() * _escala))
		return img