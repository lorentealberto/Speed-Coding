import pygame as py

from pixelsmash.animator import Animator
from settings import WIDTH, HEIGHT

class TestAnimator(object):
	
	def __init__(self):
		self.played_new_animation = False

		# An object of type animator is created
		self.animator = Animator()

		# In order to render the animation, a 'body' is needed. This body, among
		# other things, will indicate the area where you want the animation to be
		# redrawn and will also serve to check for collisions with other objects.
		self.bounds = py.Rect(WIDTH // 2, HEIGHT // 2, 0, 0)

		# We add two animations to the object (We add two animations because it
		# would not make sense to try an animation manager with only one animation.
		# You wouldn't even need an animation manager for a single animation).
		self.bounds.width, self.bounds.height = self.animator.add_animation("animation_1", 250, "image", 2, 2)

		self.animator.add_animation("animation_2", 1000, "mario_flip", 2, 2)

		# Play animation #1
		self.animator.play_animation("animation_1", 1)
				

	def update(self, _dt):
		# It is MANDATORY to update this object so that the animation plays correctly.
		self.animator.update(_dt)

		if self.animator.ended and not self.played_new_animation:
			# If the previous animation has finished, play animation No. 2 twice
			self.animator.play_animation("animation_2", 2)
			self.played_new_animation = True

	def render(self, _screen):
		# To draw the animator object on the screen it is necessary to use the
		# body that we have defined before. This body will indicate the exact
		# zone where we want to render the frames of the animation and it will
		# also indicate the body of the animation to be able to check the
		# collisions. The '_facing_left' parameter is optional and indicates for
		# which side you will be looking at the image. If its value is 'true'
		# the object will be looking to the left if it is 'true' the object will
		# be looking to the right. By default this parameter takes the value
		# 'false', that is unless we indicate otherwise the object will be facing
		# right.
		self.animator.render(_screen, self.bounds, _facing_left = False)