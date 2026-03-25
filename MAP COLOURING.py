# Map Coloring using CSP

states = ['A', 'B', 'C', 'D']

colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

solution = {}

def safe(state, color):
    for n in neighbors[state]:
        if n in solution and solution[n] == color:
            return False
    return True


def solve(state_index):

    if state_index == len(states):
        return True

    state = states[state_index]

    for color in colors:
        if safe(state, color):
            solution[state] = color

            if solve(state_index + 1):
                return True

            del solution[state]

    return False


solve(0)

print("Solution:")
for s in solution:
    print(s, "->", solution[s])
