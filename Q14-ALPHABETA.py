def alphabeta(depth, alpha, beta, maxPlayer):
    if depth == 0:
        return 1
    if maxPlayer:
        value = -999
        for _ in range(2):
            value = max(value, alphabeta(depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = 999
        for _ in range(2):
            value = min(value, alphabeta(depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

print(alphabeta(3, -999, 999, True))
