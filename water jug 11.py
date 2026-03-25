# Water Jug Problem
# Jug1 = 4L, Jug2 = 3L
# Goal = 2L

jug1 = 0
jug2 = 0

# Step 1
jug2 = 3
print(jug1, jug2)

# Step 2
jug1 = jug2
jug2 = 0
print(jug1, jug2)

# Step 3
jug2 = 3
print(jug1, jug2)

# Step 4
temp = 4 - jug1
jug1 = 4
jug2 = jug2 - temp
print(jug1, jug2)

# Step 5
jug1 = 0
print(jug1, jug2)

# Step 6
jug1 = jug2
jug2 = 0
print(jug1, jug2)

print("Goal reached")
