class Array(object):
	"""Envoltura para un array nativo de Python. Hace operaciones básicas
		destinadas a manejar múltiples objetos para videojuegos."""
	def __init__(self):
		self.array = []
		self.elemento_actual = 0

	"""Dibuja todos los elemento que hay dentro del array.
		Parámetros:
			_pantalla -- Superficie (Pantalla) donde se dibujarán los elementos."""
	def dibujar(self, _pantalla):
		for elemento in self.array:
			elemento.dibujar(_pantalla)

	"""Actualiza todos los elementos del array.
		Parámetros:
			_dt -- Delta Time, tiempo que ha transcurrido desde la última vez
				que se ejecutó este método."""
	def actualizar(self, _dt):
		for i, elemento in enumerate(self.array):
			elemento.actualizar(_dt)
			self.elemento_actual = i

	"""Obtiene el elemento de la lista que se está actualizando actualmente.
		Devuelve:
			El elemento de la lista que se está actualizando actualmente."""
	def obtener_elemento_actual(self):
		return self.elemento_actual

	"""Añade un nuevo elemento a la lista.
		Parámetros:
			_elemento -- Elemento que se añadirá a la lista."""
	def añadir_elemento(self, _elemento):
		self.array.append(_elemento)

	"""Elimina un elemento de la lista.
		Parámetros:
			_elemento -- Elemento de la lista que se eliminará."""
	def eliminar_elemento(self, _elemento):
		self.array.remove(_elemento)