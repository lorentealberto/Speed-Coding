import pygame as py
import random, sys

WIDTH = 640
HEIGHT = 480
TITLE = "Space Invaders"

def load_image(path, scale = 1):
    _img = py.image.load("resources/graphics/"+path+".png").convert_alpha()
    _img = py.transform.scale(_img, (scale * _img.get_width(), scale * _img.get_height()))
    return _img


class Fondo(object):

    def __init__(self):
        self.lista_estrellas = [Estrella()]
        self.time = 0
        self.tiempo_aparicion = random.randrange(100, 1200)

    def render(self, screen):
        for estrella in self.lista_estrellas:
            estrella.render(screen)

    def update(self, dt):
        self.crear_estrellas(dt)
        for estrella in self.lista_estrellas:
            estrella.update()

            if estrella.muerta:
                self.lista_estrellas.remove(estrella)
                

    def crear_estrellas(self, dt):
        self.time += dt

        if self.time > self.tiempo_aparicion:
            self.time = 0
            self.tiempo_aparicion = (random.randrange(100, 1200))
            self.lista_estrellas.append(Estrella())


class Estrella(object):

    def __init__(self):
        self.bounds = py.Rect(random.randrange(20, WIDTH - 20), random.randrange(-50, 0), 5, 5)
        self.muerta = False

    def render(self, screen):
        py.draw.rect(screen, (255, 255, 255), self.bounds)

    def update(self):
        self.bounds.move_ip(0, 1)
        if self.bounds.top > HEIGHT:
            self.muerta = True

class ProyectilesEnemigos(object):

    def __init__(self):
        self.lista_proyectiles = []
        self.img = load_image("rayo_laser", 2)

    def render(self, screen):
        for proyectil in self.lista_proyectiles:
            proyectil.render(screen)

    def update(self, dt):
        for proyectil in self.lista_proyectiles:
            proyectil.update(dt)

            if proyectil.muerto:
                self.lista_proyectiles.remove(proyectil)

    def añadir_proyectil(self, x, y):
        self.lista_proyectiles.append(ProyectilEnemigo(self.img, x, y))


class ProyectilEnemigo(object):

    def __init__(self, _img, _x, _y):
        self.img = _img
        self.bounds = py.Rect(_x, _y, self.img.get_width(), self.img.get_height())
        self.vy = 1
        self.muerto = False
        self.time = 0
        self.tiempo_animacion = 250

    def render(self, screen):
        screen.blit(self.img, self.bounds)

    def update(self, dt):
        self.mover()
        self.actualizar_animacion(dt)

    def mover(self):
        self.bounds.move_ip(0, self.vy)
        if self.bounds.bottom > HEIGHT - HEIGHT // 8:
            self.muerto = True

    def actualizar_animacion(self, dt):
        self.time += dt

        if self.time > self.tiempo_animacion:
            self.time = 0
            self.img = py.transform.flip(self.img, True, False)
        

class Enemigos(object):

    def __init__(self):
        self.imgs_calavera = self.cargar_imagenes_calavera()
        self.imgs_aliens = self.cargar_imagenes_alien()
        self.imgs_calamar = self.cargar_imagenes_calamar()
        
        self.lista_enemigos = []
        
        self.crear_grupo_calaveras()
        self.crear_grupo_aliens()
        self.crear_grupo_calamares()

        self.time = 0
        self.cada_cuanto_mover = 1000
        self.mover_enemigos = False
        self.vx = self.vy = 0
        self.speed = 10
        self.acciones = [(self.speed, 0), (self.speed, 0), (0, self.speed), (-self.speed, 0), (-self.speed, 0), (0, self.speed)]
        self.accion_actual = 0

        self.proyectiles = ProyectilesEnemigos()
        self.tiempo_disparo = 0
        self.max_tiempo_disparo = 1500

    def render(self, screen):
        self.proyectiles.render(screen)
        for enemigo in self.lista_enemigos:
            enemigo.render(screen)

    def update(self, dt):
        self.proyectiles.update(dt)
        self.disparar(dt)
        if not self.mover_enemigos:
            self.temporizador_mover(dt)
            
        for enemigo in self.lista_enemigos:
            enemigo.update(dt, self.vx, self.vy)
            if enemigo.muerto:
                self.lista_enemigos.remove(enemigo)

        self.mover_enemigos = False
        self.vx = 0
        self.vy = 0

    def temporizador_mover(self, dt):
        self.time += dt

        if self.time > self.cada_cuanto_mover:
            self.time = 0
            self.mover_enemigos = True
            self.vx, self.vy = self.acciones[self.accion_actual]
            self.accion_actual += 1
            if  self.accion_actual > len(self.acciones) - 1:
                self.accion_actual = 0

    def disparar(self, dt):
        self.tiempo_disparo += dt
        if self.tiempo_disparo > self.max_tiempo_disparo:
            self.tiempo_disparo = 0
            x, y = self.lista_enemigos[random.randrange(len(self.lista_enemigos))].bounds.center
            self.proyectiles.añadir_proyectil(x, y)
            
        

    # ---------------- Imágenes
    def cargar_imagenes_calavera(self):
        self.imagenes = []
        for i in range(1, 3):
            self.imagenes.append(load_image("calavera_" + str(i), 2))

        return self.imagenes

    def cargar_imagenes_alien(self):
        self.imagenes = []
        for i in range(1,  3):
            self.imagenes.append(load_image("alien_" + str(i), 2))
        return self.imagenes

    def cargar_imagenes_calamar(self):
        self.imagenes = []
        for i in range(1, 3):
            self.imagenes.append(load_image("calamar_" + str(i), 2))
        return self.imagenes



    # ---------- Grupos
    def crear_grupo_calaveras(self):
        for i in range(11):
            self.lista_enemigos.append(Enemigo(self.imgs_calavera, 130 + (i * self.imgs_calavera[0].get_width() * 2 + 22), 100))
            
    def crear_grupo_aliens(self):
        x = 0
        y = 0
        for i in range(22):
            if i % 11 == 0:
                y += 1
                x = 0
            self.lista_enemigos.append(Enemigo(self.imgs_aliens, 130 + (x * self.imgs_calavera[0].get_width() * 2 + 20), y * 30 + 100))
            x += 1
            
    def crear_grupo_calamares(self):
        x = 0
        y = 0
        for i in range(22):
            if i % 11 == 0:
                y += 1
                x = 0
            
            self.lista_enemigos.append(Enemigo(self.imgs_calamar, 130 + (x * self.imgs_calavera[0].get_width() * 2 + 20), y * 30 + 165))
            x += 1


