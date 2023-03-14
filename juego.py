import turtle
from logica import Logica

def main():
    numero = int(turtle.textinput("Tamaño del tablero: ", "Digita el tamaño del tablero, recuerda que debe ser un número que a su vez define las filas y columnas:"))

    if numero % 2 == 0 and numero >= 4:
        print ("¡Vamos a jugar!")
    else:
        print ("Error, el número debe ser par y mayor o igual a 4")
        numero = int(turtle.textinput("Tamaño del tablero", "Digita el tamaño del tablero, recuerda que debe ser un número que a su vez define las filas y columnas:"))
    
    tipo = int(turtle.textinput("Modo de juego: ", "Digita 1 para estilo vecindades de Von Neumann o 2 para estilo libre:"))

    if tipo < 1 or tipo > 2:
        print("Error, digita 1 o 2")
        tipo = int(turtle.textinput("Modo de juego", "Digita 1 para estilo vecindades de Von Neumann o 2 para estilo libre:"))
        
    juego = Logica(numero, tipo)
    juego.imprimir_tablero()
    juego.tablero_inicial()
    juego.jugando()

main()