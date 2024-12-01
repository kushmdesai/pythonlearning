class CheckersGame:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.current_player = 'X'

    def initialize_board(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    if row < 3:
                        self.board[row][col] = 'X'
                    elif row > 4:
                        self.board[row][col] = 'O'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        # Implement your move validation logic here
        return True

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = ' '
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    def play(self):
        self.initialize_board()
        while True:
            self.print_board()
            print(f"Current player: {self.current_player}")
            start_row, start_col = map(int, input("Enter start position (row col): ").split())
            end_row, end_col = map(int, input("Enter end position (row col): ").split())
            self.make_move(start_row, start_col, end_row, end_col)

if __name__ == "__main__":
    game = CheckersGame()
    game.play()
