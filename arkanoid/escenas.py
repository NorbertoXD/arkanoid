import os

import pygame as pg

from . import ALTO, ANCHO, COLOR_FONDO_PORTADA, COLOR_MENSAJE, FPS
from .entidades import Raqueta



class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla
        self.reloj.tick(FPS)

    def bucle_principal(self):
        """
        Este método debe ser implementado por cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida.
        """
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        
        self.logo = pg.image.load(
            os.path.join("resources", "images", "arkanoid_name.png"))
        
        font_file = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(font_file, 40)
        
    def bucle_principal(self):
        salir = False
        
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:
                    pg.quit()

            self.pantalla.fill((99, 0, 0))
            
            self.pintar_logo()
            self.pintar_texto()

            pg.display.flip()

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO / 3
        self.pantalla.blit(self.logo,(pos_x, pos_y))

    def pintar_texto(self):
        mensaje = "Pulsa espacio para empezar"
        texto = self.tipografia.render(mensaje, True, COLOR_MENSAJE)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto) / 2
        pos_y = .75 * ALTO
        self.pantalla.blit(texto, (pos_x, pos_y))

"""
1. Cargar la imagen de fondo en memoria ---- hecho
2. Creamos una función para "pintar_fondo"
3. Llamar a la función "pintar_fondo" en el bucle principal para que el
   fondo se pinte
"""
class Partida(Escena):
    
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        bg_file = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(bg_file)
        self.jugador = Raqueta()
    
    def bucle_principal(self):
        salir = False
        while not salir:
            self.reloj.ti
            self.jugador.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            
            self.pantalla.fill((0, 0, 66))
            self.pintar_fondo()

            # probar a puntar la raqueta
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            
            pg.display.flip()
    
    def pintar_fondo(self):
        self.pantalla.blit(self.fondo, (0, 0))

class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()