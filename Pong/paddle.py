import pygame as py

from pixelsmash.functions import read_key

from settings import SWIDTH, SHEIGHT

class Paddle(object):

	def __init__(self, _side):
		self.side = _side

		self.bounds = py.Rect(0, 0, 2, 40)
		
		self.speed = 4
		self.vy = 0
		
		self.color = (230, 0, 0) if _side == "LEFT" else (0, 0, 230)

		self.reset()

	def render(self, _screen):
		py.draw.rect(_screen, self.color, self.bounds)

	def update(self, _dt):
		self.controls()
		self.move()
		self.check_bounds()

	def controls(self):
		pressed_key = read_key()

		if self.side == "RIGHT":
			if pressed_key == "UP":
				self.vy = -self.speed
			elif pressed_key == "DOWN":
				self.vy = self.speed
			else:
				self.vy = 0
		elif self.side == "LEFT":
			if pressed_key == "W":
				self.vy = -self.speed
			elif pressed_key == "S":
				self.vy = self.speed
			else:
				self.vy = 0

	def move(self):
		self.bounds.move_ip(0, self.vy)

	def check_bounds(self):
		if self.bounds.top < 0:
			self.bounds.top = 0
			self.vy = 0
		elif self.bounds.bottom > SHEIGHT:
			self.bounds.bottom = SHEIGHT
			self.vy = 0

	def reset(self):
		self.bounds.center =  (20, SHEIGHT // 2) if self.side == "LEFT" else (SWIDTH - 20, SHEIGHT // 2)