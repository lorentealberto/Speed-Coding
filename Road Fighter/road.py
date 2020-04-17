import random

from pixelsmash.funciones import cargar_img
from pixelsmash.array import Array

from settings import WIDTH, HEIGHT

from road_piece import RoadPiece

class Road(object):

	def __init__(self):
		random.seed()

		self.road_start = cargar_img("road/road_start", 2)
		self.road_piece = cargar_img("road/road", 2)
		self.x = WIDTH // 2 - self.road_start.get_width() // 2
		self.y = 0

		self.road = Array()
		self.load_road()

	def update(self, _dt, _UI):
		self.road.update(_dt)

		if self.road.element_deleted:
			self.road.add_element(RoadPiece(self.road_piece, self.x, -self.road_piece.get_height()))
			_UI.score += 1

	def render(self, _screen):
		self.road.render(_screen)

	def load_road(self):
		for i in range(-1, HEIGHT // self.road_piece.get_height() + 1):
			self.road.add_element(RoadPiece(self.road_piece, self.x, i * self.road_piece.get_height()))

	def stop(self):
		for road_piece in self.road.array:
			road_piece.road_speed = 0