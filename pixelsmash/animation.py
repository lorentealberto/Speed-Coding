import pygame as py
from pixelsmash.timer import Timer

class Animation(object):
	"""It represents an animation on game.
			Parameters:
				_name -- Animation name
				_frames -- Animation frames
				_speed -- Speed (MS) which last each animation frame"""
	def __init__(self, _name, _frames, _speed):
		#Received by parameter
		self.name = _name
		self.frames = _frames
		self._speed = _speed
		self.timer = Timer(_velocidad)

		#Inner data
		self.current_frame = 0
		self.width = self.frames[0].get_width()
		self.height = self.frames[0].get_height()

	def render(self, _screen, _bounds, _left_toward):
		"""Draw the animation on the screen, on the position passed by
				parameter.
			Parameter:
				_screen -- Screen on which the frames will be drawn.
				_bounds -- Position where the image will be drawn.
				_left_toward -- Bool to indicate if the image will be rotated
					to the left."""
		_screen.blit(py.transform.flip(self.frames[self.frame_actual], _left_toward, False), _bounds)

	def update(self, _dt):
		"""Update the animation.
			Parameters:
				_dt -- Time in milliseconds, since this method was executed
					for the last time."""
		self.timer.update(_dt)

		#Each time the animation's internal timer emits a pulse
		#you advance the list of frames. If there are no more frames within
		#the list, it goes back to the beginning.
		if self.timer.tick:
			self.current_frame += 1
			if self.current_frame > len(self.frames) - 1:
				self.current_frame = 0

	def stop(self):
		"""Stops the internal timer of the animation and resets the counter
			of frames in the animation to start again from frame zero."""
		self.timer.parar()
		self.current_frame = 0