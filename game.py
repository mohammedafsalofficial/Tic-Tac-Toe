import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # single list to represent 3x3 board
        self.current_winner = None

    # Display the board
    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # Display the board with the index
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # Return the available moves in the board
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    # Return true if empty spots in the board
    def empty_squares(self):
        return ' ' in self.board

    # Return the number of empty spots in the board
    def num_empty_squares(self):
        return self.board.count(' ')

    # Assign the letter to the valid square and return true if successful
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        # Checking in the row for the winner
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Checking in the column for the winner
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Checking in the diagonals for the winner
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all(spot == letter for spot in diagonal2):
                return True

        return False  # if all these fails


def play(game, x_player, o_player, print_game=True):
    # Return the winner of the game(the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    while game.empty_squares():
        # Get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print()  # just an empty line

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'  # switching players

        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    tic_tac_toe_game = TicTacToe()
    play(tic_tac_toe_game, x_player, o_player, print_game=True)
