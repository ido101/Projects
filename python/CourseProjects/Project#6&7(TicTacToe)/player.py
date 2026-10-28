import random
import math


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = None
        try:
            square = int(input(self.letter + "'s turn. Enter your next move: "))
        except ValueError:
            while square not in game.available_moves():
                try:
                    square = int(input("Please enter a valid move! "))
                except ValueError:
                    pass
        return square


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)["position"]
        return square

    def minimax(self, game, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if game.current_winner == other_player:
            return {"position": None, "score": 1 * (len(game.available_moves()) + 1) if other_player == max_player else -1 * (len(game.available_moves()) + 1)}
        elif not game.empty_squares():
            return {"position": None, "score": 0}
        # initialize some dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for possible_move in game.available_moves():
            # step 1: make a move, try that spot
            game.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(game, other_player)  # now, we alternate players
            # step 3: undo the move
            game.board[possible_move] = str(possible_move)
            game.current_winner = None
            # step 4: update dictionaries if necessary
            sim_score['position'] = possible_move
            if player == max_player:
                if sim_score["score"] > best['score']:
                    best = sim_score
            else:
                if sim_score["score"] < best['score']:
                    best = sim_score
        return best
