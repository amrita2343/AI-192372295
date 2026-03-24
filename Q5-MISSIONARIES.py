from collections import deque

def valid(m,c):
    return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)

def bfs():
    q = deque([(3,3,1,[])])
    visited = set()

    while q:
        m,c,boat,path = q.popleft()
        if (m,c,boat) in visited:
            continue
        visited.add((m,c,boat))

        if m==0 and c==0:
            print(path+[(m,c,boat)])
            return

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        for dm,dc in moves:
            if boat:
                nm, nc = m-dm, c-dc
            else:
                nm, nc = m+dm, c+dc

            if 0<=nm<=3 and 0<=nc<=3 and valid(nm,nc):
                q.append((nm,nc,1-boat,path+[(m,c,boat)]))

bfs()
