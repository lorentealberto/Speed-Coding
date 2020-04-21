from game import Game


class StatesManager(object):

	def __init__(self):
		self.states = [Game(self)]
		self.current_state = 0

	def render(self, _screen):
		self.states[self.current_state].render(_screen)

	def update(self, _dt):
		self.states[self.current_state].update(_dt)