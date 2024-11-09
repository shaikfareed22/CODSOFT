import numpy as np
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = PLAYER_X
    def print_board(self):
        symbols = {EMPTY: '.', PLAYER_X: 'X', PLAYER_O: 'O'}
        for row in self.board:
            print(" ".join(symbols[cell] for cell in row))
        print()

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def is_draw(self):
        return np.all(self.board != EMPTY)

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == EMPTY]

    def make_move(self, row, col):
        if self.board[row, col] == EMPTY:
            self.board[row, col] = self.current_player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row, col] = EMPTY

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def minimax(self, depth, is_maximizing):
        if self.is_winner(PLAYER_X):
            return -1
        if self.is_winner(PLAYER_O):
            return 1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -np.inf
            for move in self.available_moves():
                self.make_move(move[0], move[1])
                score = self.minimax(depth + 1, False)
                self.undo_move(move[0], move[1])
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = np.inf
            for move in self.available_moves():
                self.make_move(move[0], move[1])
                score = self.minimax(depth + 1, True)
                self.undo_move(move[0], move[1])
                best_score = min(best_score, score)
            return best_score

    def best_move(self):
        best_score = -np.inf
        move = None
        for m in self.available_moves():
            self.make_move(m[0], m[1])
            score = self.minimax(0, False)
            self.undo_move(m[0], m[1])
            if score > best_score:
                best_score = score
                move = m
        return move

def play_game():
    game = TicTacToe()
    while True:
        game.print_board()
        if game.current_player == PLAYER_X:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if not game.make_move(row, col):
                print("Invalid move. Try again.")
                continue
        else:
            move = game.best_move()
            if move:
                game.make_move(move[0], move[1])
                print(f"AI played move: {move[0]} {move[1]}")

        if game.is_winner(game.current_player):
            game.print_board()
            print(f"Player {'X' if game.current_player == PLAYER_X else 'O'} wins!")
            break
        elif game.is_draw():
            game.print_board()
            print("It's a draw!")
            break

        game.switch_player()
if __name__ == "__main__":
    play_game()

    # install ibraries:
    # pip install numpy
    # run the code n python environment.

