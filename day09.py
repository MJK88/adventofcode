from itertools import combinations

with open("data9.in", "r") as f:
    lines = [int(x) for x in f.read().splitlines()]


def check(preamble, number):
    for x in combinations(preamble, 2):
        if sum(x) == number:
            return True
    return False


# part 1
for i in range(25, len(lines)):
    sum_exists = check(lines[i - 25 : i], lines[i])
    if not sum_exists:
        invalid = lines[i]
        print(f"{lines[i]} has no sum pair in preamble")

# part 2
for i in range(2, 20):
    for j in range(len(lines) - i):
        xslice = lines[j : j + i]
        if sum(xslice) == invalid:
            print(f"min + max = {min(xslice) + max(xslice)}")
            break

# short solution 1
for i in range(25, len(lines)):
    if not lines[i] in {
        sum(x) for x in combinations(lines[i - 25 : i], 2) if x[0] != x[1]
    }:
        break
print(lines[i])