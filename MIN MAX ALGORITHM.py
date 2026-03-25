# Minimax Algorithm

values = [3, 5, 2, 9, 12, 5, 23, 23]


def minimax(depth, node, maxPlayer):

    if depth == 3:
        return values[node]

    if maxPlayer:
        best = -1000

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i, False)
            best = max(best, val)

        return best

    else:
        best = 1000

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i, True)
            best = min(best, val)

        return best


result = minimax(0, 0, True)

print("Best value:", result)
