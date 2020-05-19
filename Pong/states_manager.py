from pixelsmash.states_manager import PSStatesManager

from main_menu import MainMenu
from game import Game

class StatesManager(PSStatesManager):

	def __init__(self):
		PSStatesManager.__init__(self)

		self.add_state(MainMenu(self))
		self.add_state(Game(self), False)
