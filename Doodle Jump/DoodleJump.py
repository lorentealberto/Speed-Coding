import pygame as py

from settings import WIDTH, HEIGHT, TITLE
from states_manager import StatesManager


def main():
	py.init()
	screen = py.display.set_mode((WIDTH, HEIGHT))
	py.display.set_caption(TITLE)

	exit = False
	FPS = py.time.Clock()
	delta = 0
	cc = (255, 253, 231)

	sm = StatesManager()

	while not exit:
		for event in py.event.get():
			if event.type == py.QUIT:
				exit = True

		screen.fill(cc)
		sm.update(delta)
		sm.render(screen)
		py.display.update()
		delta = FPS.tick(60)

	py.quit()

if __name__ == "__main__":
	main()