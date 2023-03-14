import turtle
import math

turtle.title("OTHELLO by Diego Moscoso")

class Tablero():
    def __init__(self, celdas = 8, tamaño_celda = 70, tamaño_ficha = 25, color_linea = "black", color_tablero = "forest green", color_ficha = ["black", "white"]):
        self.celdas = celdas
        self.tamaño_celda = tamaño_celda
        self.tamaño_ficha = tamaño_ficha
        self.color_linea = color_linea
        self.color_tablero = color_tablero
        self.color_ficha = color_ficha
        self.eleccion_jugador = ()
        self.matriz_tablero = [[0 for i in range(celdas)] for j in range(celdas)]

    def imprimir_tablero(self):
        turtle.setup((self.celdas * self.tamaño_celda) + (2 * self.tamaño_celda), (self.celdas * self.tamaño_celda) + (10 * self.tamaño_celda))
        turtle.bgpic("Wood.gif")
        turtle.screensize((self.celdas * self.tamaño_celda), (self.celdas * self.tamaño_celda))
        
        tablero = turtle.Turtle(visible = False)
        tablero.penup()
        tablero.speed(0)

        tablero.color(self.color_linea, self.color_tablero)
        tablero.width(8)

        esquina = -(self.celdas * self.tamaño_celda) / 2
        tablero.goto(esquina, esquina)

        tablero.begin_fill()
        for i in range(4):
            tablero.pendown()
            tablero.forward(self.tamaño_celda * self.celdas)
            tablero.left(90)
        tablero.end_fill()

        tablero.width(3)
        tablero.left(90)

        for i in range(self.celdas):
            tablero.goto((esquina + self.tamaño_celda * i) , esquina)
            tablero.pendown()
            tablero.forward(self.tamaño_celda * self.celdas)
            tablero.penup()

        tablero.left(90)

        for i in range(self.celdas):
            tablero.goto(-esquina, (esquina + self.tamaño_celda * i))
            tablero.pendown()
            tablero.forward(self.tamaño_celda * self.celdas)
            tablero.penup()

        turtle.penup()
        turtle.goto(0, (((self.celdas / 2) * self.tamaño_celda) + 220))
        turtle.write("Othello", align = "center", font=("Georgia", 50, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto((-(self.celdas / 4) * self.tamaño_celda), (((self.celdas / 2) * self.tamaño_celda) + 90))
        turtle.write("# fichas\n negras\n en tablero", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto(((self.celdas / 4) * self.tamaño_celda), (((self.celdas / 2) * self.tamaño_celda) + 90))
        turtle.write("# fichas\n blancas\n en tablero", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto((-(self.celdas / 4) * self.tamaño_celda), ((-(self.celdas / 2) * self.tamaño_celda) - 210))
        turtle.write("# fichas\n negras\n disponibles", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto(((self.celdas / 4) * self.tamaño_celda), ((-(self.celdas / 2) * self.tamaño_celda) - 210))
        turtle.write("# fichas\n blancas\n disponibles", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

    def limite_tablero(self, x, y):
        limite = (self.celdas * self.tamaño_celda) / 2
        if (x > -limite and x < limite) and (y > -limite and y < limite):
            return True
        else:
            return False
    
    def lineas(self, x, y):
        if (x % self.tamaño_celda != 0 or y % self.tamaño_celda != 0):
            return False
        else:
            return True
        
    def fila_columna(self, x, y):
        if self.limite_tablero(x, y) == True:
            fila = math.floor(((- y // self.tamaño_celda) + self.celdas/2))
            columna = math.floor(((x // self.tamaño_celda) + self.celdas/2))
            return (fila, columna)
        return ()

    def obtener_seleccion(self, x, y):
        if self.limite_tablero(x, y) == True and self.lineas(x, y) == False:
            self.eleccion_jugador = self.fila_columna(x, y)
        else:
            self.eleccion_jugador = ()

    def coordenada_dibujo_ficha(self, coordenada):
        fila = coordenada[0]
        columna = coordenada[1]

        posicion_y = (((self.celdas - 1) / 2) - fila) * self.tamaño_celda

        if columna < (self.celdas / 2):
            posicion_x = ((columna - ((self.celdas - 1) / 2)) * self.tamaño_celda) - self.tamaño_ficha
            radio = - self.tamaño_ficha
        else:
            posicion_x = ((columna - ((self.celdas - 1) / 2)) * self.tamaño_celda) + self.tamaño_ficha
            radio = self.tamaño_ficha

        return ((posicion_x, posicion_y), radio)  
    
    def dibujar_ficha(self, coordenada, color):
        informacion = self.coordenada_dibujo_ficha(coordenada)
        coordenadas = informacion[0]
        radio = informacion[1]

        ficha = turtle.Turtle(visible=False)
        ficha.penup()
        ficha.speed(0)

        ficha.color(self.color_ficha[0], self.color_ficha[color])

        ficha.setposition(coordenadas)
        ficha.setheading(90)

        ficha.begin_fill()
        ficha.pendown()
        ficha.circle(radio)
        ficha.end_fill()