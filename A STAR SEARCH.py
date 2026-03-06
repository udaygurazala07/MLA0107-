graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

h = {'A':6, 'B':4, 'C':4, 'D':3, 'E':2, 'F':0}

def astar(start, goal):
    open_list = [start]
    g = {start:0}
    parent = {start:start}

    while open_list:
        n = open_list[0]

        for v in open_list:
            if g[v] + h[v] < g[n] + h[n]:
                n = v

        if n == goal:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            return path

        open_list.remove(n)

        for (m, cost) in graph[n]:
            if m not in open_list:
                open_list.append(m)
                parent[m] = n
                g[m] = g[n] + cost

    return None


print("A* Shortest Path:", astar('A','F'))
