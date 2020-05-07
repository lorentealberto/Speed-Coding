class Array(object):
	"""Wrap for a native python array. It does basic operations
		designed to handle multiple video game objects."""
	def __init__(self):
		self.__elements = []

	"""Draw all the elements inside the array.
		Parameters:
			_screen -- Surface (Screen) where the elements will be drawn."""
	def render(self, _screen):
		for element in self.__elements:
			element.render(_screen)

	"""Updates all the elements of the array.
		Parameters:
			_dt -- Delta Time, time that has elapsed since the last
				that this method was executed."""
	def update(self, _dt, _resources_needed = None):
		for element in self.__elements:
			element.update(_dt, _resources_needed)

			if not element.isAlive():
				self.__elements.remove(element)

	"""Add a new item to the list.
		Parameters:
			_element -- Element to be added to the list."""
	def add_element(self, _element):
		self.__elements.append(_element)

	"""Remove an item from the list.
		Parameters:
			_element -- List item to be deleted."""
	def remove_element(self, _element):
		self.__elements.remove(_element)

	def intersect(self, _bounds):
		for element in self.__elements:
			if _bounds.colliderect(element.getBounds()):
				return True
		return False