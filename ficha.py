
class Ficha():
    def __init__(self, cantidad = 32, conteo = [2, 2], disponibles = [30, 30]):
        self.cantidad = cantidad
        self.conteo = conteo
        self.disponibles = disponibles

    def conteo_fichas_puestas(self, jugador):
        if jugador == 0:
            self.conteo[0] += 1
        else:
            self.conteo[1] += 1
    
    def fichas_disponibles(self, jugador): 
        if jugador == 0:
            self.disponibles[0] -= 1
        else:
            self.disponibles[1] -= 1

    def conteo_fichas_quitadas_tablero(self, jugador):
        if jugador == 0:
            self.conteo[0] -= 1
        else:
            self.conteo[1] -= 1

    def fichas_devueltas(self, jugador):
        if jugador == 0:
            self.disponibles[0] += 1
        else:
            self.disponibles[1] += 1