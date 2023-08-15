import random

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def backtracking(n):
    board = [-1] * n
    row = 0

    board[0] = random.randint(0, n-1)
    
    while row < n:
        col = board[row] + 1

        while col < n:
            if is_safe(board, row, col):
                board[row] = col
                row += 1
                break
            col += 1

        if col == n:
            board[row] = -1
            row -= 1

        elif row == n:
            return board

    return None
