import pygame as py

from pixelsmash.funciones import cargar_img
from pixelsmash.timer import Timer

from settings import WIDTH, HEIGHT

class MainMenu(object):

	def __init__(self, _states_manager):
		self.start_game = Timer(1000)
		self.logo = cargar_img("menu/logo_intro")
		self.levels = cargar_img("menu/levels_tag")
		self.selector = cargar_img("menu/selector")
		self.confirm_start_game = False

		self.blink_selection = Timer(200)
		self.blink_enabled = False

		self.states_manager = _states_manager

	def update(self, _dt):
		key = py.key.get_pressed()
		if key[py.K_RETURN]:
			self.confirm_start_game = True

		if self.confirm_start_game:
			self.start_game.update(_dt)
			self.blink_selection.update(_dt)
			
			if self.start_game.tick:
				self.states_manager.change_state(1)

			if self.blink_selection.tick:
				self.blink_enabled = not self.blink_enabled

	def render(self, _screen):
		_screen.blit(self.logo, (WIDTH // 2 - self.logo.get_width() // 2, 50))
		_screen.blit(self.levels, (WIDTH // 2 - self.levels.get_width() // 2, 200))
		_screen.blit(self.selector, (WIDTH // 2 - self.selector.get_width() * 3, 200))

		if self.blink_enabled:
			py.draw.rect(_screen, (0, 0, 0), (WIDTH // 2 - self.levels.get_width() // 2, 200, self.levels.get_width(), self.levels.get_height() // 2))