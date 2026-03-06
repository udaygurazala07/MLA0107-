def alphabeta(depth, index, isMax, values, alpha, beta):

    if depth == 3:
        return values[index]

    if isMax:
        best = -1000
        for i in range(2):
            val = alphabeta(depth+1, index*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000
        for i in range(2):
            val = alphabeta(depth+1, index*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [2,3,5,9,0,1,7,5]

result = alphabeta(0, 0, True, values, -1000, 1000)
print ("Alpha Beta Pruning :")
print("Optimal Value:", result)

