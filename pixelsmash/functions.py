import pygame as py

def load_img(_image_name, _scale = 1):
	"""It loads an image, scales it and returns it.
		Parameters:
			_image_name -- Name of the image.
			_scale -- Scale to which you want to scale the image. By
				default the image will not scale.
		Return:
			The image loaded and scaled to the indicated scale."""
	img = py.image.load("resources/graphics/" + _image_name +".png")#.convert_alpha()
	img = py.transform.scale(img, (img.get_width() * _scale, img.get_height() * _scale))
	return img

def read_key():
	key = py.key.get_pressed()

	if key[py.K_a]:
		return "A"
	elif key[py.K_w]:
		return "W"
	elif key[py.K_d]:
		return "D"
	elif key[py.K_s]:
		return "S"
	elif key[py.K_LEFT]:
		return "LEFT"
	elif key[py.K_UP]:
		return "UP"
	elif key[py.K_RIGHT]:
		return "RIGHT"
	elif key[py.K_DOWN]:
		return "DOWN"
	elif key[py.K_SPACE]:
		return "SPACE"
	elif key[py.K_RETURN]:
		return "ENTER"

	return None

def check_single_object_collision(_object_1, _object_2):
	return True if _object_1.bounds.colliderect(_object_2.bounds) else False