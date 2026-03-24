def minimax(depth, isMax):
    if depth == 0:
        return 0
    if isMax:
        return max(minimax(depth-1, False), minimax(depth-1, False))
    else:
        return min(minimax(depth-1, True), minimax(depth-1, True))

print(minimax(3, True))
