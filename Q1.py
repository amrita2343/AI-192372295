from collections import deque

goal = "123456780"

def get_moves(state):
    moves = []
    i = state.index('0')
    swap = [(i-1,i),(i+1,i),(i-3,i),(i+3,i)]
    for x,y in swap:
        if 0 <= x < 9:
            s = list(state)
            s[x], s[y] = s[y], s[x]
            moves.append("".join(s))
    return moves

def bfs(start):
    q = deque([(start, [])])
    visited = set()
    while q:
        state, path = q.popleft()
        if state == goal:
            return path + [state]
        visited.add(state)
        for move in get_moves(state):
            if move not in visited:
                q.append((move, path + [state]))

start = "123405678"
print(bfs(start))
