class Timer(object):

	def __init__(self, _delay):
		self.time = 0
		self.delay = _delay
		self.tick = False

	def update(self, dt):
		self.tick = False
		self.time += dt

		if self.time > self.delay:
			self.time = 0
			self.tick = True


	def parar(self):
		self.time = 0
