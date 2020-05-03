class Array(object):
	"""Wrap for a native python array. It does basic operations
		designed to handle multiple video game objects."""
	def __init__(self):
		self.elements = []
		self.current_element = 0

	"""Draw all the elements inside the array.
		Parameters:
			_screen -- Surface (Screen) where the elements will be drawn."""
	def render(self, _screen):
		for element in self.elements:
			element.render(_screen)

	"""Updates all the elements of the array.
		Parameters:
			_dt -- Delta Time, time that has elapsed since the last
				that this method was executed."""
	def update(self, _dt):
		for i, element in enumerate(self.elements):
			element.update(_dt)
			self.current_element = i

	"""Add a new item to the list.
		Parameters:
			_element -- Element to be added to the list."""
	def add_element(self, _element):
		self.array.append(_element)

	"""Remove an item from the list.
		Parameters:
			_element -- List item to be deleted."""
	def remove_element(self, _element):
		self.array.remove(_element)