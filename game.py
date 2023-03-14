import turtle
from logic import Logic

def main():
    number = int(turtle.textinput("Size of board", "Enter the size of board, remember must be a number that define at same time rows and columns:"))

    if number % 2 == 0 and number >= 4:
        print ("¡Let's play!")
    else:
        print ("Error, the number must be a pair number and greater than or equal to 4")
        number = int(turtle.textinput("Size of board", "Enter the size of board, remember must be a number that define at same time rows and columns:"))
    
    mode = int(turtle.textinput("Mode of game", "Enter 1 for use the Von Neumann Neighborhoods for adjacency or 2 for free mode:"))

    if mode < 1 or mode > 2:
        print("Error, enter 1 or 2")
        mode = int(turtle.textinput("Mode of game", "Enter 1 for use the Von Neumann Neighborhoods for adjacency or 2 for free mode:"))
        
    game = Logic(number, mode)
    game.print_board()
    game.initial_board()
    game.playing()

main()