from animacion import Animacion
import pygame as py

class GestorAnimaciones(object):

	def __init__(self, _posicion):
		self.animaciones = {}
		self.animacion_actual = ""
		self.posicion = _posicion

	def render(self, _screen, _bounds, _hacia_derecha):
		self.animaciones[self.animacion_actual].render(_screen, _bounds, _hacia_derecha)

	def update(self, _dt):
		self.animaciones[self.animacion_actual].update(_dt)

	def reproducir_animacion(self, _nombre_animacion):
		if self.animacion_actual != '':
			if self.animacion_actual != _nombre_animacion:
				
				self.animacion_actual = _nombre_animacion
				self.animaciones[self.animacion_actual].parar()

	def añadir_animacion(self, _nombre_animacion, _frames, _velocidad):
		self.animaciones[_nombre_animacion] = Animacion(_nombre_animacion, _frames, _velocidad, self.posicion)
		self.animacion_actual = _nombre_animacion
		return self.animaciones[_nombre_animacion].anchura, self.animaciones[_nombre_animacion].altura

	def cargar_frames(self, _nombre_carpeta, _nombre_imagen, _numero_frames, _escala = 1):
		frames = []
		for i in range(1, _numero_frames + 1):
			frames.append(self.cargar_img(_nombre_carpeta, _nombre_imagen + " (" + str(i) + ")", _escala))
		return frames

	def cargar_img(self, _nombre_carpeta, _nombre_imagen, _escala = 1):
		img = py.image.load("resources/graphics/sprites/" + _nombre_carpeta + "/" + _nombre_imagen +".png").convert_alpha()
		img = py.transform.scale(img, (img.get_width() * _escala, img.get_height() * _escala))
		return img

	def mirar_lados(self, _hacia_derecha):
		self.animaciones[self.animacion_actual].mirar_lados(_hacia_derecha)