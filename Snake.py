import math, random, pygame as py

WIDTH = 500
ROWS = 20
TITLE = "SNAKE"

#Author: Alberto Lorente
#Date: 25/04/2020

class Cube(object):
	"""Represent a block within the game. Cubes are used to form the other
		elements within the game, both the snake's body parts like food.
		Parameters:
			_position: Cube position. By default it will take the coordinate (0, 0)
				that is, the upper left corner of the screen.
			_vx: Horizontal velocity that the cube will have. Not all elements
				of the game will move. The default value is 1.
			_vy: Vertical speed that the cube will have. Not all elements
				of the game will move. The default value is 0.
			_color: Color to be used to fill the cube. The value for
				default is (255, 0, 0), the color red in RGB notation."""
	def __init__(self, _position = (0, 0), _vx = 1, _vy = 0, _color = (255, 0, 0)):
		self.position = _position
		self.vx = _vx
		self.vy = _vy
		self.color = _color

	def move(self, _speed):
		"""Apply a certain speed to the cube.
			Parameters:
				_speed: Velocity vector to be applied to the cube."""
		self.vx, self.vy = _speed

		self.position = (self.position[0] + self.vx, self.position[1] + self.vy)

	def render(self, _screen):
		"""Draw the cube on the past surface as a parameter.
			_screen: Surface where the cube will be drawn."""
		body = WIDTH // ROWS
		i, j = self.position

		py.draw.rect(_screen, self.color, (i * body + 1, j * body + 1, body - 2, body - 2))

	def generateRndPosition(self, _snake):
		"""It generates a random position for the cube. This position will be
			completely different from anywhere else you are
			some part of the snake's body.
			Parameters:
				_snake: Reference to the snake-type object to avoid
					that the food is generated on the snake."""
		positions = _snake.body

		while True:
			x = random.randrange(ROWS)
			y = random.randrange(ROWS)

			if len(list(filter(lambda z: z.position == (x, y), positions))):
				continue
			else:
				break
		self.position = (x, y)


class Snake(object):
	"""Snake-type object. It is the object that controls the player.
		Parameters:
			_position: Position where the snake will initially be placed.
			_color: The color the snake will have. By default the snake
				will be red, (255, 0, 0) in RGB notation."""
	def __init__(self, _position, _color = (255, 0, 0)):
		self.body, self.turns = [], {}
		self.color = _color
		self.head = Cube(_position)
		self.body.append(self.head)
		self.vx, self.vy = 0, 1

	def update(self, _snack):
		"""Update all elements of the snake.
			Parameters:
				_snack: Reference to the bucket that represents the food for
					check the collision between him and the snake."""
		self.controls()
		self.move()
		self.eatSnack(_snack)
		self.checkSelfCollision()

	def controls(self):
		"""Checks the keystrokes to do one action or another
			depending on which key we pressed."""
		key = py.key.get_pressed()

		if key[py.K_LEFT]:
			self.vx, self.vy = -1, 0
			self.turns[self.head.position[:]] = [self.vx, self.vy]
		elif key[py.K_UP]:
			self.vx, self.vy = 0, -1
			self.turns[self.head.position[:]] = [self.vx, self.vy]
		elif key[py.K_RIGHT]:
			self.vx, self.vy = 1, 0
			self.turns[self.head.position[:]] = [self.vx, self.vy]
		elif key[py.K_DOWN]:
			self.vx, self.vy = 0, 1
			self.turns[self.head.position[:]] = [self.vx, self.vy]

	def move(self):
		"""It moves all parts of the snake's body, depending
			of the action assigned to each of the parties."""
		for i, cube in enumerate(self.body):
			position = cube.position[:]

			if position in self.turns:
				turn = self.turns[position]
				cube.move(turn)
				if i == len(self.body) - 1:
					self.turns.pop(position)
			else:
				posX, posY = cube.position

				if cube.vx == -1 and posX <= 0:
					cube.position = (ROWS - 1, posY)
				elif cube.vx == 1 and posX >= ROWS - 1:
					cube.position = (0, posY)
				elif cube.vy == 1 and posY >= ROWS - 1:
					cube.position = (posX, 0)
				elif cube.vy == -1 and posY <= 0:
					cube.position = (posX, ROWS - 1)
				else:
					cube.move((cube.vx, cube.vy))

	def reset(self, _position):
		"""Restores the snake to its original values and removes all
			the body parts."""
		self.head = Cube(_position)
		self.body, self.turns = [], {}
		self.body.append(self.head)
		self.vx, self.vy = 0, 1

	def addCube(self):
		"""Add a new body part to the snake. The position in the
			that the new part will be added, depends on the action assigned to it
			the tail of the snake."""
		tail = self.body[-1]
		tailPositionX, tailPositionY = tail.position
		dx, dy = tail.vx, tail.vy

		if dx == 1:
			self.body.append(Cube((tailPositionX - 1, tailPositionY)))
		elif dx == -1:
			self.body.append(Cube((tailPositionX + 1, tailPositionY)))
		elif dy == 1:
			self.body.append(Cube((tailPositionX, tailPositionY - 1)))
		elif dy == -1:
			self.body.append(Cube((tailPositionX, tailPositionY + 1)))

		self.body[-1].vx = dx
		self.body[-1].vy = dy

	def render(self, _screen):
		"""Draw all parts of the
			snake.
			Parameters:
				_screen: Surface where all parts of the
					snake."""
		for cube in self.body:
			cube.render(_screen)

	def eatSnack(self, _snack):
		"""Check the collision between the head of the snake (The first
			body part) and the reference to 'snack'.
			Parameters:
				_snack: Reference to the 'snack' type object"""
		if self.body[0].position == _snack.position:
			self.addCube()
			_snack.generateRndPosition(self)

	def checkSelfCollision(self):
		"""Check the collision between the snake's head and all the
			parts of his body. If the head hits any of the parts of the
			body, the game will be restarted."""
		for i in range(len(self.body)):
			if self.body[i].position in list(map(lambda z: z.position, self.body[i + 1:])):
				self.reset((10, 10))
				break


def renderGrid(_screen):
	"""Draws the grid on the passed surface as a parameter.
		Parameters:
			_screen: Surface where the grid will be drawn."""
	spaceBtwn = WIDTH // ROWS
	x = y = 0

	for i in range(ROWS):
		x += spaceBtwn
		y += spaceBtwn

		py.draw.line(_screen, (255, 255, 255), (x, 0), (x, WIDTH))
		py.draw.line(_screen, (255, 255, 255), (0, y), (WIDTH, y))


def main():
	py.init()
	random.seed()
	screen = py.display.set_mode((WIDTH, WIDTH))
	py.display.set_caption(TITLE)

	exit = False
	cc = (0, 0, 0)
	FPS = py.time.Clock()

	snake = Snake((10, 10))
	snack = Cube(_color = (0, 255, 0))
	snack.generateRndPosition(snake)

	while not exit:
		for event in py.event.get():
			if event.type == py.QUIT:
				exit = True

		screen.fill(cc)

		snake.update(snack)
		snake.render(screen)
		snack.render(screen)
		renderGrid(screen)

		py.display.update()
		py.time.delay(50)
		FPS.tick(10)

	py.quit()


if __name__ == "__main__":
	main()