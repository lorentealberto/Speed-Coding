from pixelsmash.functions import load_img, read_key

class MainMenu(object):

	def __init__(self, _states_manager):
		self.background = load_img("main_menu")
		self.states_manager = _states_manager

	def update(self, _dt):
		if read_key() == "ENTER":
			self.states_manager.switch_state(1)

	def render(self, _screen):
		_screen.blit(self.background, (0, 0))