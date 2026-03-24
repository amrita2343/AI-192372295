from collections import deque

def water_jug(x, y, target):
    visited = set()
    q = deque([(0,0)])

    while q:
        a,b = q.popleft()
        if (a,b) in visited:
            continue
        print(a,b)
        visited.add((a,b))

        if a==target or b==target:
            return

        q.extend([(x,b),(a,y),(0,b),(a,0),
                  (max(0,a-(y-b)), min(y,a+b)),
                  (min(x,a+b), max(0,b-(x-a)))])

water_jug(4,3,2)
