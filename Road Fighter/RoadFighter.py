import pygame as py

from settings import WIDTH, HEIGHT, TITLE

from states_manager import StatesManager

def main():
	py.init()

	screen = py.display.set_mode((WIDTH, HEIGHT))
	py.display.set_caption(TITLE)

	exit = False
	cc = (0, 0, 0)
	fps = py.time.Clock()

	sm = StatesManager()

	delta = 0

	while not exit:
		for event in py.event.get():
			if event.type == py.QUIT:
				exit = True

		screen.fill(cc)
		sm.update(delta)
		sm.render(screen)
		py.display.update()
		delta = fps.tick(60)
	py.quit()

if __name__ == "__main__":
	main()
