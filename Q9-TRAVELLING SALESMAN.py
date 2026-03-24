from itertools import permutations

graph = [[0,10,15,20],
         [10,0,35,25],
         [15,35,0,30],
         [20,25,30,0]]

n = 4
min_cost = float('inf')

for p in permutations(range(1,n)):
    cost = graph[0][p[0]]
    for i in range(len(p)-1):
        cost += graph[p[i]][p[i+1]]
    cost += graph[p[-1]][0]
    min_cost = min(min_cost, cost)

print(min_cost)
