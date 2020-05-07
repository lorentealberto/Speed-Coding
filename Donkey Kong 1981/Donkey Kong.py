import pygame as py

from statesManager import StatesManager

WIDTH = 256 * 2
HEIGHT = 256 * 2
TITLE = "DONKEY KONG"

def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT)) 
    py.display.set_caption(TITLE)

    cc = (0, 0, 0)
    exit = False
    FPS = py.time.Clock()
    delta = 0

    states = StatesManager()

    while not exit:
        for event in py.event.get():
            if event.type == py.QUIT:
                exit = True
        
        screen.fill(cc)

        states.update(delta)
        states.render(screen)

        py.display.update()
        delta = FPS.tick(60)
    py.quit()

if __name__ == "__main__":
    main()