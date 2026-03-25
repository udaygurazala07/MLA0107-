# Feed Forward Neural Network (Moderate)

# input weights
w1 = 0.3
w2 = 0.4
w3 = 0.5
w4 = 0.2

# hidden to output weights
w5 = 0.6
w6 = 0.7

bias1 = -0.2
bias2 = -0.3
bias3 = -0.4


def step(x):
    if x >= 0:
        return 1
    else:
        return 0


# input
x1 = int(input("Enter first input (0/1): "))
x2 = int(input("Enter second input (0/1): "))


# hidden layer
h1 = step(x1*w1 + x2*w2 + bias1)
h2 = step(x1*w3 + x2*w4 + bias2)


# output layer
out = step(h1*w5 + h2*w6 + bias3)


print("Output:", out)
