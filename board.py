import turtle
import math

turtle.title("OTHELLO by Diego Moscoso")

class Board():
    def __init__(self, cells = 8, cell_size = 70, token_size = 25, line_color = "black", board_color = "forest green", token_color = ["black", "white"]):
        self.cells = cells
        self.cell_size = cell_size
        self.token_size = token_size
        self.line_color = line_color
        self.board_color = board_color
        self.token_color = token_color
        self.player_choice = ()
        self.board_matrix = [[0 for i in range(cells)] for j in range(cells)]

    def print_board(self):
        turtle.setup((self.cells * self.cell_size) + (2 * self.cell_size), (self.cells * self.cell_size) + (10 * self.cell_size))
        turtle.bgpic("Wood.gif")
        turtle.screensize((self.cells * self.cell_size), (self.cells * self.cell_size))
        
        board = turtle.Turtle(visible = False)
        board.penup()
        board.speed(0)

        board.color(self.line_color, self.board_color)
        board.width(8)

        corner = -(self.cells * self.cell_size) / 2
        board.goto(corner, corner)

        board.begin_fill()
        for i in range(4):
            board.pendown()
            board.forward(self.cell_size * self.cells)
            board.left(90)
        board.end_fill()

        board.width(3)
        board.left(90)

        for i in range(self.cells):
            board.goto((corner + self.cell_size * i) , corner)
            board.pendown()
            board.forward(self.cell_size * self.cells)
            board.penup()

        board.left(90)

        for i in range(self.cells):
            board.goto(-corner, (corner + self.cell_size * i))
            board.pendown()
            board.forward(self.cell_size * self.cells)
            board.penup()

        turtle.penup()
        turtle.goto(0, (((self.cells / 2) * self.cell_size) + 220))
        turtle.write("Othello", align = "center", font=("Georgia", 50, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto((-(self.cells / 4) * self.cell_size), (((self.cells / 2) * self.cell_size) + 90))
        turtle.write("# fichas\n negras\n en tablero", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto(((self.cells / 4) * self.cell_size), (((self.cells / 2) * self.cell_size) + 90))
        turtle.write("# fichas\n blancas\n en tablero", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto((-(self.cells / 4) * self.cell_size), ((-(self.cells / 2) * self.cell_size) - 210))
        turtle.write("# fichas\n negras\n disponibles", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

        turtle.penup()
        turtle.goto(((self.cells / 4) * self.cell_size), ((-(self.cells / 2) * self.cell_size) - 210))
        turtle.write("# fichas\n blancas\n disponibles", align = "center", font=("Georgia", 25, "normal"))
        turtle.hideturtle()

    def board_limit(self, x, y):
        limit = (self.cells * self.cell_size) / 2
        if (x > -limit and x < limit) and (y > -limit and y < limit):
            return True
        else:
            return False
    
    def lines(self, x, y):
        if (x % self.cell_size != 0 or y % self.cell_size != 0):
            return False
        else:
            return True
        
    def row_column(self, x, y):
        if self.board_limit(x, y) == True:
            row = math.floor(((- y // self.cell_size) + self.cells/2))
            column = math.floor(((x // self.cell_size) + self.cells/2))
            return (row, column)
        return ()

    def get_selection(self, x, y):
        if self.board_limit(x, y) == True and self.lines(x, y) == False:
            self.player_choice = self.row_column(x, y)
        else:
            self.player_choice = ()

    def coordinate_draw_token(self, coordinate):
        row = coordinate[0]
        column = coordinate[1]

        position_y = (((self.cells - 1) / 2) - row) * self.cell_size

        if column < (self.cells / 2):
            position_x = ((column - ((self.cells - 1) / 2)) * self.cell_size) - self.token_size
            radius = - self.token_size
        else:
            position_x = ((column - ((self.cells - 1) / 2)) * self.cell_size) + self.token_size
            radius = self.token_size

        return ((position_x, position_y), radius)  
    
    def draw_token(self, coordinate, color):
        information = self.coordinate_draw_token(coordinate)
        coordinates = information[0]
        radius = information[1]

        token = turtle.Turtle(visible=False)
        token.penup()
        token.speed(0)

        token.color(self.token_color[0], self.token_color[color])

        token.setposition(coordinates)
        token.setheading(90)

        token.begin_fill()
        token.pendown()
        token.circle(radius)
        token.end_fill()