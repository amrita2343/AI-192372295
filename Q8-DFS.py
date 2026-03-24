graph = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':[], 'E':[]}

def dfs(node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(n, visited)

dfs('A')