class Enemigo(object):

    def __init__(self, _imgs, _x, _y):
        self.imgs = _imgs
        self.bounds = py.Rect(_x, _y, self.imgs[0].get_width(), self.imgs[0].get_height())
        self.vx = self.vy = 0
        self.speed = 5
        self.time = 0
        self.cambiar_frame = 500
        self.frame_actual = 0
        self.muerto = False

    def render(self, screen):
        screen.blit(self.imgs[self.frame_actual], self.bounds)

    def update(self, dt, vx = 0, vy = 0):
        self.actualizar_animacion(dt)
        self.mover(vx, vy)

    def actualizar_animacion(self, dt):
        self.time += dt
        if self.time > self.cambiar_frame:
            self.time = 0
            self.frame_actual += 1

            if self.frame_actual >= len(self.imgs):
                self.frame_actual = 0
                
    def mover(self, vx = 0, vy = 0):
        self.vx = vx
        self.vy = vy
        
        self.bounds.move_ip(self.vx, self.vy)

        if self.vx != 0:
            self.vx = 0
        if self.vy != 0:
            self.vy = 0

    def mover_hacia(self, _lado):
        if _lado == "derecha":
            self.vx = self.speed
        elif _lado == "izquierda":
            self.vx = -self.speed

        if _lado == "abajo":
            self.vy = self.speed


class UI(object):

    def __init__(self):
        self.font = py.font.Font("resources/fonts/space_invaders.ttf", 16)
        self.score = 0
        self.high_score = 0
        self.lives = 3
        self.credits = 0
        self.img_vida = load_image("nave", 2)
        self.img_vida.fill((0, 255, 0), special_flags = py.BLEND_RGB_MULT)
        

    def render(self, screen):
        screen.blit(self.font.render("SCORE< 1 >    HI - SCORE< 2 >", True, (255, 255, 255)), (50, 25))
        screen.blit(self.font.render("%.4d" % self.score, True, (255, 255, 255)), (60, 50))
        screen.blit(self.font.render("%.4d" % self.high_score, True, (255, 255, 255)), (190, 50))

        # ----------------- VIDAS
        py.draw.rect(screen, (0, 255, 0), (0, HEIGHT - 60, WIDTH, 5))
        screen.blit(self.font.render(str(self.lives), True, (255, 255, 255)), (50, HEIGHT - 50))
        self.dibujar_vidas(screen)
        screen.blit(self.font.render("CREDIT  %.2d" % self.score, True, (255, 255, 255)), (WIDTH - 150, HEIGHT - 50))

    def dibujar_vidas(self, screen):
        for i in range(self.lives - 1):            
            screen.blit(self.img_vida, (80 + i * (self.img_vida.get_width() + 10), HEIGHT - 50))


