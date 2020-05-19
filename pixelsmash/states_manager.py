class StatesManager(object):
	def __init__(self):
		self.states = []
		self.current_state = -1

	def update(self, _dt):
		self.states[self.current_state].update(_dt)

	def render(self, _screen):
		self.states[self.current_state].render(_screen)

	def add_state(self, _state, _use_state = True):
		self.states.append(_state)

		if _use_state:
			self.current_state = len(self.states) - 1

	def switch_state(self, _state_id):
		if _state_id > 0 and _state_id < len(self.states):
			self.current_state = _state_id
		else:
			print("Cannot switch state: Invalid State ID")