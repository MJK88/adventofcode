import math

with open("data5.in", "r") as f:
    lines = f.read().splitlines()

# part 1
ids = []
for line in lines:
    row = [0, 127]
    column = [0, 7]
    for x in line:
        if x == "F":
            row[1] = math.floor(row[1] - abs(row[0] - row[1]) / 2)
        elif x == "B":
            row[0] = math.ceil(row[0] + abs(row[0] - row[1]) / 2)
        elif x == "L":
            column[1] = math.floor(column[1] - abs(column[0] - column[1]) / 2)
        elif x == "R":
            column[0] = math.ceil(column[0] + abs(column[0] - column[1]) / 2)
    ids.append(8 * row[0] + column[0])
print(f"max seat ID: {max(ids)}")

# part 2
print(
    next(
        i
        for i in range(min(ids), max(ids))
        if (i not in ids and i - 1 in ids and i + 1 in ids)
    )
)
