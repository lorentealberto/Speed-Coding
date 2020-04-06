class Timer(object):
	"""Objeto que sirve como un temporizador, emitiendo pulsos cada X tiempo.
		Parámetros:
			_delay -- Cada cuantos milisegundos se quiere emitir un pulso."""
	def __init__(self, _delay):
		self.time = 0
		self.delay = _delay
		self.tick = False

	def update(self, _dt):
		"""Actualiza los componentes del reloj. También se encarga de emitir el
			pulso correspondiente una vez que haya pasado el tiempo necesario.
			Parámetros:
				_dt -- Tiempo en milisegundos que ha transcurrido desde que se
					llamó a este método por última vez."""
		self.tick = False
		self.time += _dt
		if self.time > self.delay:
			self.time = 0
			self.tick = True

	def parar(self):
		"""Detiene / Resetea el reloj."""
		self.time = 0