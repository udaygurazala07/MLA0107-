graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
def ucs(start, goal):
    visited = []
    queue = [(0, start, [start])] 

    while queue:
        queue.sort()  
        cost, node, path = queue.pop(0)
        if node == goal:
            print("Shortest Path:", path)
            print("Total cost:", cost)
            return
        if node not in visited:
            visited.append(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    queue.append((cost + weight, neighbor, path + [neighbor]))
ucs('A', 'F')
