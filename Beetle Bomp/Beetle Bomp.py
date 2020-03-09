import pygame as py
import random, sys

WIDTH = 640
HEIGHT = 480
TITLE = "Beetle Bomp"

            
class Bola(object):
    def __init__(self):
        self.img = self.load_imgs()

        self.bounds = py.Rect(WIDTH // 2, HEIGHT - HEIGHT // 3, self.img[0].get_width(), self.img[1].get_height())

        self.id_bola = random.randrange(5)
        self.speed = 6
        self.lanzar_bola = False
        self.vx = 4

    def render(self, screen):
        screen.blit(self.img[self.id_bola], self.bounds)

    def update(self):
        self.controls()
        self.check_bounds()

    def load_imgs(self):
        self.imgs = []
        for i in range(1, 6):
            img = py.image.load("beetle_graphics/balls/ball_" + str(i) + ".png")
            self.imgs.append(img)
        return self.imgs

    def controls(self):
        key = py.key.get_pressed()

        if key[py.K_SPACE]:
            self.lanzar_bola = True

        if key[py.K_RIGHT]:
            self.bounds.move_ip(self.vx, 0)
        elif key[py.K_LEFT]:
            self.bounds.move_ip(-self.vx, 0)

        if self.lanzar_bola:
            self.disparar_bola()

        if key[py.K_UP]:
            self.reset()

    def disparar_bola(self):
        self.bounds.move_ip(0, -self.speed)

    def reset(self):
        self.lanzar_bola = False
        self.id_bola = random.randrange(5)
        self.bounds.x = WIDTH // 2
        self.bounds.y = HEIGHT - HEIGHT // 3

    def check_bounds(self):
        if self.bounds.top < 0:
            self.reset()


class Beetles(object):
    def __init__(self, puntos_clave):
        
        self.imgs = self.load_images()
        self.ordenados = []
        self.generar_grupos(puntos_clave[0])

        self.puntos_clave = puntos_clave

    def render(self, screen):
        for beetle in self.ordenados:
            beetle.render(screen)
        
    def update(self):
        for beetle in self.ordenados:
            beetle.update(self.puntos_clave)

    def generar_grupos(self, start_point):
        for i in range(5):
            _id = random.randrange(5)
            img = self.imgs[_id]
            for i in range(2):
                self.ordenados.append(Beetle(_id, img, 0, 0))

        self.establecer_posicion(start_point)

    def establecer_posicion(self, start_point):
        for i, beetle in enumerate(self.ordenados):
            beetle.bounds.x = start_point[0] + (i * 30) - beetle.img.get_width()
            beetle.bounds.y = start_point[1] - beetle.img.get_height()


    def load_images(self):
        self.imgs = []
        for i in range(1, 7):
            img = py.image.load("beetle_graphics/beetles/beetle_" + str(i) + ".png").convert_alpha()
            img = py.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            img = py.transform.rotate(img, -90)
            self.imgs.append(img)
        return self.imgs

class Beetle(object):
    def __init__(self, _id, img, x, y):
        self.img = img
        self.bounds = py.Rect(x, y, self.img.get_width(), self.img.get_height())
        self.speed = 1
        self.angle = -90
        self.id = _id

        self.first_point = self.second_point = self.third_point = False

    def render(self, screen):
        screen.blit(self.img, (self.bounds.center[0], self.bounds.center[1]))

    def update(self, puntos_clave):
        if self.bounds.center[0] + self.bounds.width // 2 < puntos_clave[1][0] and not self.first_point:
            self.bounds.move_ip(self.speed, 0)
            
            if self.bounds.center[0] + self.bounds.width // 2 == puntos_clave[1][0]:
                self.first_point = True

        if  self.bounds.center[1] + self.bounds.height // 2 < puntos_clave[2][1] and self.first_point and not self.second_point:
            if self.angle >= -90:
                self.img = py.transform.rotate(self.img, -90)
                self.angle -= 90

            if self.bounds.center[1] + self.bounds.height // 2 == puntos_clave[2][1] - 2:
                self.second_point = True

            self.bounds.move_ip(0, self.speed)

        
        if self.bounds.center[0] + self.bounds.width // 2 > puntos_clave[3][0] and self.second_point and not self.third_point:
            
            
            if self.angle >= -180:
                self.img = py.transform.rotate(self.img, -90)
                self.angle -= 90
            self.bounds.move_ip(-self.speed, 0)

            if self.bounds.center[0] + self.bounds.width // 2 == puntos_clave[3][0]:
                
                self.third_point = True
            


class Camino(object):
    def __init__(self):
        self.puntos_clave = [(20, 50), (WIDTH - 20, 50), (WIDTH - 20, 100), (20, 100)]
        self.flor = py.image.load("beetle_graphics/flower.png")
        self.flor_bounds = py.Rect(0, 0, self.flor.get_width(), self.flor.get_height())
        self.flor_bounds.center = self.puntos_clave[3]

    def render(self, screen):

        #for punto in self.puntos_clave:
         #   py.draw.circle(screen, (255, 0, 0), punto, 5)

        for i in range(len(self.puntos_clave) - 1):
            py.draw.line(screen, (255, 255, 255), self.puntos_clave[i], self.puntos_clave[i + 1])

        screen.blit(self.flor, self.flor_bounds)


class Juego(object):
    def __init__(self):
        self.camino = Camino()
        
        self.beetles = Beetles(self.camino.puntos_clave)

        self.bola = Bola()

    def render(self, screen):
        self.camino.render(screen)
        self.beetles.render(screen)

        self.bola.render(screen)

    def update(self):
        self.beetles.update()
        self.bola.update()

        self.comprobar_colisiones()

    def comprobar_colisiones(self):
        for i, beetle in enumerate(self.beetles.ordenados):
            if beetle.bounds.colliderect(self.bola.bounds):
                if self.bola.id_bola == beetle.id:
                    if i == len(self.beetles.ordenados) - 1:
                        if beetle.id == self.beetles.ordenados[i - 1].id:
                            self.beetles.ordenados.pop(i)
                            self.beetles.ordenados.pop(i - 1)
                            self.bola.reset()
                            break
                    else:
                        if self.beetles.ordenados[i - 1].id == beetle.id:
                            self.beetles.ordenados.pop(i)
                            self.beetles.ordenados.pop(i - 1)
                            self.bola.reset()
                        elif  self.beetles.ordenados[i + 1].id == beetle.id:
                            self.beetles.ordenados.pop(i)
                            self.beetles.ordenados.pop(i)
                            self.bola.reset()
                            

def main():

    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption(TITLE)

    exit = False
    clear = (0, 100, 50)
    fps = py.time.Clock()

    juego = Juego()
    while not exit:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit(0)

        screen.fill(clear)

        juego.update()
        juego.render(screen)
        
        py.display.update()
        fps.tick(60)
        
        
    

if __name__ == "__main__":
    main()
