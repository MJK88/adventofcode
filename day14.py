import re

with open("data14.in", "r") as f:
    lines = f.read().splitlines()

mem = {}
for x in lines:
    if x.startswith("mask"):
        mask = x.split(" = ")[1]

    if match := re.match(r"mem\[(\d+)\] = (\d+)", x):
        result = list(f"{int(match.group(2)):0>36b}")
        for i, char in enumerate(mask):
            if char != "X":
                result[i] = char
        mem[match.group(1)] = int("".join(result), 2)

print(sum(x for x in mem.values()))