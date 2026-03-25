# Travelling Salesman Problem

from itertools import permutations

graph = {
    'A': {'A':0,'B':10,'C':15,'D':20},
    'B': {'A':10,'B':0,'C':35,'D':25},
    'C': {'A':15,'B':35,'C':0,'D':30},
    'D': {'A':20,'B':25,'C':30,'D':0}
}

cities = ['B','C','D']

min_path = 999
best_path = ()

for p in permutations(cities):

    cost = 0
    k = 'A'

    for j in p:
        cost += graph[k][j]
        k = j

    cost += graph[k]['A']

    if cost < min_path:
        min_path = cost
        best_path = p


print("Minimum cost:", min_path)
print("Path: A", best_path, "A")
