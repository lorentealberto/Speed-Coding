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
		self.__name = _name
		self.__frames = _frames
		self.__speed = _speed
		self.__timer = Timer(_speed)

		#Inner data
		self.__current_frame = 0
		self.__width = self.__frames[0].get_width()
		self.__height = self.__frames[0].get_height()
		self.__ended = False

	def render(self, _screen, _bounds, _facing_left = False):
		"""Draw the animation on the screen, on the position passed by
				parameter.
			Parameter:
				_screen -- Screen on which the frames will be drawn.
				_bounds -- Position where the image will be drawn.
				_facing_left -- Bool to indicate if the image will be rotated
					to the left. Default value = False"""
		_screen.blit(py.transform.flip(self.__frames[self.__current_frame], _facing_left, False), _bounds)

	def update(self, _dt):
		"""Update the animation.
			Parameters:
				_dt -- Time in milliseconds, since this method was executed
					for the last time."""
		self.__timer.update(_dt)

		# Each time the animation's internal timer emits a pulse
		# you advance the list of frames. If there are no more frames within
		# the list, it goes back to the beginning.
		if self.__timer.getTick():
			self.__current_frame += 1

			if self.__current_frame > len(self.__frames) - 1:
				self.__current_frame = len(self.__frames) - 1
				self.__ended = True
		
	def stop(self):
		"""Stops the internal timer of the animation and resets the counter
			of frames in the animation to start again from frame zero."""
		self.__timer.stop()
		self.__current_frame = 0

	def reset_animation(self):
		self.__current_frame = 0
		self.__ended = False

	def isEnded(self):
		return self.__ended

	def getWidth(self):
		return self.__width

	def getHeight(self):
		return self.__height

	def getSize(self):
		return (self.__width, self.__height)