from math import prod

with open("data3.in", "r") as f:
    lines = f.read().splitlines()

count = 0
for i, x in enumerate(lines):
    if x[i * 3 % len(x)] == "#":
        count += 1

print("number of trees: {}".format(count))

count = []
for a, b in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
    num = 0
    for i, x in enumerate(lines[::b]):
        if x[i * a % len(x)] == "#":
            num += 1
    count.append(num)

print("mult. of the number of trees of all slopes: {}".format(prod(count)))