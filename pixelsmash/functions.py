import pygame as py

def load_img(_image_name, _scale = 1):
	"""It loads an image, scales it and returns it.
		Parameters:
			_image_name -- Name of the image.
			_scale -- Scale to which you want to scale the image. By
				default the image will not scale.
		Return:
			The image loaded and scaled to the indicated scale."""
	img = py.image.load("resources/graphics/" + _image_name +".png").convert_alpha()
	img = py.transform.scale(img, (img.get_width() * _scale, img.get_height() * _scale))
	return img