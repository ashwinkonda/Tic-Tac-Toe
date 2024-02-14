class TicTacToe:
    # Initialization
    def __init__(self):
        self.moves = [str(i) for i in range(1, 10)]
        self.player_turn = 1
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

    # Game logic
    def print_board(self):
        for i in range(0, 9, 3):
            print("    ".join(self.moves[i:i+3]))

        winner = self.check_winner()
        tie = self.check_tie()
        if winner:
            print(winner)
            return
        elif tie:
            print(tie)
            return

        self.make_move()

    def make_move(self):
        player = self.get_player()
        move = self.get_valid_move()
        self.moves[move] = player
        self.player_turn += 1
        self.print_board()

    # Helper methods
    def get_valid_move(self):
        player = self.get_player()
        try:
            move = int(input(f"(Player {player}) Make your move (1 - 9): ")) - 1
            if 0 <= move < 9 and self.moves[move].isdigit():
                return move
            else:
                print("Invalid move, try again.")
                return self.get_valid_move()
        except ValueError:
            print("Invalid move, try again.")
            return self.get_valid_move()

    def get_player(self):
        if self.player_turn % 2 == 0:
            return "O"
        else:
            return "X"

    # Win and tie condition methods
    def check_winner(self):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for pos in winning_positions:
            if self.moves[pos[0]] == self.moves[pos[1]] == self.moves[pos[2]]:
                return f"Player {self.moves[pos[0]]} wins!"
        return None

    def check_tie(self):
        if all(not move.isdigit() for move in self.moves):
            return "It's a tie!"
        return None


if __name__ == "__main__":
    newGame = TicTacToe()
