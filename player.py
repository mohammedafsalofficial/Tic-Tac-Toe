import math
import random


class Player:
    # letter is x or o
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Get a random valid spot for computer
    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Get a valid spot for human
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class AIComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Predicting the right spot to minimize the defeat
    def get_move(self, game):
        return random.choice(game.available_moves()) if len(game.available_moves()) == 9 else self.minimax(game, self.letter)['position']

    # Minimax Algorithm
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # If someone wins
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }
        # If Draw
        elif not state.num_empty_squares():
            return {
                'position': None,
                'score': 0
            }

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # maximizer
        else:
            best = {'position': None, 'score': math.inf}  # minimizer

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # now, we alternate players
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # Update the best possible score
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
