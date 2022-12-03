from itertools import combinations


with open("2022/day03.input", "r") as f:
    lines = f.read().splitlines()


def PrioritiesAlphabet(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96


priorities = []
for x in lines:
    halfs = [x[: len(x) // 2], x[len(x) // 2 :]]
    common = list(set.intersection(*map(set, halfs)))[0]
    priorities.append(PrioritiesAlphabet(common))

print(sum(priorities))

priorities = []
linesThree = [lines[x : x + 3] for x in range(0, len(lines), 3)]
for x in linesThree:
    common = list(set.intersection(*map(set, x)))[0]
    priorities.append(PrioritiesAlphabet(common))

print(sum(priorities))
