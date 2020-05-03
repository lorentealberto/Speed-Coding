import pygame as py
from settings import WIDTH, HEIGHT, TITLE
from tests import Tests

def main():
	py.init()
	screen = py.display.set_mode((WIDTH, HEIGHT))
	py.display.set_caption(TITLE)

	cc = (0, 0, 0)
	exit = False
	FPS = py.time.Clock()
	dt = 0

	tests = Tests()

	while not exit:
		for event in py.event.get():
			if event.type == py.QUIT:
				exit = True

		screen.fill(cc)

		tests.update(dt)
		tests.render(screen)
		py.display.update()
		dt = FPS.tick(60)
	py.quit()

if __name__ == "__main__":
	main()