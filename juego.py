from mapa import *
import sys

RES = W, H = 1600, 900
class Juego():
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode(RES)
        self.reloj = pg.time.Clock()
        self.nuevo_juego()

    def nuevo_juego(self):
        self.map = Mapa(self)

    def actualizar(self):
        pg.display.flip()
        self.reloj.tick(30)

    def dibujar(self):
        self.ventana.fill("black")
        self.map.draw()

    def mantener_venatana(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def jugar(self):
        while True:
            self.mantener_venatana()
            self.actualizar()
            self.dibujar()

            
        

    
