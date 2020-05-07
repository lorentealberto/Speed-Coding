class Timer(object):
	"""Object that serves as a timer, emitting pulses every X time.
		Parameters:
			Delay -- Every few milliseconds you want to emit a pulse."""
	def __init__(self, _delay):
		self.__time = 0
		self.__delay = _delay
		self.__tick = False

	def update(self, _dt):
		"""Updates the clock components. It also issues the
			corresponding pulse once the necessary time has elapsed.
			Parameters:
				dt -- Time in milliseconds that has elapsed since
					called this method for the last time."""
		self.__tick = False
		self.__time += _dt
		if self.__time > self.__delay:
			self.__time = 0
			self.__tick = True

	def stop(self):
		"""Stop / Reset the clock."""
		self.__time = 0

	def getTick(self):
		return self.__tick