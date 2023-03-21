import os
import pygame 
from . import ALTO, ANCHO
from .escenas import Portada, Partida, MejoresJugadores

class TheQuest:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption()

        # Windows: resources\images\icon.png
        # Mac/Linux: resources/images/icon.png
        ruta = os.path.join("resources", "fondo-nocturna-galaxia.jpg")
        icono = pygame.image.load(ruta)
        pygame.display.set_icon(icono)

        objeto_portada = Portada(self.pantalla)
        objeto_partida = Partida(self.pantalla)
        objeto_mejores = MejoresJugadores(self.pantalla)

        self.escenas = [
            objeto_portada,
            objeto_partida,
            objeto_mejores
        ]

        # Escrito de forma simplificada:
        #
        # self.escenas = [
        #     Portada(self.pantalla)
        #     Partida(self.pantalla)
        #     MejoresJugadores(self.pantalla)
        # ]

    def jugar(self):
        """Este es el bucle principal"""
        for escena in self.escenas:
            he_acabado = escena.bucle_principal()
            if he_acabado:
                # return
                break
        print("He acabado el for")
        pygame.quit()