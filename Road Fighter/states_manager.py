from pixelsmash.array import Array
from main_menu import MainMenu
from game import Game


class StatesManager(object):

	def __init__(self):
		self.states = Array()
		#self.states.add_element(MainMenu(self))
		self.states.add_element(Game(self))

	def update(self, _dt):
		self.states.update_current_state(_dt)

	def render(self, _screen):
		self.states.render_current_state(_screen)

	def change_state(self, _state):
		self.states.elemento_actual = _state