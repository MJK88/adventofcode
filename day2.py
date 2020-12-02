import re

with open("data2.in", "r") as f:
    lines = f.readlines()

i = 0
j = 0
for x in lines:
    a, b, c, d = re.match(r"(\d+)-(\d+) (\w): (\w*)", x).groups()

    # part 1
    if int(a) <= d.count(c) <= int(b):
        i += 1

    # part 2
    if (d[int(a) - 1] == c) != (d[int(b) - 1] == c):
        j += 1

print("part 1: {}, part 2: {}".format(i, j))

# short solutions
# Part One
print(sum([int(i) <= p.count(l) <= int(j) for i, j, l, p in re.findall(r'(\d+)-(\d+) (\w): (\w+)', open('data2.in').read())]))
# Part Two
print(sum([(p[int(i) - 1] == l) ^ (p[int(j) - 1] == l) for i, j, l, p in re.findall(r'(\d+)-(\d+) (\w): (\w+)', open('data2.in').read())]))