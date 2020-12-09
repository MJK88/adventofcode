from itertools import combinations

with open("data9.in", "r") as f:
    lines = [int(x) for x in f.read().splitlines()]


def check(preamble, number):
    for x in combinations(preamble, 2):
        if sum(x) == number:
            return True
    return False


for i in range(25, len(lines)):
    preamble = lines[i - 25 : i]
    number = lines[i]
    sum_exists = check(preamble, number)
    if not sum_exists:
        invalid = number
        print(f"{number} has no pair in preamble: {preamble}")


for i in range(2, 20):
    for j in range(len(lines) - i + 1):
        xslice = lines[j : j + i]
        print(xslice)
        if sum(xslice) == invalid:
            print(f"sum {xslice} is {invalid}")
            print(f"min + max is {min(xslice) + max(xslice)}")
            break
