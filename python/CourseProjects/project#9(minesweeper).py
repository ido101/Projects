import random
import time


# create a board object to represent the game
# this is where we can say "create a new board object" or "dig here" or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        # create the board
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()
        # initialize a set of location we've uncovered
        # we will save (row, col) tuples into this set
        self.dug = set()

    def assign_values_to_board(self):
        for i in range(self.dim_size):
            for j in range(self.dim_size):
                if self.board[i][j] == "*":
                    continue
                self.board[i][j] = self.get_num_close_bombs(i, j)

    def get_num_close_bombs(self, row, col):
        num = 0
        for i in range(max(0, row - 1), min(self.dim_size, (row + 1) + 1)):
            for j in range(max(0, col - 1), min(self.dim_size, (col + 1) + 1)):
                if i == row and j == col:
                    continue
                if self.board[i][j] == "*":
                    num += 1
        return num

    def make_new_board(self):
        # created an empty board
        b = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # random location on board
            loc = random.randint(0, self.dim_size ** 2 - 1)
            # get row and column of location
            row = loc // self.dim_size
            col = loc % self.dim_size
            if b[row][col] == "*":
                # this means we've planted a bomb so continue without increasing bombs planted
                continue
            b[row][col] = "*"
            bombs_planted += 1
        return b

    def dig(self, row, col):
        self.dug.add((row, col))  # keep track that we dug here
        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True
        for i in range(max(0, row - 1), min(self.dim_size, (row + 1) + 1)):
            for j in range(max(0, col - 1), min(self.dim_size, (col + 1) + 1)):
                if (i, j) in self.dug:
                    continue  # don't dig where you already dug
                self.dig(i, j)

        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        print(" | ", end="")
        for i in range(self.dim_size):
            print(f"{i} | ", end="")
        print()
        for i in range(self.dim_size):
            print(f"{i}| ", end="")
            for j in range(self.dim_size):
                print(visible_board[i][j], end="   ")
            print()
        return ""

    def print_full_board(self):
        print(" | ", end="")
        for i in range(self.dim_size):
            print(f"{i} | ", end="")
        print()
        for i in range(self.dim_size):
            print(f"{i}| ", end="")
            for j in range(self.dim_size):
                print(self.board[i][j], end="   ")
            print()


# play the game
def play(dim_size=10, num_bombs=10):
    start = time.time()
    # create board and plant bombs
    board = Board(dim_size, num_bombs)
    # repeat the steps until there is no place to dig - Victory
    while len(board.dug) < dim_size ** 2 - num_bombs:
        # show the user the board and ask them where they want to dig
        print(board)
        d = input("Where do you want to dig? (row, column)")
        loc = d.split(",")
        row = int(loc[0])
        col = int(loc[1])

        # if the location is safe, dig until each square is next to a bomb
        safe = board.dig(row, col)
        # if the location is a bomb show game over
        if not safe:
            print("GAME OVER")
            board.print_full_board()
            break
    else:
        end = time.time()
        print("YOU WON!")
        print("Took you: " + str(end-start) + " seconds")
        print(board)


if __name__ == "__main__":
    play()
