from pixelsmash.functions import check_single_object_collision, read_key, load_img

from settings import SWIDTH, SHEIGHT
from player_1 import Player_1
from player_2 import Player_2
from ball import Ball


class Game(object):

	def __init__(self, _states_manager):
		self.press_space = load_img("press_space")
		self.pause = True

		self.player_1 = Player_1()
		self.player_2 = Player_2()
		self.ball = Ball()

	def render(self, _screen):
		if self.pause:
			_screen.blit(self.press_space, (SWIDTH // 2 - self.press_space.get_rect().width // 2, SHEIGHT // 2 - self.press_space.get_rect().height // 2))
		else:
			self.player_1.render(_screen)
			self.player_2.render(_screen)
			self.ball.render(_screen)

	def update(self, _dt):
		if not self.pause:
			self.player_1.update(_dt)
			self.player_2.update(_dt)
			self.ball.update(_dt)
			self.check_collisions()
			self.check_score()
		else:
			if read_key() == "SPACE":
				self.pause = False

	def check_collisions(self):
		if (check_single_object_collision(self.player_1, self.ball) or
				check_single_object_collision(self.player_2, self.ball)):
			self.ball.switch_speed()

	def check_score(self):
		if self.ball.bounds.right < 0 or self.ball.bounds.left > SWIDTH:
			self.pause = True
			self.ball.reset()
			self.player_1.reset()
			self.player_2.reset()