with open("data10.in", "r") as f:
    lines = sorted([int(x) for x in f.read().splitlines()])

# part 1
lines.append(max(lines) + 3)
difference = [lines[0]] + [lines[i + 1] - lines[i] for i, x in enumerate(lines[1:])]
print(difference.count(1) * difference.count(3))

