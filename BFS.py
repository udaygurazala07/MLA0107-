from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(start):
    visited=[]
    queue=[]
    visited.append(start)
    queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
print("BFS:")
bfs('A')
