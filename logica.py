import turtle
from board import Board
from tokens import Token

class Logica(Tablero, Ficha):
    def __init__(self, celdas, tipo):
        Tablero.__init__(self, celdas)
        Ficha.__init__(self)
        self.tipo = tipo
        self.jugador = 0

        if tipo == 1:
            self.vecindades = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        else:
            self.vecindades = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        self.marcador1 = turtle.Turtle(visible = False)
        self.marcador2 = turtle.Turtle(visible = False)

    def tablero_inicial(self):
        coordenada_base_1 = int(self.celdas / 2)
        coordenada_base_2 = int(self.celdas / 2) - 1

        self.dibujar_ficha((coordenada_base_2, coordenada_base_2), 0)
        self.dibujar_ficha((coordenada_base_2, coordenada_base_1), 1)
        self.dibujar_ficha((coordenada_base_1, coordenada_base_2), 1)
        self.dibujar_ficha((coordenada_base_1, coordenada_base_1), 0)

        self.matriz_tablero[coordenada_base_2][coordenada_base_2] = 1
        self.matriz_tablero[coordenada_base_2][coordenada_base_1] = 2
        self.matriz_tablero[coordenada_base_1][coordenada_base_2] = 2
        self.matriz_tablero[coordenada_base_1][coordenada_base_1] = 1

        self.marcador_negro(self.marcador1)
        self.marcador_blanco(self.marcador1)
        self.disponible_negro(self.marcador2)
        self.disponible_blanco(self.marcador2)

    def jugando(self):
        print("Turno ficha negra")
        self.jugador = 0
        turtle.onscreenclick(self.othello_negra)
        turtle.mainloop()

    def othello_negra(self, x, y):
        if self.turno_disponible() == True:
            self.obtener_seleccion(x, y)
            if self.eleccion_jugador != () and self.comprobacion(self.eleccion_jugador) == True:
                turtle.onscreenclick(None)
                self.poner_ficha()
            else:
                print("Realiza una selección válida")
                return

            self.jugador = 1
            if self.turno_disponible() == False:
                if self.conteo[0] > self.conteo[1]:
                    print("Victoria de las fichas negras " + str(self.conteo[0]) + " a " + str(self.conteo[1]) + " sobre las fichas blancas")
                elif self.conteo[0] < self.conteo[1]:
                    print("Victoria de las fichas blancas " + str(self.conteo[1]) + " a " + str(self.conteo[0]) + " sobre las fichas negras")
                elif self.disponibles[0] == 0:
                    print("Oh no, no hay mas fichas negras disponibles, victoria de las fichas blancas")
                elif self.disponibles[1] == 0:
                    print("Oh no, no hay mas fichas blancas disponibles, victoria de las fichas negras")
                else:
                    print("Juego finalizado, ¡hay empate!")

            else:
                print("Turno ficha blanca")
                turtle.onscreenclick(self.othello_blanca)
        else:
            return
    
    def othello_blanca(self, x, y):
        self.jugador = 1
        if self.turno_disponible() == True:
            self.obtener_seleccion(x, y)
            if self.eleccion_jugador != () and self.comprobacion(self.eleccion_jugador) == True:
                turtle.onscreenclick(None)
                self.poner_ficha()
            else:
                print("Realiza una selección válida")
                return
            
            self.jugador = 0
            if self.turno_disponible() == False:
                if self.conteo[0] > self.conteo[1]:
                    print("Victoria de las fichas negras " + str(self.conteo[0]) + " a " + str(self.conteo[1]) + " sobre las fichas blancas")
                elif self.conteo[0] < self.conteo[1]:
                    print("Victoria de las fichas blancas " + str(self.conteo[1]) + " a " + str(self.conteo[0]) + " sobre las fichas negras")
                elif self.disponibles[0] == 0:
                    print("Oh no, no hay mas fichas negras disponibles, victoria de las fichas blancas")
                elif self.disponibles[1] == 0:
                    print("Oh no, no hay mas fichas blancas disponibles, victoria de las fichas negras")
                else:
                    print("Juego finalizado, ¡hay empate!")
            else:
                print("Turno ficha negra")
                turtle.onscreenclick(self.othello_negra)
        else:
            return

    def turno_disponible(self):
        for i in range(self.celdas):
            for j in range(self.celdas):
                evaluacion = (i, j)
                if self.comprobacion(evaluacion) == True:
                    return True
                else:
                    continue
            continue
        return False

    def fila_columna_valido(self, fila, columna):
        if 0 <= fila < self.celdas and 0 <= columna <self.celdas:
            return True
        return False
    
    def comprobacion(self, evaluacion):
        if self.matriz_tablero[evaluacion[0]][evaluacion[1]] == 0:
            for direccion in self.vecindades:
                if self.adyacente(evaluacion, direccion) == True and self.cadena(evaluacion, direccion) == True:
                    return True
            return False
    
    def adyacente(self, evaluacion, direccion):
        ficha_nueva = self.jugador + 1
        fila_evaluar = evaluacion[0] + (direccion[0] * 1)
        columna_evaluar = evaluacion[1] + (direccion[1] * 1)          
        if self.fila_columna_valido(fila_evaluar, columna_evaluar) == False or self.matriz_tablero[fila_evaluar][columna_evaluar] == 0:
            return False
        elif self.matriz_tablero[fila_evaluar][columna_evaluar] == ficha_nueva:
            return False
        else:
            return True
    
    def cadena(self, evaluacion, direccion):
        ficha_nueva = self.jugador + 1
        for i in list(range(1, self.celdas)):
            fila_evaluar = evaluacion[0] + (direccion[0] * i)
            columna_evaluar = evaluacion[1] + (direccion[1] * i)          
            if self.fila_columna_valido(fila_evaluar, columna_evaluar) == False or self.matriz_tablero[fila_evaluar][columna_evaluar] == 0:
                return False
            elif self.matriz_tablero[fila_evaluar][columna_evaluar] == ficha_nueva:
                return True
            else:
                continue
    
    def capturar_fichas(self):
        ficha_nueva = self.jugador + 1
        for direccion in self.vecindades:
            if self.cadena(self.eleccion_jugador, direccion):
                for i in list(range(1, self.celdas)):
                    fila_evaluar = self.eleccion_jugador[0] + (direccion[0] * i)
                    columna_evaluar = self.eleccion_jugador[1] + (direccion[1] * i)
                    if self.matriz_tablero[fila_evaluar][columna_evaluar] == ficha_nueva:
                        break
                    else:
                        if self.fila_columna_valido(fila_evaluar, columna_evaluar) == False or self.matriz_tablero[fila_evaluar][columna_evaluar] == 0:
                            continue
                        else:
                            self.matriz_tablero[fila_evaluar][columna_evaluar] = ficha_nueva
                            self.conteo_fichas_puestas(self.jugador)
                            self.conteo_fichas_quitadas_tablero((self.jugador + 1) % 2)
                            self.fichas_devueltas((self.jugador + 1) % 2)
                            self.dibujar_ficha((fila_evaluar, columna_evaluar), self.jugador)
                            self.fichas_disponibles(self.jugador)
                            continue
            continue
    
    def poner_ficha(self):
        self.matriz_tablero[self.eleccion_jugador[0]][self.eleccion_jugador[1]] = self.jugador + 1
        self.conteo_fichas_puestas(self.jugador)
        self.fichas_disponibles(self.jugador)
        self.dibujar_ficha(self.eleccion_jugador, self.jugador)
        self.capturar_fichas()
        self.borrar_marcador(self.marcador1)
        self.borrar_disponible(self.marcador2)
        self.marcador_negro(self.marcador1)
        self.marcador_blanco(self.marcador1)
        self.disponible_negro(self.marcador2)
        self.disponible_blanco(self.marcador2)
        print(self.conteo)
        print(self.disponibles)
        
    def finalizar_juego(self):
        if self.turno_disponible() == False or self.conteo[0] >= 32 or self.conteo[1] >= 32 or self.disponibles[0] == 0 or self.disponibles[1] == 0:
            return True
        else:
            return False
        
    def marcador_negro(self, marcador_negro):
        marcador_negro.penup()
        marcador_negro.goto((-(self.celdas / 4) * self.tamaño_celda), (((self.celdas / 2) * self.tamaño_celda) + 35))
        marcador_negro.write(self.conteo[0], align = "center", font=("Georgia", 35, "normal"))
        marcador_negro.hideturtle()
        
    def marcador_blanco(self, marcador_blanco):
        marcador_blanco.penup()
        marcador_blanco.goto(((self.celdas / 4) * self.tamaño_celda), (((self.celdas / 2) * self.tamaño_celda) + 35))
        marcador_blanco.write(self.conteo[1], align = "center", font=("Georgia", 35, "normal"))
        marcador_blanco.hideturtle()

    def borrar_marcador(self, marcador):
        marcador.clear()

    def disponible_negro(self, disponible_negro):
        disponible_negro.penup()
        disponible_negro.goto((-(self.celdas / 4) * self.tamaño_celda), ((-(self.celdas / 2) * self.tamaño_celda) - 80))
        disponible_negro.write(self.disponibles[0], align = "center", font=("Georgia", 35, "normal"))
        disponible_negro.hideturtle()
        
    def disponible_blanco(self, disponible_blanco):
        disponible_blanco.penup()
        disponible_blanco.goto(((self.celdas / 4) * self.tamaño_celda), ((-(self.celdas / 2) * self.tamaño_celda) - 80))
        disponible_blanco.write(self.disponibles[1], align = "center", font=("Georgia", 35, "normal"))
        disponible_blanco.hideturtle()

    def borrar_disponible(self, disponible):
        disponible.clear()