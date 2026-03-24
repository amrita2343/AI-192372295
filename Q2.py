N = 8

def safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve(board, col):
    if col == N:
        print(board)
        return True
    for i in range(N):
        if safe(board, i, col):
            board[col] = i
            if solve(board, col + 1):
                return True
    return False

solve([-1]*N, 0)
