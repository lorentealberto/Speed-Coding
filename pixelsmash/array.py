class Array(object):
	"""Envoltura para un array nativo de Python. Hace operaciones básicas
		destinadas a manejar múltiples objetos para videojuegos."""
	def __init__(self):

		self.array = []
		self.elemento_actual = 0
		self.element_deleted = False


	"""Dibuja todos los elemento que hay dentro del array.
		Parámetros:
			_pantalla -- Superficie (Pantalla) donde se dibujarán los elementos."""
	def render(self, _pantalla):
		for elemento in self.array:
			elemento.render(_pantalla)

	"""Actualiza todos los elementos del array.
		Parámetros:
			_dt -- Delta Time, tiempo que ha transcurrido desde la última vez
				que se ejecutó este método."""
	def update(self, _dt):
		self.element_deleted = False
		for i, elemento in enumerate(self.array):
			elemento.update(_dt)
			self.elemento_actual = i
			if not elemento.alive:
				self.delete_element(elemento)
				self.element_deleted = True

	"""Obtiene el elemento de la lista que se está actualizando actualmente.
		Devuelve:
			El elemento de la lista que se está actualizando actualmente."""
	def get_current_element(self):
		if len(self.array) > 0:
			return self.array[self.elemento_actual]
		else:
			return None

	"""Añade un nuevo elemento a la lista.
		Parámetros:
			_elemento -- Elemento que se añadirá a la lista."""
	def add_element(self, _elemento):
		self.array.append(_elemento)

	"""Elimina un elemento de la lista.
		Parámetros:
			_elemento -- Elemento de la lista que se eliminará."""
	def delete_element(self, _elemento):
		self.elemento_actual = 0
		self.array.remove(_elemento)

	def render_current_state(self, _screen):
		self.array[self.elemento_actual].render(_screen)

	def update_current_state(self, _dt):
		self.array[self.elemento_actual].update(_dt)		