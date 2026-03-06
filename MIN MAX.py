def minimax(values):
    max1 = max(values[0], values[1])
    max2 = max(values[2], values[3])
    max3 = max(values[4], values[5])
    max4 = max(values[6], values[7])
    min1 = min(max1, max2)
    min2 = min(max3, max4)
    result = max(min1, min2)
    return result
values = [2,3,5,9,0,1,7,5]
print("MAX MIN :")
print("Optimal Value:", minimax(values))
