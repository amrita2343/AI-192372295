import heapq

graph = {'A':[('B',1),('C',3)],
         'B':[('D',3)],
         'C':[('D',1)],
         'D':[]}

h = {'A':3,'B':2,'C':1,'D':0}

def astar(start, goal):
    pq = [(0,start)]
    visited = set()

    while pq:
        cost,node = heapq.heappop(pq)
        if node == goal:
            print("Reached")
            return
        if node in visited:
            continue
        visited.add(node)

        for n,w in graph[node]:
            heapq.heappush(pq,(cost+w+h[n],n))

astar('A','D')
