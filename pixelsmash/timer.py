class Timer(object):
	"""Object that serves as a timer, emitting pulses every X time.
		Parameters:
			Delay -- Every few milliseconds you want to emit a pulse."""
	def __init__(self, _delay):
		self.time = 0
		self.delay = _delay
		self.tick = False

	def update(self, _dt):
		"""Updates the clock components. It also issues the
			corresponding pulse once the necessary time has elapsed.
			Parameters:
				dt -- Time in milliseconds that has elapsed since
					called this method for the last time."""
		self.tick = False
		self.time += _dt
		if self.time > self.delay:
			self.time = 0
			self.tick = True

	def stop(self):
		"""Stop / Reset the clock."""
		self.time = 0