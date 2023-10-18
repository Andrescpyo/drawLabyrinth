from mapa import *
import pygame as pg
import sys

mapa = "C:/User/\Estudiantes/Desktop/laberinto/mapa.txt"
class Juego():
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode((1600,900))
        self.nuevo_juego()

    def nuevo_juego(self):
        self.mapa = Mapa(mapa)

    def actualizar(self):
        pg.display.flip()

    def dibujar(self):
        self.ventana.fill("black")
        self.mapa.dibujar()

    def ventana(self):
        for i in pg.event.get():
            if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_SCAPE):
                pg.quit()
                sys.exit()

    def jugar(self):
        while True:
            self.ventana()
            self.actualizar()
            self.dibujar()

            
        

    
