import turtle
from board import Board
from tokens import Token

class Logic(Board, Token):
    def __init__(self, cells, mode):
        Board.__init__(self, cells)
        Token.__init__(self)
        self.mode = mode
        self.player = 0

        if mode == 1:
            self.neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        else:
            self.neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        self.score1 = turtle.Turtle(visible = False)
        self.score2 = turtle.Turtle(visible = False)
        self.play_text = turtle.Turtle(visible = False)

    def initial_board(self):
        base_coordinate_1 = int(self.cells / 2)
        base_coordinate_2 = int(self.cells / 2) - 1

        self.draw_token((base_coordinate_2, base_coordinate_2), 0)
        self.draw_token((base_coordinate_2, base_coordinate_1), 1)
        self.draw_token((base_coordinate_1, base_coordinate_2), 1)
        self.draw_token((base_coordinate_1, base_coordinate_1), 0)

        self.board_matrix[base_coordinate_2][base_coordinate_2] = 1
        self.board_matrix[base_coordinate_2][base_coordinate_1] = 2
        self.board_matrix[base_coordinate_1][base_coordinate_2] = 2
        self.board_matrix[base_coordinate_1][base_coordinate_1] = 1

        self.black_score(self.score1)
        self.white_score(self.score1)
        self.black_available(self.score2)
        self.white_available(self.score2)

    def playing(self):
        self.black_play_text(self.play_text)
        print("Turn for black token")
        self.player = 0
        turtle.onscreenclick(self.othello_black)
        turtle.mainloop()

    def othello_black(self, x, y):
        if self.available_turn() == True:
            self.get_selection(x, y)
            if self.player_choice != () and self.check(self.player_choice) == True:
                turtle.onscreenclick(None)
                self.put_token()
            else:
                print("Make a valid selection")
                return

            self.player = 1
            if self.available_turn() == False:
                if self.count[0] > self.count[1]:
                    print("Black tokens win " + str(self.count[0]) + " to " + str(self.count[1]) + " over white tokens")
                elif self.count[0] < self.count[1]:
                    print("White tokens win " + str(self.count[1]) + " to " + str(self.count[0]) + " over black tokens")
                elif self.availables[0] == 0:
                    print("Oh no, no more available black tokens, white tokens wins")
                elif self.availables[1] == 0:
                    print("Oh no, no more available white tokens, black tokens wins")
                else:
                    print("Game over, ¡is a tie!")

            elif self.count[0] >= 32 or self.count[1] >= 32:
                print("Black tokens win " + str(self.count[0]) + " to " + str(self.count[1]) + " over white tokens")

            else:
                self.empty_play_text(self.play_text)
                self.white_play_text(self.play_text)
                print("Turn for white token")
                turtle.onscreenclick(self.othello_white)
        else:
            return
    
    def othello_white(self, x, y):
        self.player = 1
        if self.available_turn() == True:
            self.get_selection(x, y)
            if self.player_choice != () and self.check(self.player_choice) == True:
                turtle.onscreenclick(None)
                self.put_token()
            else:
                print("Make a valid selection")
                return
            
            self.player = 0
            if self.available_turn() == False:
                if self.count[0] > self.count[1]:
                    print("Black tokens win " + str(self.count[0]) + " to " + str(self.count[1]) + " over white tokens")
                elif self.count[0] < self.count[1]:
                    print("White tokens win " + str(self.count[1]) + " to " + str(self.count[0]) + " over black tokens")
                elif self.availables[0] == 0:
                    print("Oh no, no more available black tokens, white tokens wins")
                elif self.availables[1] == 0:
                    print("Oh no, no more available white tokens, black tokens wins")
                else:
                    print("Game over, ¡is a tie!")
            elif self.count[0] >= 32 or self.count[1] >= 32:
                print("White tokens win " + str(self.count[1]) + " to " + str(self.count[0]) + " over black tokens")
            else:
                self.empty_play_text(self.play_text)
                self.black_play_text(self.play_text)
                print("Turn for black token")
                turtle.onscreenclick(self.othello_black)
        else:
            return

    def available_turn(self):
        for i in range(self.cells):
            for j in range(self.cells):
                evaluation = (i, j)
                if self.check(evaluation) == True:
                    return True
                else:
                    continue
            continue
        return False

    def valid_row_column(self, row, column):
        if 0 <= row < self.cells and 0 <= column <self.cells:
            return True
        return False
    
    def check(self, evaluation):
        if self.board_matrix[evaluation[0]][evaluation[1]] == 0:
            for direction in self.neighbors:
                if self.adjacent(evaluation, direction) == True and self.chain(evaluation, direction) == True:
                    return True
            return False
    
    def adjacent(self, evaluation, direction):
        new_token = self.player + 1
        row_to_evaluate = evaluation[0] + (direction[0] * 1)
        column_to_evaluate = evaluation[1] + (direction[1] * 1)          
        if self.valid_row_column(row_to_evaluate, column_to_evaluate) == False or self.board_matrix[row_to_evaluate][column_to_evaluate] == 0:
            return False
        elif self.board_matrix[row_to_evaluate][column_to_evaluate] == new_token:
            return False
        else:
            return True
    
    def chain(self, evaluation, direction):
        new_token = self.player + 1
        for i in list(range(1, self.cells)):
            row_to_evaluate = evaluation[0] + (direction[0] * i)
            column_to_evaluate = evaluation[1] + (direction[1] * i)          
            if self.valid_row_column(row_to_evaluate, column_to_evaluate) == False or self.board_matrix[row_to_evaluate][column_to_evaluate] == 0:
                return False
            elif self.board_matrix[row_to_evaluate][column_to_evaluate] == new_token:
                return True
            else:
                continue
    
    def capture_tokens(self):
        new_token = self.player + 1
        for direction in self.neighbors:
            if self.chain(self.player_choice, direction):
                for i in list(range(1, self.cells)):
                    row_to_evaluate = self.player_choice[0] + (direction[0] * i)
                    column_to_evaluate = self.player_choice[1] + (direction[1] * i)
                    if self.board_matrix[row_to_evaluate][column_to_evaluate] == new_token:
                        break
                    else:
                        if self.valid_row_column(row_to_evaluate, column_to_evaluate) == False or self.board_matrix[row_to_evaluate][column_to_evaluate] == 0:
                            continue
                        else:
                            self.board_matrix[row_to_evaluate][column_to_evaluate] = new_token
                            self.count_placed_tokens(self.player)
                            self.count_removed_board_tokens((self.player + 1) % 2)
                            self.return_tokens((self.player + 1) % 2)
                            self.draw_token((row_to_evaluate, column_to_evaluate), self.player)
                            self.available_tokens(self.player)
                            continue
            continue
    
    def put_token(self):
        self.board_matrix[self.player_choice[0]][self.player_choice[1]] = self.player + 1
        self.count_placed_tokens(self.player)
        self.available_tokens(self.player)
        self.draw_token(self.player_choice, self.player)
        self.capture_tokens()
        self.empty_score(self.score1)
        self.empty_available(self.score2)
        self.black_score(self.score1)
        self.white_score(self.score1)
        self.black_available(self.score2)
        self.white_available(self.score2)
        
    def black_score(self, black_score):
        black_score.penup()
        black_score.goto(15, (((-(self.cells * self.cell_size) / 2)) - 90))
        black_score.write(self.count[0], align = "center", font=("Arial", 12, "normal"))
        black_score.hideturtle()
        
    def white_score(self, white_score):
        white_score.penup()
        white_score.goto(15, ((-(self.cells * self.cell_size) / 2) - 140))
        white_score.write(self.count[1], align = "center", font=("Arial", 12, "normal"))
        white_score.hideturtle()

    def empty_score(self, score):
        score.clear()

    def black_available(self, black_available):
        black_available.penup()
        black_available.goto((((self.cells * self.cell_size) / 4) + 35), ((-(self.cells * self.cell_size) / 2) - 90))
        black_available.write(self.availables[0], align = "center", font=("Arial", 12, "normal"))
        black_available.hideturtle()
        
    def white_available(self, white_available):
        white_available.penup()
        white_available.goto((((self.cells * self.cell_size) / 4) + 35), ((-(self.cells * self.cell_size) / 2) - 140))
        white_available.write(self.availables[1], align = "center", font=("Arial", 12, "normal"))
        white_available.hideturtle()

    def empty_available(self, available):
        available.clear()

    def black_play_text(self, black_play_text):
        black_play_text.penup()
        black_play_text.goto(0, (((self.cells * self.cell_size) / 2) + 30))
        black_play_text.write("Player 1 plays...", align = "center", font=("Georgia", 15, "normal"))
        black_play_text.hideturtle()
    
    def white_play_text(self, white_play_text):
        white_play_text.penup()
        white_play_text.goto(0, (((self.cells * self.cell_size) / 2) + 30))
        white_play_text.write("Player 2 plays...", align = "center", font=("Georgia", 15, "normal"))
        white_play_text.hideturtle()
    
    def empty_play_text(self, play_text):
        play_text.clear()