class Mapa():
    def __init__(self, archivo):
        self.archivo = archivo
        open(self.mapa, "a")
        self.mapa= []

    def converitr(self):
        for i in self.archivo:
            self.mapa.append(i)

        return self.mapa
