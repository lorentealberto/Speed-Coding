from pixelsmash.animation import Animation
from pixelsmash.functions import load_img
import pygame as py

class Animator(object):
	"""Object that will serve as an animation container for another superior object."""
	def __init__(self):
		self.animations = {}
		self.currentAnimation = ""
		
		self.times = 0
		self.currentTimes = 0
		
		self.ended = False

	def render(self, _screen, _bounds, _facing_left = False):
		"""Draw the current animation on the screen.
			Parameters:
				_screen -- Screen where it will be drawn.
				_bounds -- Position where it will be drawn.
				_facing_left -- Flag that indicates if the object is looking
					to the left."""
		self.animations[self.currentAnimation].render(_screen, _bounds, _facing_left)

	def update(self, _dt):
		"""Update the animation.
			Parameters:
				_dt -- Time in milliseconds that has passed since it was called
					the method for the last time."""
		if self.times == -1:
			self.animations[self.currentAnimation].update(_dt)
			if self.animations[self.currentAnimation].ended:
				self.animations[self.currentAnimation].reset_animation()
		else:
			if self.currentTimes < self.times:
				if self.animations[self.currentAnimation].ended:
					self.currentTimes += 1
					self.animations[self.currentAnimation].reset_animation()
				else:
					self.animations[self.currentAnimation].update(_dt)	
			else:
				self.ended = True
			
	def play_animation(self, _animation_name, _loop = -1):
		"""Plays the selected animation as long as the animation
			selected is not void, whether it is a valid animation or not
			playing now.
			Parameters:
				_animation_name -- Name of the animation to be played.
				_loop -- Number of times the animation will be repeated. Default
					value of this parameter is -1, that is the animation will be
					repeated indefinitely."""

		if len(self.animations) > 0:
			self.animations[self.currentAnimation].stop()
		
		if self.currentAnimation != '':
			self.currentAnimation = _animation_name
			self.ended = False
			self.times = _loop
			self.currentTimes = 0	
			return self.animations[_animation_name].width, self.animations[_animation_name].height

	def add_animation(self, _animation_name, _speed, _animation_path, _number_frames, _scale = 1):
		"""Add a new animation to the instance animation catalog
			of the object. It puts it as the current animation that you want to play and
			returns the width and height of the first frame of the animation.
			Parameters:
				_animation_name -- Name the animation will have internally.
				_speed -- Speed at which you want to play the animation
				_animation_path -- Path where animation is.
				_number_frames -- Animation number of frames
				_scale -- Animation scale. Default value = 1. It means animation isn't resizing.
			Return:
				width -- the width of the first frame of the animation.
				height -- The height of the first frame of the animation."""
		_frames = self.__load_frames(_animation_path, _number_frames, _scale)

		self.animations[_animation_name] = Animation(_animation_name, _frames, _speed)

		self.currentAnimation = _animation_name

		return self.animations[_animation_name].width, self.animations[_animation_name].height

	def __load_frames(self, _image_name, _number_frames, _scale = 1):
		"""[Private Method]
			Load a list of frames
			Parameters:
				_image_name -- The name that the frames have inside the
					folder. All the frames in it have to be called from the
					same way, but it has to be numbered so that they are loaded
					correctly.
				_number_frames -- Number of frames the animation has.
				_scale -- Scale at which you want to resize the frames
					of animation. By default, no frames in the animation
					it will escalate."""
		frames = []
		for i in range(1, _number_frames + 1):
			frames.append(load_img(_image_name + " (" + str(i) + ")", _scale))
		return frames