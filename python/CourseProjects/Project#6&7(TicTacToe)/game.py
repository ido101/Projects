import player
import time


class TicTacToe:
    def __init__(self):
        self.board = [str(i) for i in range(9)]
        self.current_winner = None

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:i*3+3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot.isdigit()]

    def empty_squares(self):
        for i in self.board:
            if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
                return True
        return False

    def make_move(self, move, letter):
        if self.board[move].isdigit():
            self.board[move] = letter
            if self.winner(letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, letter):
        if (self.board[0] == letter and self.board[1] == letter and self.board[2] == letter) or (self.board[3] == letter and self.board[4] == letter and self.board[5] == letter) or (self.board[6] == letter and self.board[7] == letter and self.board[8] == letter) or (self.board[0] == letter and self.board[3] == letter and self.board[6] == letter) or (self.board[1] == letter and self.board[4] == letter and self.board[7] == letter) or (self.board[2] == letter and self.board[5] == letter and self.board[8] == letter) or (self.board[0] == letter and self.board[4] == letter and self.board[8] == letter) or (self.board[2] == letter and self.board[4] == letter and self.board[6] == letter):
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = 'X'  # starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        elif letter == 'X':
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " won!")
                return letter

            letter = "O" if letter == "X" else "X"
        else:
            print("Invalid move")
        if print_game:
            time.sleep(0.8)

    if print_game:
        print("Its a tie")
    return None


if __name__ == "__main__":
    while True:
        human_or_comp = input("Enter number of players(1 or 2): ")
        while human_or_comp not in ["1", "2"]:
            human_or_comp = input("Please enter a valid number of players! ")
        if human_or_comp == "1":
            x = player.HumanPlayer("X")
            o = player.GeniusComputerPlayer("O")
        else:
            x = player.HumanPlayer("X")
            o = player.HumanPlayer("O")
        g = TicTacToe()
        play(g, x, o)
        p_a = input("Do you want to play again?(y or n)").lower().strip()
        if p_a == "n":
            quit("Bye")
