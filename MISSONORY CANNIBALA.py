# Missionaries and Cannibals Problem

M = 3
C = 3
boat = 'left'

print("M C Boat")

while True:

    print(M, C, boat)

    # goal condition
    if M == 0 and C == 0:
        print("Goal reached")
        break

    # move 1 missionary and 1 cannibal
    if boat == 'left':
        M -= 1
        C -= 1
        boat = 'right'

    else:
        M -= 1
        C -= 1
        boat = 'left'

    # safety condition
    if M < 0 or C < 0:
        break
