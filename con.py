def check_diagonals_right(board):
  """
  Checks if there are any winning diagonals (from right to left) on the board.

  Args:
    board: A 2D list representing the game board.

  Returns:
    True if there is a winning diagonal, False otherwise.
  """

  # Iterate over the board from the top-right corner to the bottom-left corner.
  for row in range(len(board)):
    for col in range(len(board[0])):
      # Check if the current cell is the start of a winning diagonal.
      if board[row][col] != 0 and check_diagonal_right(board, row, col):
        return True

  # If no winning diagonals are found, return False.
  return False


def check_diagonal_right(board, row, col):
  """
  Checks if there is a winning diagonal (from right to left) starting from the given cell.

  Args:
    board: A 2D list representing the game board.
    row: The row of the starting cell.
    col: The column of the starting cell.

  Returns:
    True if there is a winning diagonal, False otherwise.
  """

  # Get the value of the starting cell.
  value = board[row][col]

  # Iterate over the diagonal from the starting cell to the bottom-right corner.
  for i in range(1, len(board)):
    # Check if the current cell is off the board or has a different value than the starting cell.
    if row + i >= len(board) or col - i < 0 or board[row + i][col - i] != value:
      return False

  # If all cells on the diagonal have the same value, return True.
  return True
