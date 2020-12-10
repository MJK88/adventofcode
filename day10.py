with open("data10.in", "r") as f:
    lines = sorted([int(x) for x in f.read().splitlines()])

# part 1
lines.append(max(lines) + 3)
num_diff = [lines[0]] + [lines[i + 1] - lines[i] for i, x in enumerate(lines[:-1])]
print(num_diff.count(1) * num_diff.count(3))

# part 2
# get indices where difference changes from 1 to 3, 3 to 1 and 3 to 3
idx_change = [
    i
    for i, x in enumerate(num_diff)
    if num_diff[i - 1] != x or (x == num_diff[i - 1] == 3)
]

# get distance between indices like before
# this represents the number of consecutive ones and not threes
idx_diff = [idx_change[0]] + [
    idx_change[i + 1] - idx_change[i] for i, x in enumerate(idx_change[:-1])
]

# i.e. if 4 consecutive ones -> number of permutations is 7
# multiply all num of permutations to the power of their occurences
product = 1
for y, z in zip([1, 2, 3, 4], [1, 2, 4, 7]):
    product *= z ** idx_diff.count(y)
print(product)
