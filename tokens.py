
class Token():
    def __init__(self, quantity = 32, count = [2, 2], availables = [30, 30]):
        self.quantity = quantity
        self.count = count
        self.availables = availables

    def count_placed_tokens(self, player):
        if player == 0:
            self.count[0] += 1
        else:
            self.count[1] += 1
    
    def available_tokens(self, player): 
        if player == 0:
            self.availables[0] -= 1
        else:
            self.availables[1] -= 1

    def count_removed_board_tokens(self, player):
        if player == 0:
            self.count[0] -= 1
        else:
            self.count[1] -= 1

    def return_tokens(self, player):
        if player == 0:
            self.availables[0] += 1
        else:
            self.availables[1] += 1