import pygame as py

from gestor_estados import GestorEstados

WIDTH = 512
HEIGHT = 480
TITLE = "Popeye"

def main():
	py.init()
	screen = py.display.set_mode((WIDTH, HEIGHT))
	py.display.set_caption(TITLE)
	(32, 210, 48, 61)

	exit = False
	clear_color = (0, 0, 0)
	fps = py.time.Clock()
	delta = 0

	gestor_estados = GestorEstados()

	while not exit:
		for event in py.event.get():
			if event.type == py.QUIT:
				exit = True

		screen.fill(clear_color)

		gestor_estados.update(delta)
		gestor_estados.render(screen)

		py.display.update()
		delta = fps.tick(60)
	py.quit()

if __name__ == "__main__":
	main()