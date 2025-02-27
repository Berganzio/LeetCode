import numpy as np

class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        # Create a 3x3 board
        board = np.full((3, 3), "", dtype=str)
        # Set current player
        current = "X"
        # Fill the board with the moves
        for i, (row, col) in enumerate(moves):
            board[row][col] = current
            current = "O" if current == "X" else "X"
        # Check rows for a winner
        for row in board:
            if list(row) == ["X", "X", "X"]:
                return "A"
            elif list(row) == ["O", "O", "O"]:
                return "B"
        # Check columns for a winner
        for col in board.T:
            if list(col) == ["X", "X", "X"]:
                return "A"
            elif list(col) == ["O", "O", "O"]:
                return "B"
        # Check diagonals for a winner
        if list(board.diagonal()) == ["X", "X", "X"]:
            return "A"
        elif list(board.diagonal()) == ["O", "O", "O"]:
            return "B"
        if list(board[::-1].diagonal()) == ["X", "X", "X"]:
            return "A"
        elif list(board[::-1].diagonal()) == ["O", "O", "O"]:
            return "B"
        # Check for draw or pending
        if len(moves) == 9:
            return "Draw"
        return "Pending"

# test
print(Solution().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))