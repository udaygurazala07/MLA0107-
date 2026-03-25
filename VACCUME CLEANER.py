# Vacuum Cleaner Problem

rooms = ["dirty", "dirty"]   # room A and room B
pos = 0   # start at room A (0 = A, 1 = B)

for i in range(2):

    if rooms[pos] == "dirty":
        print("Room", pos, "is dirty")
        print("Cleaning room", pos)
        rooms[pos] = "clean"

    else:
        print("Room", pos, "is clean")

    pos = pos + 1

print("All rooms clean")
