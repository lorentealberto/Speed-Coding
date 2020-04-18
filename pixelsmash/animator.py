from pixelsmash.animacion import Animacion
from pixelsmash.funciones import cargar_img
import pygame as py

class Animator(object):
	"""Object that will serve as an animation container for another superior object."""
	def __init__(self):
		self.animations = {}
		self.current_animation = ""
		
		self.n_veces = 0
		self.veces_ahora = 0
		
		self.ended = False

	def render(self, _screen, _bounds, _left_toward = False):
		"""Draw the current animation on the screen.
			Parameters:
				_screen -- Screen where it will be drawn.
				_bounds -- Position where it will be drawn.
				_left_toward -- Flag that indicates if the object is looking
					to the left."""
		self.animations[self.current_animation].render(_screen, _bounds, _left_toward)

	def update(self, _dt):
		"""Update the animation.
			Parameters:
				_dt -- Time in milliseconds that has passed since it was called
					the method for the last time."""
		if self.n_veces == 0:
			self.animations[self.current_animation].update(_dt)
		else:
			if self.veces_ahora <= self.n_veces:
				if (self.animations[self.current_animation].frame_actual >= 
					len(self.animations[self.current_animation].frames) - 1):
					self.veces_ahora += 1
				else:
					self.animations[self.current_animation].update(_dt)
			else:
				self.ended = True
		
	def play_animation(self, _animation_name, loop = 0):
		"""Plays the selected animation as long as the animation
			selected is not void, whether it is a valid animation or not
			playing now.
			Parameters:
				_animation_name -- Name of the animation to be played."""
		if self.current_animation != '':
			#if self.animacion_actual != _nombre_animacion:
			self.current_animation = _animation_name
			self.n_veces = loop
			self.veces_ahora = 0
			self.ended = False
			self.animations[self.current_animation].stop()
			return self.animations[_animation_name].width, self.animations[_animation_name].height

	def add_animation(self, _animation_name, _frames, _speed, loop = 0):
		"""Add a new animation to the instance animation catalog
			of the object. It puts it as the current animation that you want to play and
			returns the width and height of the first frame of the animation.
			Parameters:
				_animation_name -- Name the animation will have internally.
				_frames -- List of frames that make up the animation.
				_speed -- Speed at which you want to play the animation
			Come back:
				width -- the width of the first frame of the animation.
				height -- The height of the first frame of the animation."""
		self.animations[_animation_name] = Animacion(_animation_name, _frames, _velocidad)
		self.animacion_actual = _animation_name
		self.n_veces = loop
		self.veces_ahora = 0
		return self.animations[_animation_name].width, self.animations[_animation_name].height

	def load_frames(self, _image_name, _number_frames, _scale = 1):
		"""Load a list of frames
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
			frames.append(cargar_img(_image_name + " (" + str(i) + ")", _scale))
		return frames