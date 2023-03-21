"""
Crear class Escena

"""

import os
import pygame


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()

    def bucle_principal():
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        ruta = os.path.join("resources", "fondo-nocturna-galaxia.jpg")
        self.fondo = pygame.image.load(ruta)
        ruta_tipo = os.path.join("resources", "CabinSketch-Bold.ttf")
        self.tipografia = pygame.font.Font(ruta_tipo, 28)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    salir = True
            self.pantalla.fill((15, 15, 15))
            pygame.display.flip()
        return False
    
class Partida(Escena):
    pass


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
            self.pantalla.fill((0, 0, 99))
            pygame.display.flip()
        return False