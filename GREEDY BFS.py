graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',3), ('E',1)],
    'C': [('F',5)],
    'D': [],
    'E': [('F',2)],
    'F': []
}
h = {'A':6, 'B':4, 'C':4, 'D':3, 'E':2, 'F':0}
def greedy_bfs(start, goal):
    open_list = [start]
    visited = []
    parent = {start: None}
    cost = {start: 0}
    while open_list:
        n = open_list[0]

        for i in open_list:
            if h[i] < h[n]:
                n = i
        if n == goal:
            path = []
            while n:
                path.append(n)
                n = parent[n]
            path.reverse()
            return path, cost[goal]
        open_list.remove(n)
        visited.append(n)

        for (m, c) in graph[n]:
            if m not in visited:
                open_list.append(m)
                parent[m] = n
                cost[m] = cost[parent[m]] + c
    return None
path, total_cost = greedy_bfs('A','F')
print("Greedy BFS :")
print("Shortest Path:", path)
print("Cost:", total_cost)
