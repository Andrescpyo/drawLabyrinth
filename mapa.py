import pygame as pg

class Archivo():
    def __init__(self, archivo):
        self.archivo = archivo
        self.mapa= []

    def converitr(self):
        with open (self.archivo, 'r') as f:
            for linea in f:
                self.mapa.append(list(linea))
            
            for i in range(len(self.mapa)):
                if self.mapa[i][-1] == '\n':
                    self.mapa[i].pop()
            
            for i in range(len(self.mapa)):
                for j in range(len(self.mapa[i])):
                    try:
                        self.mapa[i][j] = int(self.mapa[i][j])
                    except ValueError:
                        pass

        return self.mapa

a= "C:/Users/Fabian/Documents/GitHub/drawLabyrinth/mapa.txt"
c=Archivo(a)
mapa= c.converitr()

class Mapa():
    def __init__(self, juego):
        self.juego = juego
        self.conversion_mapa = mapa
        self.mapa = {}
        self.obtener_mapa()

    def obtener_mapa(self):
        for j, columna in enumerate(self.conversion_mapa):
            for i, valor in enumerate(columna):
                if valor:
                    self.mapa[(i, j)] = valor

    def draw(self):
        [pg.draw.rect(self.juego.ventana, 'darkgray', (pos[0] * 30, pos[1]* 30,30,30),2) 
        for pos in self.mapa]

if __name__ == "__main__":
    print(mapa)