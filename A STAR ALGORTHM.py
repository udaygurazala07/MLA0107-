# A* Algorithm

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {},
    'E': {},
    'F': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 0,
    'E': 0,
    'F': 0
}

open_list = ['A']
closed_list = []

g = {'A': 0}

parents = {'A': 'A'}

while open_list:

    n = None

    for v in open_list:
        if n == None or g[v] + heuristic[v] < g[n] + heuristic[n]:
            n = v

    if n == None:
        break

    if n == 'D':
        path = []

        while parents[n] != n:
            path.append(n)
            n = parents[n]

        path.append('A')
        path.reverse()

        print("Path:", path)
        break

    for m in graph[n]:

        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parents[m] = n
            g[m] = g[n] + graph[n][m]

        else:
            if g[m] > g[n] + graph[n][m]:
                g[m] = g[n] + graph[n][m]
                parents[m] = n

    open_list.remove(n)
    closed_list.append(n)
