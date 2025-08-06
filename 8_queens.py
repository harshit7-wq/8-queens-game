def print_board(board):
    """Print the chessboard with Q for queens and . for empty."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""

    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n, solutions):
    """Try to place queens row by row using backtracking."""
    if row == n:
        # All queens placed successfully; save solution
        solutions.append([r[:] for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack


def main():
    n = 8
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, n, solutions)
    print(f"Total solutions for {n}-Queens: {len(solutions)}\n")

    # Print all solutions
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution #{idx}:")
        print_board(solution)


if __name__ == "__main__":
    main()
