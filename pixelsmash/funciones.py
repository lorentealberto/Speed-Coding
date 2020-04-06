import pygame as py

def cargar_img(_nombre_imagen, _escala = 1):
	"""Carga una imagen, la escala y la devuelve.
		Parámetros:
			_nombre_imagen -- Nombre de la imagen.
			_escala -- Escala a la que se quiere escalar la imagen. Por
				defecto la imagen no se escalará.
		Devuelve:
			La imagen cargada y escalada a la escala indicada."""
	img = py.image.load("resources/graphics/" + _nombre_imagen +".png").convert_alpha()
	img = py.transform.scale(img, (img.get_width() * _escala, img.get_height() * _escala))
	return img