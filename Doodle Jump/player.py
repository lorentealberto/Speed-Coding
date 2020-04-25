import pygame as py
from pixelsmash.functions import load_img
from settings import WIDTH

class Player(object):

	def __init__(self):
		self.img = load_img("player")
		self.bounds = self.img.get_rect()
		self.vy, self.vx = 0, 0
		self.gravity = 1
		self.horizontal_speed = 5
		self.on_ground = False
		self.max_fall_speed = 8
		self.facing_left = False
		self.jump_power = -18

		self.center_object()

	def render(self, _screen):
		_screen.blit(py.transform.flip(self.img, self.facing_left, False), self.bounds)

	def update(self, _dt):
		self.apply_gravity()
		self.move()
		self.controls()
		self.check_facing()
		self.check_bounds()

	def apply_gravity(self):
		if not self.on_ground:
			self.vy += self.gravity
		else:
			self.vy = 0

		if self.vy > self.max_fall_speed:
			self.vy = self.max_fall_speed

	def move(self):
		self.bounds.move_ip(self.vx, self.vy)

	def controls(self):
		key = py.key.get_pressed()

		if key[py.K_RIGHT]:
			self.vx = self.horizontal_speed
		elif key[py.K_LEFT]:
			self.vx = -self.horizontal_speed
		else:
			self.vx = 0

	def check_facing(self):
		if self.vx > 0:
			self.facing_left = False
		elif self.vx < 0:
			self.facing_left = True

	def check_bounds(self):
		if self.bounds.top < 0:
			self.bounds.top = 0
		
		if self.bounds.right < 0:
			self.bounds.right = 0
		elif self.bounds.left > WIDTH:
			self.bounds.left = WIDTH

	def center_object(self):
		self.bounds.x = WIDTH // 2 - self.bounds.width // 2

	def jump(self):
		self.vy = self.jump_power
