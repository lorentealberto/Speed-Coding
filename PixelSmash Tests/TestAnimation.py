import pygame as py

from pixelsmash.animation import Animation
from pixelsmash.functions import load_img

from settings import WIDTH, HEIGHT

class TestAnimation(object):
	"""PixelSmash 'Animation' class test set"""
	def __init__(self):
		self.bounds = py.Rect(WIDTH // 2, HEIGHT // 2, 0, 0)

		self.animation = Animation("walk", [load_img("image (1)", 2), load_img("image (2)", 2)], 250)

		self.bounds.width, self.bounds.height = self.animation.width, self.animation.height

		self.bounds.x -= self.bounds.width // 2

	def render(self, _screen):
		 # If the value of '_facing_left' is 'False' the animation will be 
		 # looking to the right, if on the contrary the value is 'True', the
		 # animation will be looking to the left. The default value of this
		 # parameter is 'False' that is, by default the image will be looking
		 # to the right.
		self.animation.render(_screen, self.bounds, _facing_left = False)

	def update(self, _dt):
		self.animation.update(_dt)

		# If the bottom line is uncommented, the animation will not play since
		# every time this method is executed, the animation stops
		#self.animation.stop()