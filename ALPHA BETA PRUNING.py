# Alpha Beta Pruning

values = [3, 5, 6, 9, 1, 2, 0, -1]


def alphabeta(depth, node, maxPlayer, alpha, beta):

    if depth == 3:
        return values[node]

    if maxPlayer:
        best = -1000

        for i in range(2):
            val = alphabeta(depth + 1, node*2 + i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for i in range(2):
            val = alphabeta(depth + 1, node*2 + i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


result = alphabeta(0, 0, True, -1000, 1000)

print("Best value:", result)
