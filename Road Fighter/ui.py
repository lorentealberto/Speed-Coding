import pygame as py
from settings import WIDTH


class UI(object):

	def __init__(self):
		self.font = py.font.Font(None, 50)

		self.score = 0
		self.label_score = self.font.render("Score: %d" % (self.score), 0, (255, 255, 255))

	def update(self, _dt):
		self.label_score = self.font.render("Score: %d" % (self.score), 0, (255, 255, 255))

	def render(self, _screen):
		_screen.blit(self.label_score, (WIDTH // 3 - self.label_score.get_width() // 2, 20))