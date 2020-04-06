import pygame as py

from gestor_estados import GestorEstados

WIDTH = 480
HEIGHT = 320
TITLE = "Arkanoid"

def main():
	py.init()
	pantalla = py.display.set_mode((WIDTH, HEIGHT))
	py.display.set_caption(TITLE)

	exit = False
	color_fondo = (0, 0, 0)
	FPS = py.time.Clock()
	delta = 0

	gestor = GestorEstados()

	while not exit:
		for event in py.event.get():
			if event.type == py.QUIT:
				exit = True

		pantalla.fill(color_fondo)

		gestor.actualizar(delta)
		gestor.dibujar(pantalla)

		py.display.update()
		delta = FPS.tick(60)
	py.quit()

if __name__ == "__main__":
	main()