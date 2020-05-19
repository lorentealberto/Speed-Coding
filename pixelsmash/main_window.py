import pygame as py


class MainWindow(object):
    def __init__(self, _width, _height, _title, _states_manager):
        py.init()
    
        screen = py.display.set_mode(_width, _height)
        py.display.set_caption(_title)

        clear_color = (0, 0, 0)
        exit_game = False
        frames_per_second = py.time.Clock()
        delta = 0

        states_manager = _states_manager

        while not exit_game:
            for event in py.event.get():
                if event.type == py.QUIT:
                    exit_game = True
            
            screen.fill(clear_color)

            states_manager.update(delta)
            states_manager.render(screen)

            py.display.update()
            delta = frames_per_second.tick(60)
        py.quit()