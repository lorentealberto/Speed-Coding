import pygame as py
import random as rnd

from settings import SWIDTH, SHEIGHT

class Ball(object):

	def __init__(self):
		rnd.seed()

		self.bounds = py.Rect(0, 0, 5, 5)
		self.color = (255, 255, 255)
		
		self.speed = 2
		
		self.vx = self.vy = self.speed

		self.reset()

	def render(self, _screen):
		py.draw.rect(_screen, self.color, self.bounds)

	def update(self, _dt):
		self.bounds.move_ip(self.vx, self.vy)

		self.check_bounds()

	def check_bounds(self):
		if self.bounds.top < 0 or self.bounds.bottom > SHEIGHT:
			self.vy *= -1

	def switch_speed(self):
		self.vy *= -1 if rnd.randrange(10) == 0 else 1
		self.vx *= -1

	def reset(self):
		self.bounds.center = (SWIDTH // 2, SHEIGHT // 2)
		self.vx *= 1 if rnd.randrange(2) == 0 else -1
		self.vy *= 1 if rnd.randrange(2) == 0 else -1