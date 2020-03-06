import pygame as py
import sys

WIDTH = 640
HEIGHT = 480
TITLE = "PONG"

class Jugador(object):
    def __init__(self):

        self.width = 15
        self.height = 100

        self.bounds = py.Rect(20, HEIGHT // 2 - self.height // 2, self.width, self.height)
        self.color = (255, 255, 255)
        self.vy = 0
        self.speed = 5

    def render(self, screen):
        py.draw.rect(screen, self.color, self.bounds)

    def update(self):
        self.controls()
        self.move()
        self.check_borders()

    def controls(self):
        key = py.key.get_pressed()
        if key[py.K_UP]:
            self.vy -= self.speed
        elif key[py.K_DOWN]:
            self.vy += self.speed
        else:
            self.vy = 0

    def move(self):
        self.bounds.move_ip(0, self.vy)

    def check_borders(self):
        if self.bounds.y < 0:
            self.bounds.y = 0
        elif self.bounds.bottom > HEIGHT:
            self.bounds.bottom = HEIGHT


class Pelota(object):
    def __init__(self):
        self.size = 5
        self.hit_box_size = 6

        self.bounds = py.Rect(WIDTH // 2 - self.size // 2, HEIGHT // 2 - self.size // 2, self.size, self.size)
        self.hit_box = py.Rect(WIDTH // 2 - self.hit_box_size // 2, HEIGHT // 2 - self.hit_box_size // 2, self.hit_box_size, self.hit_box_size)

        self.color = (255, 255, 255)
        self.hit_box_color = (255, 0, 0)

        self.speed = 5
        self.vx = self.vy = self.speed
        

    def render(self, screen):
        py.draw.rect(screen, self.color, self.bounds)
        py.draw.rect(screen, self.hit_box_color, self.hit_box)

    def update(self):
        self.move()
        self.check_borders()

    def move(self):
        self.bounds.move_ip(self.vx, self.vy)
        self.hit_box.center = self.bounds.center

    def check_borders(self):
        if self.bounds.right < 0:
            self.bounds.right = 0
            self.vx *= -1
        elif self.bounds.left > WIDTH:
            self.bounds.left = WIDTH
            self.vx *= -1

        if self.bounds.top < 0:
            self.bounds.top = 0
            self.vy *= -1
        elif self.bounds.bottom > HEIGHT:
            self.bounds.bottom = HEIGHT
            self.vy *= -1

class Contrincante(object):
    def __init__(self):
        self.width = 15
        self.height = 100

        self.bounds = py.Rect(WIDTH - 20 - self.width, HEIGHT // 2 - self.height // 2, self.width, self.height)
        self.color = (255, 255, 255)
        self.speed = 5
        self.vy = 0

    def render(self, screen):
        py.draw.rect(screen, self.color, self.bounds)

    def update(self, pelota):
        self.move(pelota)
        self.check_borders()

    def move(self, pelota):
        if self.bounds.center[1] < pelota.bounds.y + pelota.bounds.height:
            self.vy = self.speed
        elif self.bounds.center[1] > pelota.bounds.y + pelota.bounds.height:
            self.vy = -self.speed
        else:
            self.vy = 0

        self.bounds.move_ip(0, self.vy)

    def check_borders(self):
        if self.bounds.top < 0:
            self.bounds.top = 0
        elif self.bounds.bottom > HEIGHT:
            self.bounds.bottom = HEIGHT
        
class Juego(object):
    def __init__(self):
        self.jugador = Jugador()
        self.pelota = Pelota()
        self.contrincante = Contrincante()

    def render(self, screen):
        self.jugador.render(screen)
        self.pelota.render(screen)
        self.contrincante.render(screen)

    def update(self):
        self.jugador.update()
        self.pelota.update()
        self.contrincante.update(self.pelota)
        self.check_collisions()

    def check_collisions(self):
        if (self.jugador.bounds.colliderect(self.pelota.hit_box) or
            self.contrincante.bounds.colliderect(self.pelota.hit_box)):
            self.pelota.vx *= -1


def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption(TITLE)

    exit = False
    clear = (0, 0, 0)
    clock = py.time.Clock()

    juego = Juego()

    while not exit:
        for event in py.event.get():
            if event.type == py.QUIT:
                exit = True

        screen.fill(clear)

        juego.update()
        juego.render(screen)
        


        py.display.update()
        clock.tick(60)

    sys.exit(0)
    
    return 0
if __name__ == "__main__":
    main()