class Barreras(object):

    def __init__(self):
        self.lista_barreras = []
        self.img = load_image("barrera", 2)
        self.img.fill((0, 255, 0), special_flags = py.BLEND_RGB_MULT)
        self.añadir_barreras()

    def render(self, screen):
        for barrera in self.lista_barreras:
            barrera.render(screen)

    def update(self):
        for barrera in self.lista_barreras:
            barrera.update()
            if barrera.destruida:
                self.lista_barreras.remove(barrera)

    def añadir_barreras(self):
        for i in range(4):
            self.lista_barreras.append(Barrera(self.img, 125 + i * (self.img.get_width() * 2 + 25), HEIGHT - HEIGHT // 3 - 10))


class Barrera(object):

    def __init__(self, _img, _x, _y):
        self.img = _img
        self.bounds = py.Rect(_x, _y, _img.get_width(), _img.get_height())
        self.golpes = 0
        self.destruida = False

    def render(self, screen):
        screen.blit(self.img, self.bounds)

    def update(self):
        if self.golpes > 3:
            self.destruida = True
    

class Proyectiles(object):

    def __init__(self):
        self.lista_proyectiles = []

    def render(self, screen):
        for proyectil in self.lista_proyectiles:
            proyectil.render(screen)

    def update(self):
        for proyectil in self.lista_proyectiles:
            proyectil.update()
            if proyectil.die:
                self.lista_proyectiles.remove(proyectil)

    def añadir_proyectil(self, x, y):
        self.lista_proyectiles.append(Proyectil(x, y))


class Proyectil(object):

    def __init__(self, x, y):
        self.bounds = py.Rect(x, y, 2, 10)
        self.vy = 8
        self.die = False

    def render(self, screen):
        py.draw.rect(screen, (255, 255, 255), self.bounds)

    def  update(self):
        self.move()
        self.check_top_screen()

    def move(self):
        self.bounds.move_ip(0, -self.vy)

    def check_top_screen(self):
        if self.bounds.bottom < 0:
            self.die = True
            

class Jugador(object):

    def __init__(self):
        self.img = load_image("nave", 2)
        self.img.fill((0, 255, 0), special_flags = py.BLEND_RGB_MULT)
        self.bounds = py.Rect(WIDTH // 2, HEIGHT - (HEIGHT // 4), self.img.get_width(), self.img.get_height())
        self.vx = 0
        self.speed = 5
        self.can_shoot = True
        self.time = 0
        self.shoot_time = 1000
        self.proyectiles = Proyectiles()
        

    def render(self, screen):
        screen.blit(self.img, self.bounds)
        self.proyectiles.render(screen)

    def update(self, dt):
        self.controls(dt)
        self.move()
        self.check_borders()
        self.proyectiles.update()

    def controls(self, dt):
        key = py.key.get_pressed()

        if key[py.K_LEFT]:
            self.vx = -self.speed
        elif key[py.K_RIGHT]:
            self.vx = self.speed
        else:
            self.vx = 0

        self.shoot_control(key, dt)

    def move(self):
        self.bounds.move_ip(self.vx, 0)

    def check_borders(self):
        if self.bounds.left < 0:
            self.bounds.left = 0
        elif self.bounds.right > WIDTH:
            self.bounds.right = WIDTH

    def shoot_control(self, key, dt):
        if key[py.K_SPACE] and self.can_shoot:
            self.can_shoot = False
            self.shoot()

        self.shoot_timer(dt)

    def shoot(self):
        self.proyectiles.añadir_proyectil(self.bounds.center[0], self.bounds.center[1])

    def shoot_timer(self, dt):
        self.time += dt
        if self.time > self.shoot_time:
            self.time = 0
            self.can_shoot = True


class Juego(object):
    
    def __init__(self):
        self.ui = UI()
        self.jugador = Jugador()
        self.barreras = Barreras()
        self.enemigos = Enemigos()
        self.fondo = Fondo()
        
    def render(self, screen):
        self.fondo.render(screen)
        self.jugador.render(screen)
        self.barreras.render(screen)
        self.enemigos.render(screen)
        self.ui.render(screen)
        
    def update(self, dt):
        self.jugador.update(dt)
        self.barreras.update()
        self.enemigos.update(dt)
        self.comprobar_colisiones()
        self.fondo.update(dt)

    def comprobar_colisiones(self):
        for proyectil in self.jugador.proyectiles.lista_proyectiles:
            for enemigo in self.enemigos.lista_enemigos:
                if proyectil.bounds.colliderect(enemigo.bounds):
                    enemigo.muerto = True
                    proyectil.die = True
                    break

        for proyectil in self.jugador.proyectiles.lista_proyectiles:
            for barrera in self.barreras.lista_barreras:
                if proyectil.bounds.colliderect(barrera.bounds):
                    proyectil.die = True
                    barrera.golpes += 1
                    break
                
        for proyectil_enemigo in self.enemigos.proyectiles.lista_proyectiles:
            for barrera in self.barreras.lista_barreras:
                if proyectil_enemigo.bounds.colliderect(barrera.bounds):
                    proyectil_enemigo.muerto = True
                    barrera.golpes += 1
                    break

        for proyectil_enemigo in self.enemigos.proyectiles.lista_proyectiles:
            if proyectil_enemigo.bounds.colliderect(self.jugador.bounds):
                py.quit()
                sys.exit(0)
                

    
def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption(TITLE)

    clear_color = (0, 0, 0)
    exit = False
    fps = py.time.Clock()
    dt = 0

    juego = Juego()

    while not exit:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit(0)

        screen.fill(clear_color)

        juego.update(dt)
        juego.render(screen)

        py.display.update()
        dt = fps.tick(60)

if __name__ == "__main__":
    main()
