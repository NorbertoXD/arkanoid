import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO, ANCHO

"""
1. Crear una clase Raqueta
   a. Sea un Sprite
   b. El metodo update es el que se encarga de gestionarla
2. Situarlo con las coordenadas y para eso, obtener el rectangulo
3. Metodo mostrar_paleta
4. En el bucle principal llamar a mostrar_paleta


Para animar las imagenes:
1. Funcion "animar" con una lista de imagenes y las mostramos en bucle
"""


class Raqueta(Sprite):

    margen_inferior = 20
    
    def __init__(self) -> None:
        super().__init__()

        self.sprites = [
           pg.image.load(os.path.join("resources", "images", "electric00.png")),
           pg.image.load(os.path.join("resources", "images", "electric00.png")),
           pg.image.load(os.path.join("resources", "images", "electric00.png")),



        ]
        
        
        image_path = os.path.join("resources", "images", "electric00.png")
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-self.margen_inferior))
        
    def update(self):
        # self.rect.x = self.rect.x + 1
        self.image = self.sprites[self.contador]
        self.contador

