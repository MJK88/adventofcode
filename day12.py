with open("data12.in", "r") as f:
    lines = [[x[0], int(x[1:])] for x in f.read().splitlines()]

# part 1
N = 0
E = 0
facing = 90
for x in lines:
    if x[0] == "N" or (x[0] == "F" and facing == 0):
        N += x[1]
    elif x[0] == "E" or (x[0] == "F" and facing == 90):
        E += x[1]
    elif x[0] == "S" or (x[0] == "F" and facing == 180):
        N -= x[1]
    elif x[0] == "W" or (x[0] == "F" and facing == 270):
        E -= x[1]
    elif x[0] == "R":
        facing += x[1]
    elif x[0] == "L":
        facing -= x[1]
    if facing >= 360:
        facing -= 360
    elif facing < 0:
        facing += 360

print(abs(N) + abs(E))

# part 2
ship = [0, 0]
wp = [10, 1]  # E, N

for x in lines:
    if x[0] == "N":
        wp[1] += x[1]
    elif x[0] == "E":
        wp[0] += x[1]
    elif x[0] == "S":
        wp[1] -= x[1]
    elif x[0] == "W":
        wp[0] -= x[1]
    elif x[0] == "F":
        ship = [sum(i) for i in zip(ship, [j * x[1] for j in wp])]
    elif (x[0] == "R" and x[1] == 90) or (x[0] == "L" and x[1] == 270):
        wp = [wp[1], -wp[0]]
    elif (x[0] == "R" or x[0] == "L") and x[1] == 180:
        wp = [-wp[0], -wp[1]]
    elif (x[0] == "R" and x[1] == 270) or (x[0] == "L" and x[1] == 90):
        wp = [-wp[1], wp[0]]

print(sum(map(abs, ship)))